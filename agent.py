from tools import ask_ai, save_report

def execute_agent(query):
    print("Question : "+query)
    content = ask_ai(query)
    print("Answer : "+content)
    save_report(os.path.join("reports", "report.md"), content)
    return content

