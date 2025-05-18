from pydantic import BaseModel

class AgentRequest(BaseModel):
    agent_name: str
    task: str
    user: str = "default"

class FeedbackRequest(BaseModel):
    agent_name: str
    prompt: str
    output: str
    feedback: str
