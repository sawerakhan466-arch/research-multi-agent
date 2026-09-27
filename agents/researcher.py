from crewai import Agent


def researcher():
    return Agent(
        role="Researcher",
        goal="Research the given topic and collect useful information.",
        backstory="You are a research assistant who provides accurate and relevant information.",
        verbose=True
    )
