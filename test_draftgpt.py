import os
import requests
from urllib.parse import urlparse, parse_qs

def parse_slack_message_link(link):
    parsed_url = urlparse(link)
    query_params = parse_qs(parsed_url.query)
    return query_params.get("text", [""])[0]


def retrieve_slack_message(slack_message_link, slack_token):
    headers = {
        "Authorization": f"Bearer {slack_token}",
    }
    response = requests.get(slack_message_link, headers=headers)
    try:
        response_json = response.json()
        return response_json.get("text", "")
    except ValueError:
        print("Error: Response is not valid JSON")
        return ""


def draft_gpt(user_input, openai_api_key=os.environ["OPENAI_API_KEY"], gpt_model=os.environ["GPT_MODEL"]):

    if openai_api_key is None:
        raise ValueError("OpenAI API key is not set in environment variables.")

    '''
    with open("incident_descriptions/incident_description.txt", "r") as file:
        incident_desc = file.read().replace("\n", "")
    '''

    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}",
    }

    data = {
        "model": gpt_model,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
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

    '''
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    '''


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
    if slack_message_link and slack_token:
        user_input = retrieve_slack_message(slack_message_link, slack_token)
        if user_input:
            response = draft_gpt(user_input)
            if response:
                print("GPT response:", response)
            else:
                print("Failed to get GPT response.")
        else:
            print("Failed to retrieve user input from Slack message link.")
    else:
        print("SLACK_MESSAGE_LINK or SLACK_TOKEN environment variable not set.")
