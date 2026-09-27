from crewai import Agent


def researcher(llm):

    return Agent(
        role="Researcher",
        goal="Research the given topic and collect useful information.",
        backstory="You are a research assistant who provides accurate and relevant information.",
        llm=llm,
        verbose=True
    )
