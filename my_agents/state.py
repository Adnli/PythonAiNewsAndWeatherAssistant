from dataclasses import dataclass, field
from typing import List, Dict, Any

@dataclass
class ChatState:
    messages: List[Dict[str, str]] = field(default_factory=list)

    def add_user(self, text: str) -> None:
        self.messages.append({"role": "user", "content": text})

    def add_assistant(self, text: str) -> None:
        self.messages.append({"role": "assistant", "content": text})
