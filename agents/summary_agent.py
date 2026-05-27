from agents.llm_agent import ask_ai

def summary_agent(text):
    prompt = f"""
    You are a summary AI agent.

    Summarize this clearly:

    {text}
    """

    return ask_ai(prompt)