# this file act as memory 


from typing import TypedDict

class AgentState(TypedDict):
    user_input: str
    topic: str
    action: str
    result: str