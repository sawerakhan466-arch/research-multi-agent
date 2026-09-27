from crewai import Agent


def writer(llm):

    return Agent(
        role="Research Writer",
        goal="Write a clear and organized research report.",
        backstory="You are a research writer who creates clear and organized reports.",
        llm=llm,
        verbose=True
    )
