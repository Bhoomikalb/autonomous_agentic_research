import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
import os
from graphs.research_graph import app  # Your agent wrapper

# -------------------------
# Page configuration
# -------------------------
st.set_page_config(
    page_title="Autonomous Agentic Researcher",
    layout="wide"
)

st.title("Autonomous Agentic Research Assistant")

# -------------------------
# Load API keys from environment
# -------------------------
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.warning("GROQ_API_KEY is not set.")
    st.stop()
# -------------------------
# Sidebar controls
# -------------------------
st.sidebar.header("Controls")
chart_type = st.sidebar.selectbox(
    "Select chart type",
    ["Bar Chart", "Line Chart"]
)

# -------------------------
# User input
# -------------------------
topic = st.text_input(
    "Research Topic",
    placeholder="Ask anything… e.g. AI in healthcare"
)

# -------------------------
# Session state
# -------------------------
if "result" not in st.session_state:
    st.session_state.result = None

# -------------------------
# Start button
# -------------------------
if st.button("Start Research") and topic:
    with st.spinner("Agents are researching..."):
        try:
            # Invoke your AI agent
            st.session_state.result = app.invoke({"user_topic": topic})
            st.success("Research Complete")
        except Exception as e:
            st.error(f"Error during research: {e}")

# -------------------------
# Display results
# -------------------------
if st.session_state.result:
    result = st.session_state.result

    # Expandable research output
    with st.expander("Full Research Output", expanded=True):
        st.markdown(result)

    # -------------------------
    # Metrics sliders
    # -------------------------
    st.subheader("📊 Research Quality Metrics")

    col1, col2, col3, col4 = st.columns(4)
    with col1: novelty = st.slider("Novelty", 0, 10, 8)
    with col2: feasibility = st.slider("Feasibility", 0, 10, 6)
    with col3: data_quality = st.slider("Data Quality", 0, 10, 5)
    with col4: experiment_strength = st.slider("Experiment Strength", 0, 10, 7)

    metrics = {
        "Novelty": novelty,
        "Feasibility": feasibility,
        "Data Quality": data_quality,
        "Experiment Strength": experiment_strength
    }

    df = pd.DataFrame({
        "Metric": metrics.keys(),
        "Score": metrics.values()
    })

    # -------------------------
    # Plot chart
    # -------------------------
    fig, ax = plt.subplots()
    if chart_type == "Bar Chart":
        ax.bar(df["Metric"], df["Score"], color="skyblue")
    else:
        ax.plot(df["Metric"], df["Score"], marker="o", linestyle="-", color="green")

    ax.set_ylim(0, 10)
    ax.set_ylabel("Score")
    ax.set_title("Research Evaluation Metrics")

    st.pyplot(fig)

    # -------------------------
    # Download options
    # -------------------------
    st.subheader("Download Outputs")
    colA, colB = st.columns(2)

    with colA:
        paper_content = f"""
Research Topic: {topic}

=====================
AUTONOMOUS AI OUTPUT
=====================

{result}
"""
        paper_bytes = io.BytesIO()
        paper_bytes.write(paper_content.encode("utf-8"))
        paper_bytes.seek(0)

        st.download_button(
            label="📄 Download Research Summary (TXT)",
            data=paper_bytes,
            file_name=f"{topic.replace(' ', '_')}_research.txt",
            mime="text/plain"
        )

    with colB:
        csv_bytes = io.BytesIO()
        df.to_csv(csv_bytes, index=False)
        csv_bytes.seek(0)

        st.download_button(
            label="📊 Download Metrics (CSV)",
            data=csv_bytes,
            file_name=f"{topic.replace(' ', '_')}_metrics.csv",
            mime="text/csv"
        )

    # -------------------------
    # Interaction tip
    # -------------------------
    st.info(
        "Tip: Adjust the sliders to explore how research quality changes. "
        "Plots update instantly without re-running the agents."
    )
