import streamlit as st
from graphs.research_graph import app
import pandas as pd
import matplotlib.pyplot as plt
import io

# --- Streamlit page setup ---
st.set_page_config(
    page_title="Autonomous Agentic Researcher",
    layout="wide"
)
st.title("Autonomous Agentic Research Assistant")

# --- Sidebar controls ---
st.sidebar.header("Controls")
chart_type = st.sidebar.selectbox(
    "Select chart type",
    ["Bar Chart", "Line Chart"]
)

# --- User input for research topic ---
topic = st.text_input(
    "Research Topic",
    placeholder="Ask anything… e.g. AI in healthcare"
)

# --- Session state (important for interactivity) ---
if "result" not in st.session_state:
    st.session_state.result = None

# --- Start button ---
if st.button("Start Research"):
    with st.spinner("Agents are researching..."):
        st.session_state.result = app.invoke({"user_topic": topic})
        st.success("Research Complete")

# --- Display results only if available ---
if st.session_state.result:

    result = st.session_state.result

    # --- Expandable sections ---
    with st.expander("Full Research Output", expanded=True):
        st.markdown(result)

    # =========================
    # 📊 INTERACTIVE METRICS
    # =========================
    st.subheader("📊 Research Quality Metrics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        novelty = st.slider("Novelty", 0, 10, 8)
    with col2:
        feasibility = st.slider("Feasibility", 0, 10, 6)
    with col3:
        data_quality = st.slider("Data Quality", 0, 10, 5)
    with col4:
        experiment_strength = st.slider("Experiment Strength", 0, 10, 7)

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

    # --- Plot ---
    fig, ax = plt.subplots()

    if chart_type == "Bar Chart":
        ax.bar(df["Metric"], df["Score"])
    else:
        ax.plot(df["Metric"], df["Score"], marker="o")

    ax.set_ylim(0, 10)
    ax.set_ylabel("Score")
    ax.set_title("Research Evaluation Metrics")

    st.pyplot(fig)

    # =========================
    # DOWNLOAD OPTIONS
    # =========================
    st.subheader("Download Outputs")

    colA, colB = st.columns(2)

    # --- Download research summary ---
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

    # --- Download metrics ---
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

    # =========================
    # 🧠 INTERACTION TIP
    # =========================
    st.info(
        "Tip: Adjust the sliders to explore how research quality changes. "
        "Plots update instantly without re-running the agents."
    )
