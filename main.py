from fastapi import FastAPI

from database.database import engine
from database.models import Base

from fastapi import Depends
from sqlalchemy.orm import Session
from database.database import get_db
from database.models import Agent
from database.schemas import AgentCreate

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Yuno Backend Running"}

@app.post("/agents")
def create_agent(agent: AgentCreate, db: Session = Depends(get_db)):
    new_agent = Agent(
        name=agent.name,
        role=agent.role,
        model=agent.model
    )

    db.add(new_agent)
    db.commit()
    db.refresh(new_agent)

    return new_agent

@app.get("/agents")
def get_agents(db: Session = Depends(get_db)):
    return db.query(Agent).all()

@app.delete("/agents/{agent_id}")
def delete_agent(agent_id: int, db: Session = Depends(get_db)):
    agent = db.query(Agent).filter(Agent.id == agent_id).first()

    if not agent:
        return {"error": "Agent not found"}

    db.delete(agent)
    db.commit()

    return {"message": "Agent deleted successfully"}

@app.put("/agents/{agent_id}")
def update_agent(
    agent_id: int,
    updated: AgentCreate,
    db: Session = Depends(get_db)
):
    agent = db.query(Agent).filter(Agent.id == agent_id).first()

    if not agent:
        return {"error": "Agent not found"}

    agent.name = updated.name
    agent.role = updated.role
    agent.model = updated.model

    db.commit()
    db.refresh(agent)

    return agent