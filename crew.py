from crewai import Crew, Task, Process

from agents.researcher import researcher
from agents.analyst import analyst
from agents.writer import writer


def run_research(topic):

    research_agent = researcher()
    analyst_agent = analyst()
    writer_agent = writer()

    research_task = Task(
        description=f"""
        Research this topic:

        {topic}

        Find:
        - important facts
        - recent information
        - useful statistics
        - reliable sources
        - source URLs

        Use the web search tool.
        Do not make up information.
        """,
        expected_output="A research summary with important facts and sources.",
        agent=research_agent
    )

    analysis_task = Task(
        description="""
        Analyze the research provided by the researcher.

        Identify:
        - important findings
        - patterns
        - useful comparisons
        - research gaps
        - limitations

        Do not invent information.
        """,
        expected_output="A clear analysis of the research findings.",
        agent=analyst_agent,
        context=[research_task]
    )

    writing_task = Task(
        description=f"""
        Write a final research report about:

        {topic}

        Use the research and analysis from the previous agents.

        Include:

        # Research Report

        ## Introduction
        ## Key Findings
        ## Analysis
        ## Research Gaps
        ## Limitations
        ## Conclusion
        ## Sources

        Keep the report clear and evidence-based.
        Do not invent sources.
        """,
        expected_output="A complete research report with sources.",
        agent=writer_agent,
        context=[research_task, analysis_task]
    )

    crew = Crew(
        agents=[
            research_agent,
            analyst_agent,
            writer_agent
        ],
        tasks=[
            research_task,
            analysis_task,
            writing_task
        ],
        process=Process.sequential,
        verbose=True
    )

    return crew.kickoff()
