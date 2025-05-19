# Import all agent classes from the agents package
from omniagent.agents.code_agent import CodeAgent
from omniagent.agents.legal_agent import LegalAgent
from omniagent.agents.data_agent import DataAgent
from omniagent.agents.finance_agent import FinanceAgent
from omniagent.agents.cyber_agent import CyberAgent
from omniagent.agents.vision_agent import VisionAgent
from omniagent.agents.teach_agent import TeachAgent
from omniagent.agents.memory_agent import MemoryAgent

# Create a dictionary mapping agent names to their instances
AGENTS = {
    "code": CodeAgent(),
    "legal": LegalAgent(),
    "data": DataAgent(),
    "finance": FinanceAgent(),
    "cyber": CyberAgent(),
    "vision": VisionAgent(),
    "teach": TeachAgent(),
    "memory": MemoryAgent(),
}