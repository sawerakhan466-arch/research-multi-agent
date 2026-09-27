import os
import streamlit as st

from crewai import Crew, Task, Process, LLM

# Get Groq API key
groq_key = st.secrets["GROQ_API_KEY"]

# Create Groq LLM
groq_llm = LLM(
    model="groq/openai/gpt-oss-120b",
    api_key=groq_key,
    temperature=0.2
)

from agents.researcher import researcher
from agents.analyst import analyst
from agents.writer import writer


def run_research(topic):

    research_agent = researcher(groq_llm)
    analyst_agent = analyst(groq_llm)
    writer_agent = writer(groq_llm)

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
