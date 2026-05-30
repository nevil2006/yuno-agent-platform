from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv
import os

load_dotenv()

groq_llm = LLM(
    model="groq/llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)


def run_crew(query):

    research_agent = Agent(
        role="Research Agent",
        goal="Research user topic briefly",
        backstory="Expert researcher",
        verbose=True,
        llm=groq_llm,
        allow_delegation=True
    )

    summary_agent = Agent(
        role="Summary Agent",
        goal="Create short summary",
        backstory="Expert summarizer",
        verbose=True,
        llm=groq_llm
    )

    research_task = Task(
        description=f"Research briefly: {query}",
        expected_output="Short research under 100 words",
        agent=research_agent
    )

    summary_task = Task(
        description="Summarize briefly",
        expected_output="Short concise summary under 50 words",
        agent=summary_agent
    )

    crew = Crew(
        agents=[
            research_agent,
            summary_agent
        ],
        tasks=[
            research_task,
            summary_task
        ],
        verbose=True
    )

    result = crew.kickoff()

    return str(result)