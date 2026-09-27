import os
import streamlit as st

os.environ["OPENAI_API_KEY"] = st.secrets["GROQ_API_KEY"]
os.environ["OPENAI_BASE_URL"] = "https://api.groq.com/openai/v1"

from crewai import Crew, Task, Process

from agents.researcher import researcher
from agents.analyst import analyst
from agents.writer import writer
