from crewai import Agent


def analyst(llm):

    return Agent(
        role="Research Analyst",
        goal="Analyze the research and identify important findings.",
        backstory="You carefully analyze research and identify useful patterns and gaps.",
        llm=llm,
        verbose=True
    )
