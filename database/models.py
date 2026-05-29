from sqlalchemy import Column, Integer, String, Text, DateTime
from database.database import Base
from datetime import datetime


class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    role = Column(String, nullable=False)

    model = Column(String, nullable=False)

    system_prompt = Column(Text)

    tools = Column(String)

    memory = Column(String)

    schedule = Column(String)

    guardrails = Column(String)

    channel = Column(String)


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)

    query = Column(Text)

    research = Column(Text)

    summary = Column(Text)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )