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
        goal="Research user topic",
        backstory="Expert researcher",
        verbose=True,
        llm=groq_llm
    )

    summary_agent = Agent(
        role="Summary Agent",
        goal="Summarize information",
        backstory="Expert summarizer",
        verbose=True,
        llm=groq_llm
    )

    research_task = Task(
        description=f"Research this topic: {query}",
        expected_output="Detailed research on topic",
        agent=research_agent
    )

    summary_task = Task(
        description="Summarize the research",
        expected_output="Clear short summary",
        agent=summary_agent
    )

    crew = Crew(
        agents=[research_agent, summary_agent],
        tasks=[research_task, summary_task],
        verbose=True
    )

    result = crew.kickoff()
    return str(result)