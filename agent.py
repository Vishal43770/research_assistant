from tools import ask_ai, save_report,read_report
import os
import time
import json

def execute_agent(user_input):

    state = {
    "user_input": user_input,
    "topic": "",
    "action": "",
    "result": ""
}
    if "research" in user_input.lower():

        topic = user_input.replace("Research", "").strip()
        state["topic"] = topic
        state["action"] = "Research"
        start=time.time()
        response = ask_ai(
            f"Write a short report about {topic}")
        save_report(os.path.join("reports","report.md"), response)
        state["result"] = response
        end=time.time()-start
        print("\n\ncurrent state:")
        for key, value in state.items():
            if key == "result":
                print(f"  {key}:")
                # Print the markdown text with actual newlines indented
                print("\n".join(f"    {line}" for line in value.splitlines()))
            else:
                print(f"  {key}: {value}")
        # print(json.dumps(state, indent=4))
        print("\ntime taken: ",end)
        return response

    elif "read" in user_input.lower():
        state["action"] = "Read"
        content = read_report(os.path.join("reports","report.md"))
        start=time.time()
        end=time.time()-start
        state["result"] = content
        print("\n\ncurrent state:")
        for key, value in state.items():
            if key == "result":
                print(f"  {key}:")
                # Print the markdown text with actual newlines indented
                print("\n".join(f"    {line}" for line in value.splitlines()))
            else:
                print(f"  {key}: {value}")
        # print(json.dumps(state, indent=4))
        print("\ntime taken: ",end)
        return content

    else:
        state["action"] = "unknown"
        state["result"] = "I don't know what to do."
        print("\nCurrent State:")
         for key, value in state.items():
            if key == "result":
                print(f"  {key}:")
                # Print the markdown text with actual newlines indented
                print("\n".join(f"    {line}" for line in value.splitlines()))
            else:
                print(f"  {key}: {value}")
        # print(json.dumps(state, indent=4))
        print("\ntime taken: ",end)
        print(json.dumps(state, indent=4))
        return "I don't know what to do."



    