import os
import requests
from urllib.parse import urlparse


def parse_slack_message_link(link):
    parsed_url = urlparse(link)
    if parsed_url.netloc.endswith('.slack.com'):
        # Extract channel ID from the path
        path_parts = parsed_url.path.strip('/').split('/')
        if len(path_parts) >= 3 and path_parts[-3] == 'archives':
            channel_id = path_parts[-2]
            message_id = path_parts[-1]
            return channel_id, message_id
    print("Error: Invalid Slack message link.")
    return None


def retrieve_slack_message(channel_id, message_id, slack_token):
    headers = {
        "Authorization": f"Bearer {slack_token}",
    }
    # Construct the request data
    timestamp = message_id[1:0]
    data = {
        "channel": channel_id,
        "latest": timestamp,
        "limit": 1,
        "inclusive": True
    }
    # Construct the API URL
    API_URL = "https://slack.com/api/conversations.history"
    print("API URL:", API_URL)  # Print the constructed API URL
    response = requests.get(API_URL, headers=headers, params=data)
    try:
        response_json = response.json()
        # Check if the response is successful
        if response_json["ok"]:
            # Extract the text of the first message
            message_text = response_json["messages"][0]["text"]
            return message_text
        else:
            print("Error:", response_json["error"])
            return None
    except (KeyError, IndexError):
        print("Error: No messages found in response.")
        return None


def draft_gpt(user_input, openai_api_key=os.environ["OPENAI_API_KEY"], gpt_model=os.environ["GPT_MODEL"]):

    if openai_api_key is None:
        raise ValueError("OpenAI API key is not set in environment variables.")

    
    with open("incident_descriptions/incident_description.txt", "r") as file:
        incident_desc = file.read().replace("\n", "")
    
    if user_input == None:
        user_input = incident_desc

    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}",
    }

    data = {
        "model": gpt_model,
        "messages": [
            {"role": "system", "content": "You are responsible for analyzing incident root causes at a software engineering company. Your tasks include extracting messages from users and systems and then determining the root cause of the incident in the incident report."},
            {
                "role": "user",
                "content": user_input,
            },
        ],
    }

    response = requests.post(url, headers=headers, json=data)
    # Check if the request was successful
    if response.status_code == 200:
        print("Response from OpenAI:", response.json())
        print("\n")
        print(response.json()["choices"][0]["message"]["content"])

        file = open("report.txt", 'w')
        file.write(response.json()["choices"][0]["message"]["content"])
        file.close()

    else:
        print("Error:", response.status_code, response.text)

    return response.status_code

 
def test_draft_gpt():
    test_inputs = [
            "What is the capital of Sweden?",
            "Please solve this math problem: 1+1"
            ]

    for user_input in test_inputs:
        response = draft_gpt(user_input)

        assert response != "", f"Response for input '{user_input}' should not be empty"


if __name__ == "__main__":
    slack_message_link = os.getenv("MESSAGE_LINK")
    slack_token = os.getenv("SLACK_TOKEN")
    
    if slack_message_link:
        parsed_link = parse_slack_message_link(slack_message_link)
        if parsed_link:
            slack_channel_id, message_id = parsed_link
        else:
            slack_channel_id = None
            message_id = None
    else:
        slack_channel_id = None
        message_id = None
    
    if slack_channel_id and message_id:
        print("Slack channel ID:", slack_channel_id, "Message ID:", message_id)
        user_input = retrieve_slack_message(slack_channel_id, message_id, slack_token)
    else:
        print("No valid Slack message link provided. Running draft_gpt without user input.")
        user_input = None
    
    response = draft_gpt(user_input)
    if response:
        print("GPT response:", response)
    else:
        print("Failed to get GPT response.")
