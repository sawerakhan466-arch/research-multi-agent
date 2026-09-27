import streamlit as st

# Fix for CrewAI + Groq cache_breakpoint error
try:
    import crewai.llms.cache as crew_cache
    crew_cache.mark_cache_breakpoint = lambda msg: msg
except Exception:
    pass

from crewai import Crew, Task, Process, LLM

from agents.researcher import researcher
from agents.analyst import analyst
from agents.writer import writer


def run_research(topic):

    # Groq LLM
    groq_llm = LLM(
        model="groq/openai/gpt-oss-120b",
        api_key=st.secrets["GROQ_API_KEY"],
        temperature=0.2
    )

    # Create agents
    research_agent = researcher(groq_llm)
    analyst_agent = analyst(groq_llm)
    writer_agent = writer(groq_llm)

    # -------------------------
    # Research Task
    # -------------------------
    research_task = Task(
        description=f"""
        Research the following topic:

        {topic}

        Provide useful facts, explanations,
        examples, important points and relevant
        background information.
        """,
        expected_output="""
        A detailed research summary about the topic.
        """,
        agent=research_agent
    )

    # -------------------------
    # Analysis Task
    # -------------------------
    analysis_task = Task(
        description="""
        Carefully analyze the research produced
        by the researcher.

        Identify:
        - Important findings
        - Key ideas
        - Patterns
        - Comparisons
        - Research gaps
        - Important implications
        """,
        expected_output="""
        A clear and organized analysis of the research.
        """,
        agent=analyst_agent,
        context=[research_task]
    )

    # -------------------------
    # Writing Task
    # -------------------------
    writing_task = Task(
        description=f"""
        Write a clear and well-organized research
        report about:

        {topic}

        Use the research and analysis provided by
        the previous agents.

        Structure the report as:

        # Research Report

        ## Introduction

        ## Key Findings

        ## Analysis

        ## Research Gaps

        ## Limitations

        ## Conclusion
        """,
        expected_output="""
        A complete and well-structured research report.
        """,
        agent=writer_agent,
        context=[research_task, analysis_task]
    )

    # -------------------------
    # Crew
    # -------------------------
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

    # Run the crew
    result = crew.kickoff()

    return result
