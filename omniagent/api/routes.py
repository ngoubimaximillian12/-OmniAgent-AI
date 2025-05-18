from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from agent_registry import AGENTS
from memory.memory_utils import retrieve_similar_prompts, log_and_embed
from learning.feedback_loop import log_feedback

router = APIRouter()


class AgentRequest(BaseModel):
    agent_name: str
    task: str
    user: str = "default"


class FeedbackRequest(BaseModel):
    agent_name: str
    prompt: str
    output: str
    feedback: str


@router.post("/run-agent")
def run_agent(req: AgentRequest):
    agent = AGENTS.get(req.agent_name)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")

    memory = retrieve_similar_prompts(req.task)
    result = agent.run(req.task, context=None, memory=memory)
    log_and_embed(agent.name, req.task, result)
    return {"result": result}


@router.get("/memory")
def get_memory(task: str):
    memory = retrieve_similar_prompts(task)
    return {"matches": memory}


@router.post("/feedback")
def submit_feedback(req: FeedbackRequest):
    log_feedback(req.agent_name, req.prompt, req.output, req.feedback)
    return {"status": "feedback logged"}
