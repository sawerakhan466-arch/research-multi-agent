from crewai import Agent
from tools.web_search import web_search


def researcher():

    return Agent(
        role="Researcher",
        goal="Research the given topic and find useful information.",
        backstory="You are a research assistant who searches for information.",
        tools=[web_search()],
        verbose=True
    )
