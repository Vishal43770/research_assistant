# main file the exceutes the agent 

import os 
from tools import save_report


# import requests, base64

# invoke_url = "https://integrate.api.nvidia.com/v1/chat/completions"
# stream = False


# load_dotenv()

# headers = {
#   "Authorization": os.getenv("API_KEY"),
#   "Accept": "text/event-stream" if stream else "application/json"
# }

# payload = {
#   "model": "mistralai/mistral-medium-3.5-128b",
#   "reasoning_effort": "high",
#   "messages": [{"role":"user","content":"HI TELL ME WHO IS YOUR GOD IN SHORT IN 5 LIKES BELOW 250 CHARS"}],
#   "max_tokens": 16384,
#   "temperature": 0.70,
#   "top_p": 1.00,
#   "stream": stream
# }

# response = requests.post(invoke_url, headers=headers, json=payload)

# if response.status_code != 200:
#     print(f"Error {response.status_code}: {response.text}")
#     exit(1)

# content = ""
# if stream:
#     for line in response.iter_lines():
#         if line:
#             print(line.decode("utf-8"))
# else:
#     response_json = response.json()
#     content = response_json["choices"][0]["message"]["content"]
#     print(content)

# if content:
#     cleaned_text = "\n".join(
#         line.strip().lstrip("*").strip().replace("**", "")
#         for line in content.splitlines()
#     )

# caling the save report function from tools.py

from tools import ask_ai
query=[
    """ 
    can u explain what is right
    """
]
import time
start=time.time()
content = ask_ai(query)
end=time.time()
print("time taken: ",end-start)
result = save_report(os.path.join("reports", "report.md"), content)
# print(content)
# print(result)

from tools import read_report

report_content = read_report(os.path.join("reports", "report.md"))
# print("\n--- Saved Report ---")
# print(report_content)