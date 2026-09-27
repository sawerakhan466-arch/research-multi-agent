import streamlit as st
from crew import run_research


st.set_page_config(
    page_title="Research AI",
    page_icon="🔬",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0f0f1f, #1b1028);
    color: white;
}

.title {
    text-align: center;
    font-size: 48px;
    font-weight: 800;
    margin-top: 30px;
}

.subtitle {
    text-align: center;
    color: #c8b8d9;
    font-size: 18px;
    margin-bottom: 40px;
}

.agent {
    background: rgba(255,255,255,0.06);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.1);
}

</style>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="title">🔬 Research AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Multi-Agent Research Assistant powered by CrewAI + Groq</div>',
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="agent">
    🔎<br>
    <b>Researcher</b><br>
    Searches the web
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="agent">
    🧠<br>
    <b>Analyst</b><br>
    Analyzes findings
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="agent">
    ✍️<br>
    <b>Writer</b><br>
    Creates report
    </div>
    """, unsafe_allow_html=True)


st.write("")

topic = st.text_area(
    "Enter your research topic",
    placeholder="Example: Impact of Artificial Intelligence on Education",
    height=120
)


if st.button("🚀 Start Research", use_container_width=True):

    if not topic.strip():
        st.warning("Please enter a research topic.")
    else:

        with st.status("🤖 Research team is working...", expanded=True):

            st.write("🔎 Researcher is searching the web...")
            
            st.write("🧠 Analyst is analyzing the information...")

            st.write("✍️ Writer is preparing the final report...")

            try:
                result = run_research(topic)

                st.session_state["result"] = str(result)

                st.write("✅ Research completed!")

            except Exception as e:
                st.error(f"Something went wrong: {e}")


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
