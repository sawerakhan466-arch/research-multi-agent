import os
import streamlit as st

# Use Groq with CrewAI
os.environ["OPENAI_API_KEY"] = st.secrets["GROQ_API_KEY"]
os.environ["OPENAI_BASE_URL"] = "https://api.groq.com/openai/v1"

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
        Research the following topic:

        {topic}

        Provide important facts, explanations,
        examples and relevant information.
        """,
        expected_output="A detailed research summary.",
        agent=research_agent
    )

    analysis_task = Task(
        description="""
        Analyze the research provided by the researcher.

        Identify the important findings,
        patterns, comparisons and gaps.
        """,
        expected_output="A clear analysis of the research.",
        agent=analyst_agent,
        context=[research_task]
    )

    writing_task = Task(
        description=f"""
        Write a clear research report about:

        {topic}

        Include:

        # Research Report

        ## Introduction

        ## Key Findings

        ## Analysis

        ## Research Gaps

        ## Limitations

        ## Conclusion
        """,
        expected_output="A complete research report.",
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
