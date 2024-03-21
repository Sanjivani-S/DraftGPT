import requests
import json
import os

# test_draftgpt.py

def capital_case(x):
    return x.capitalize()


def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'


def draft_gpt(openai_api_key = "sk-na..."):
   # put yout api key here
  if openai_api_key is None:
      raise ValueError("OpenAI API key is not set in environment variables.")
  
  url = "https://api.openai.com/v1/chat/completions"
  
  headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {openai_api_key}"
  }
  
  data = {
      "model": "gpt-3.5-turbo",
      "messages": [
          {
              "role": "system",
              "content": "You are a helpful assistant."
          },
          {
              "role": "user",
              "content": "Hello!"
          }
      ]
  }
  
  response = requests.post(url, headers=headers, json=data)
  
  # Check if the request was successful
  if response.status_code == 200:
      print("Response from OpenAI:", response.json())
      print('\n')
      print(response.json()['choices'][0]['message']['content'])
  else:
      print("Error:", response.status_code, response.text)

def test_draft_gpt():
    assert capital_case('semaphore') == 'Semaphore'
