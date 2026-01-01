import streamlit as st
from graphs.research_graph import app
import pandas as pd
import matplotlib.pyplot as plt
import io

# --- Streamlit page setup ---
st.set_page_config(page_title="Autonomous Agentic Researcher")
st.title("Autonomous Agentic Research Assistant")

# --- User input for research topic ---
topic = st.text_input("Research Topic", value="AI healthcare")

# --- Start button ---
if st.button("Start Research"):
    with st.spinner("Agents are researching..."):
        result = app.invoke({"user_topic": topic})
        st.success("Research Complete")

        # --- Display result ---
        st.markdown(result)

        # --- Example: Dynamic metrics for plotting ---
        # You can adjust keys to match your result dictionary structure
        # Here we attempt to parse novelty & feasibility from result text if possible
        try:
            # Dummy example: replace with actual parsing if your result is structured
            metrics = {
                "Novelty": 8,
                "Feasibility": 6,
                "Data Collected": 5,
                "Experiment Strength": 7
            }

            df = pd.DataFrame({
                "Metric": list(metrics.keys()),
                "Score": list(metrics.values())
            })

            # --- Plot ---
            fig, ax = plt.subplots()
            ax.bar(df["Metric"], df["Score"], color="skyblue")
            ax.set_ylim(0, 10)
            ax.set_ylabel("Score / Quality")
            ax.set_title("Research Metrics Overview")
            st.pyplot(fig)

        except Exception as e:
            st.warning(f"Could not generate plot: {e}")

        # --- Download research summary ---
        try:
            paper_content = f"Research Topic: {topic}\n\nResult:\n{result}"
            paper_bytes = io.BytesIO()
            paper_bytes.write(paper_content.encode("utf-8"))
            paper_bytes.seek(0)

            st.download_button(
                label="📄 Download Research Summary",
                data=paper_bytes,
                file_name=f"{topic.replace(' ', '_')}_research.txt",
                mime="text/plain"
            )
        except Exception as e:
            st.warning(f"Could not generate download button: {e}")
