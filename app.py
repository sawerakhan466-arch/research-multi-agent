import streamlit as st
from crew import run_research


st.set_page_config(
    page_title="Research AI",
    page_icon="🔬",
    layout="wide"
)


st.markdown("""
<style>

/* Main background */
.stApp {
    background: linear-gradient(
        135deg,
        #16001f 0%,
        #3b073f 45%,
        #8e165f 100%
    );
    color: white;
}


/* Main title */
.title {
    text-align: center;
    font-size: 48px;
    font-weight: 800;
    margin-top: 30px;
    color: #ffffff;
}


/* Subtitle */
.subtitle {
    text-align: center;
    color: #f5c6e5;
    font-size: 18px;
    margin-bottom: 40px;
}


/* Agent cards */
.agent {
    background: rgba(255, 255, 255, 0.10);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    border: 1px solid rgba(255, 255, 255, 0.20);
    color: white;
}


/* Research topic label */
.stTextArea label {
    color: white !important;
    font-weight: 600 !important;
}


/* Research topic box */
.stTextArea textarea {
    color: #111111 !important;
    background-color: #ffffff !important;
    border-radius: 12px !important;
    border: 2px solid #e85aad !important;
    font-size: 16px !important;
}


/* Placeholder text */
.stTextArea textarea::placeholder {
    color: #777777 !important;
    opacity: 1 !important;
}


/* Start button */
.stButton > button {
    background: linear-gradient(
        90deg,
        #ff2fa3,
        #c026d3
    ) !important;

    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    font-size: 17px !important;
    font-weight: 700 !important;
    padding: 12px !important;
}


/* Button hover */
.stButton > button:hover {
    background: linear-gradient(
        90deg,
        #ff4db3,
        #d946ef
    ) !important;
    color: white !important;
}


/* Status box */
.stStatus {
    background: rgba(255, 255, 255, 0.08) !important;
    border-radius: 12px !important;
}


/* Report heading */
.stSubheader {
    color: white !important;
}


/* Download button */
.stDownloadButton > button {
    background: #ffffff !important;
    color: #8e165f !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
}

</style>
""", unsafe_allow_html=True)


# Header
st.markdown(
    '<div class="title">🔬 Research AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Multi-Agent Research Assistant powered by CrewAI + Groq</div>',
    unsafe_allow_html=True
)


# Agent cards
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="agent">
        🔎<br><br>
        <b>Researcher</b><br>
        Searches the web
    </div>
    """, unsafe_allow_html=True)


with col2:
    st.markdown("""
    <div class="agent">
        🧠<br><br>
        <b>Analyst</b><br>
        Analyzes findings
    </div>
    """, unsafe_allow_html=True)


with col3:
    st.markdown("""
    <div class="agent">
        ✍️<br><br>
        <b>Writer</b><br>
        Creates report
    </div>
    """, unsafe_allow_html=True)


st.write("")


# Research topic
topic = st.text_area(
    "Enter your research topic",
    placeholder="Example: Impact of Artificial Intelligence on Education",
    height=120
)


# Start research
if st.button("🚀 Start Research", use_container_width=True):

    if not topic.strip():

        st.warning("Please enter a research topic.")

    else:

        with st.status(
            "🤖 Research team is working...",
            expanded=True
        ):

            st.write("🔎 Researcher is searching the web...")

            st.write("🧠 Analyst is analyzing the information...")

            st.write("✍️ Writer is preparing the final report...")

            try:

                result = run_research(topic)

                st.session_state["result"] = str(result)

                st.write("✅ Research completed!")

            except Exception as e:

                st.error(f"Something went wrong: {e}")


# Final report
if "result" in st.session_state:

    st.divider()

    st.subheader("📄 Final Research Report")

    st.markdown(st.session_state["result"])

    st.download_button(
        "⬇️ Download Report",
        st.session_state["result"],
        file_name="research_report.md",
        mime="text/markdown"
    )
