from abc import ABC, abstractmethod
from typing import Any, Dict


class ILLMProvider(ABC):
    """
    The Strategy Interface.
    Every LLM provider must implement this.
    """

    @abstractmethod
    async def generate_response(self, prompt: str) -> Dict[str, Any]:
        """
        Sends prompt to LLM and returns a dictionary (parsed JSON).
        """
        pass
