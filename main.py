from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database.database import engine, get_db
from database.models import Base, Agent, Message
from database.schemas import AgentCreate

from agents.llm_agent import ask_ai
from agents.research_agent import research_agent
from agents.summary_agent import summary_agent
from runtime.crew_runtime import run_crew


# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI()


# -------------------------
# HOME
# -------------------------

@app.get("/")
def home():
    return {"message": "Yuno Backend Running"}


# -------------------------
# AGENT CRUD
# -------------------------

# Create Agent
@app.post("/agents")
def create_agent(
    agent: AgentCreate,
    db: Session = Depends(get_db)
):
    new_agent = Agent(
        name=agent.name,
        role=agent.role,
        model=agent.model,
        system_prompt=agent.system_prompt,
        tools=agent.tools,
        memory=agent.memory,
        schedule=agent.schedule,
        guardrails=agent.guardrails,
        channel=agent.channel
    )

    db.add(new_agent)
    db.commit()
    db.refresh(new_agent)

    return new_agent


# Get Agents
@app.get("/agents")
def get_agents(
    db: Session = Depends(get_db)
):
    return db.query(Agent).all()


# Delete Agent
@app.delete("/agents/{agent_id}")
def delete_agent(
    agent_id: int,
    db: Session = Depends(get_db)
):
    agent = db.query(Agent).filter(
        Agent.id == agent_id
    ).first()

    if not agent:
        return {"error": "Agent not found"}

    db.delete(agent)
    db.commit()

    return {
        "message": "Agent deleted successfully"
    }


# Update Agent
@app.put("/agents/{agent_id}")
def update_agent(
    agent_id: int,
    updated: AgentCreate,
    db: Session = Depends(get_db)
):
    agent = db.query(Agent).filter(
        Agent.id == agent_id
    ).first()

    if not agent:
        return {"error": "Agent not found"}

    agent.name = updated.name
    agent.role = updated.role
    agent.model = updated.model
    agent.system_prompt = updated.system_prompt
    agent.tools = updated.tools
    agent.memory = updated.memory
    agent.schedule = updated.schedule
    agent.guardrails = updated.guardrails
    agent.channel = updated.channel

    db.commit()
    db.refresh(agent)

    return agent


# -------------------------
# SINGLE AI AGENT
# -------------------------

@app.post("/ask")
def ask_agent(prompt: str):

    answer = ask_ai(prompt)

    return {
        "prompt": prompt,
        "response": answer
    }


# -------------------------
# MULTI AGENT + SAVE HISTORY
# -------------------------

@app.post("/multi-agent")
def multi_agent(
    query: str,
    db: Session = Depends(get_db)
):

    research = research_agent(query)

    summary = summary_agent(research)

    message = Message(
        query=query,
        research=research,
        summary=summary
    )

    db.add(message)
    db.commit()

    return {
        "query": query,
        "research": research,
        "summary": summary
    }


# -------------------------
# CREW AI ROUTE
# -------------------------

@app.post("/crew")
def crew_route(query: str):

    result = run_crew(query)

    return {
        "query": query,
        "crew_result": result
    }


# -------------------------
# MESSAGE HISTORY
# -------------------------

@app.get("/messages")
def get_messages(
    db: Session = Depends(get_db)
):
    return db.query(Message).all()