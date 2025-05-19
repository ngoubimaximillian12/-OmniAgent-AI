from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from omniagent.agent_registry import AGENTS
from omniagent.memory.memory_utils import retrieve_similar_prompts, log_and_embed
from omniagent.learning.feedback_loop import log_feedback
from omniagent.llm.llm_provider import LLMProvider

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

    try:
        memory = retrieve_similar_prompts(req.task)
        result = agent.run(req.task, context=None, memory=memory)
        log_and_embed(agent=agent.name, prompt=req.task, output=result)
        return {"result": result}
    except Exception as e:
        # Fallback to DeepSeek local LLM
        try:
            llm = LLMProvider.get_llm()
            fallback_result = llm.run(req.task)
            log_and_embed("DeepSeekFallback", req.task, fallback_result)
            return {
                "result": fallback_result,
                "warning": f"Primary agent failed, used DeepSeek fallback. Error: {str(e)}"
            }
        except Exception as fallback_error:
            raise HTTPException(
                status_code=500,
                detail=f"Both primary agent and fallback DeepSeek failed: {fallback_error}"
            )

@router.get("/memory")
def get_memory(task: str):
    memory = retrieve_similar_prompts(task)
    return {"matches": memory}

@router.post("/feedback")
def submit_feedback(req: FeedbackRequest):
    log_feedback(req.agent_name, req.prompt, req.output, req.feedback)
    return {"status": "feedback logged"}
