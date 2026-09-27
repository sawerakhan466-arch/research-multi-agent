from crewai import Agent
from tools.web_search import web_search


def researcher():
    return Agent(
        role="Researcher",
        goal="Find useful and reliable information about the given topic.",
        backstory="You are a web researcher who collects facts and sources.",
        tools=[web_search()],
        verbose=True
    )
