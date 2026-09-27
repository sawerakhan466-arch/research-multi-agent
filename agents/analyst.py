from crewai import Agent


def analyst():
    return Agent(
        role="Research Analyst",
        goal="Analyze the research and identify important findings and gaps.",
        backstory="You carefully analyze research and separate facts from assumptions.",
        verbose=True
    )
