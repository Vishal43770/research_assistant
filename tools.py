# this file has the helper functions / tools
import os
from dotenv import load_dotenv
load_dotenv()

def save_report(filename,content):
    if not os.path.exists("reports"):
        os.makedirs("reports")
    with open(filename,"w",encoding="utf-8") as f: # use 'a' for append
        f.write(content)
        return f"Report saved to {filename}"

def read_report(filename):
    path = os.path.join(filename)
    if not os.path.exists(path):
        return "No Report Found!"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        return content
def ask_ai(query):
    import requests, base64

    invoke_url = "https://integrate.api.nvidia.com/v1/chat/completions"
    stream = False

    headers = {
    "Authorization": os.getenv("API_KEY"),
    "Accept": "text/event-stream" if stream else "application/json"
    }

    payload = {
    "model": "mistralai/mistral-medium-3.5-128b",
    "reasoning_effort": "high",
    "messages": [{"role":"user","content":query}],
    "max_tokens": 16384,
    "temperature": 0.70,
    "top_p": 1.00,
    "stream": stream
    }

    response = requests.post(invoke_url, headers=headers, json=payload)

    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")
        exit(1)

    content = ""
    if stream:
        for line in response.iter_lines():
            if line:
                print(line.decode("utf-8"))
    else:
        response_json = response.json()
        content = response_json["choices"][0]["message"]["content"]
        # content = response_json["choices"][0]["message"]

        # print(content)

    if content:
        cleaned_text = "\n".join(
            line.strip().lstrip("*").strip().replace("**", "")
            for line in content.splitlines()
        )
        return cleaned_text
