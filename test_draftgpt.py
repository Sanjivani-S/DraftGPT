import os

import requests


def draft_gpt(openai_api_key=os.environ["OPENAI_API_KEY"]):

    if openai_api_key is None:
        raise ValueError("OpenAI API key is not set in environment variables.")

    with open("incident_description.txt", "r") as file:
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
                "content": incident_desc,
            },
        ],
    }

    response = requests.post(url, headers=headers, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        print("Response from OpenAI:", response.json())
        print("\n")
        print(response.json()["choices"][0]["message"]["content"])

    else:
        print("Error:", response.status_code, response.text)

    return response.status_code


def test_draft_gpt():
    assert draft_gpt() == 200


if __name__ == "__main__":
    draft_gpt()
