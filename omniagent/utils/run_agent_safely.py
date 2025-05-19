import requests
from omniagent.agent_registry import AGENTS
from omniagent.llm.llm_provider import LLMProvider

API_URL = "http://localhost:8000/run-agent"

def run_agent_safely(agent_name, task, user="default"):
    try:
        # Try backend call first
        response = requests.post(API_URL, json={
            "agent_name": agent_name,
            "task": task,
            "user": user
        }, timeout=5)
        if response.status_code == 200:
            result = response.json().get("result")
            print(f"✅ Backend result for {agent_name}: {result}")
            return result or "No result from backend."
        else:
            print(f"⚠️ Backend returned status {response.status_code}, falling back to local agent.")
            raise Exception("Backend failure")
    except Exception as e:
        print(f"⚠️ Backend call failed ({e}), falling back to local DeepSeek LLM.")

        # Attempt to instantiate local LLM
        try:
            llm = LLMProvider.get_llm()
            print("✅ Successfully instantiated local DeepSeek LLM.")
        except Exception as inst_err:
            print(f"❌ Failed to instantiate local DeepSeek LLM: {inst_err}")
            return f"❌ Cannot instantiate local LLM: {inst_err}"

        # Run the task with local LLM directly
        try:
            # Option 1: Run with the requested agent if it exists
            agent = AGENTS.get(agent_name)
            if agent:
                print(f"✅ Found agent '{agent_name}', running locally.")
                # We run the agent's run method which should use llm internally
                result = agent.run(task)
                print(f"✅ Local agent run result: {result}")
                return result
            else:
                # Option 2: If no agent, run llm.run directly for raw answer
                print(f"⚠️ Agent '{agent_name}' not found, running raw LLM fallback.")
                llm_result = llm.run(task)
                print(f"✅ Raw LLM fallback result: {llm_result}")
                return llm_result
        except Exception as run_err:
            print(f"❌ Local agent/LLM run failed: {run_err}")
            return f"❌ Local fallback failed: {run_err}"
