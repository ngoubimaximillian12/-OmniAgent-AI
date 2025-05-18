from agents.code_agent import CodeAgent
from agents.legal_agent import LegalAgent
from agents.data_agent import DataAgent
from agents.finance_agent import FinanceAgent
from agents.cyber_agent import CyberAgent
from agents.teach_agent import TeachAgent
from agents.memory_agent import MemoryAgent
from agents.vision_agent import VisionAgent

# Registry for all active agents in the system
AGENTS = {
    "CodeAgent": CodeAgent(),
    "LegalAgent": LegalAgent(),
    "DataAgent": DataAgent(),
    "FinanceAgent": FinanceAgent(),
    "CyberAgent": CyberAgent(),
    "TeachAgent": TeachAgent(),
    "MemoryAgent": MemoryAgent(),
    "VisionAgent": VisionAgent()
}
