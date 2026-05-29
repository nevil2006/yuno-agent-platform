from pydantic import BaseModel
from typing import Optional


class AgentCreate(BaseModel):

    name: str

    role: str

    model: str

    system_prompt: Optional[str] = None

    tools: Optional[str] = None

    memory: Optional[str] = None

    schedule: Optional[str] = None

    guardrails: Optional[str] = None

    channel: Optional[str] = None