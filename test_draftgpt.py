import os
import requests
import gradio

openai_api_key=os.environ["OPENAI_API_KEY"]

def draft_gpt(user_input):

    if openai_api_key is None:
        raise ValueError("OpenAI API key is not set in environment variables.")

    with open("incident_descriptions/incident_description.txt", "r") as file:
        incident_desc = file.read().replace("\n", "")

    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}",
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": user_input ##incident_desc,
            },
        ],
    }
  
    response = requests.post(url, headers=headers, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        ChatGPT_reply = response.json()["choices"][0]["message"]["content"]
        print(ChatGPT_reply) 
        
        file = open("report.txt", 'w')
        file.write(ChatGPT_reply)
        file.close()
        return ChatGPT_reply

    else:
        print("Error:", response.status_code, response.text)
        return response.status_code


def test_draft_gpt():
    assert draft_gpt() == 200


if __name__ == "__main__":
    demo = gradio.Interface(fn=draft_gpt, inputs = "text", outputs = "text", title = "EC2 troubleshooter for AWS")
    demo.launch()

    ## draft_gpt()
