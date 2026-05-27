from agents.llm_agent import ask_ai

def research_agent(query):
    prompt = f"""
    You are a research AI agent.

    Give detailed research about:
    {query}
    """

    return ask_ai(prompt)