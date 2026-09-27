from crewai import Agent


def writer():
    return Agent(
        role="Research Writer",
        goal="Write a clear final research report using the collected information.",
        backstory="You are a research writer who creates simple, organized reports.",
        verbose=True
    )
