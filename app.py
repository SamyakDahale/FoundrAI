import streamlit as st
import traceback
from rag_chain import ManualRAG

# ------------------------
# Helper functions
# ------------------------
def extract_action_points(answer: str):
    """Extract bullet-like actionable steps from answer."""
    lines = [line.strip() for line in answer.split(".") if line]
    actions = [
        f"✅ {line}"
        for line in lines
        if any(word in line.lower() for word in ["must", "require", "should", "need"])
    ]
    return actions

# ------------------------
# Initialize session state
# ------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "qa" not in st.session_state:
    st.session_state.qa = ManualRAG()

# ------------------------
# Page Config
# ------------------------
st.set_page_config(page_title="Founder AI", layout="wide")

# Header Section
st.title("Founder AI – Startup Compliance & Guidance Platform")
st.markdown("""
This platform helps startup founders navigate **laws, licenses, tax rules, labor regulations, data protection,** and sector-specific norms in a unified, simplified, and personalized way.
""")

# Sidebar Menu
with st.sidebar:
    st.header("Navigation")
    st.button("🏠 Home")
    st.button("🧠 Knowledge Graph")
    st.button("🎯 Personalized Guidance")
    st.button("📂 Document Tracker")
    st.button("🔔 Alerts & Updates")
    st.button("🌐 Multilingual Support")

# Main Layout
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("💬 Search Compliance Information")

    user_query = st.text_input("Enter your query (e.g., How to register GST in Maharashtra?)")

    if st.button("Search"):
        if user_query.strip():
            try:
                # Prepare chat history as context
                history_context = "\n".join(
                    [f"User: {q}\nAssistant: {a}" for q, a in st.session_state.chat_history]
                )
                prompt_with_history = f"{history_context}\nUser: {user_query}\nAssistant:"

                result = st.session_state.qa({"query": prompt_with_history})
                answer = result.get("result", "")
                sources = result.get("source_documents", [])

                # Save in chat history
                st.session_state.chat_history.append((user_query, answer))

                # Display Answer
                st.success("Answer:")
                st.write(answer)

                # Show Key Action Points
                actions = extract_action_points(answer)
                if actions:
                    st.subheader("📌 Key Action Points")
                    for act in actions:
                        st.markdown(f"- {act}")

                # Show Sources
                if sources:
                    st.subheader("📚 Sources")
                    for idx, doc in enumerate(sources, 1):
                        snippet = doc.page_content[:200].replace("\n", " ") + "..."
                        st.markdown(f"{idx}. **{doc.metadata.get('source','')}** → {snippet}")

            except Exception as e:
                st.error(f"ERROR: {e}")
                st.text(traceback.format_exc())
        else:
            st.warning("Please enter a query before searching.")

    # Chat history display
    if st.session_state.chat_history:
        st.subheader("📝 Chat History")
        for i, (q, a) in enumerate(st.session_state.chat_history, 1):
            st.markdown(f"**Q{i}:** {q}")
            st.markdown(f"**A{i}:** {a}")

    # Alerts
    st.subheader("⚡ Latest Alerts")
    st.info("⚠️ New MSME scheme launched with 0% interest loans for small businesses.")
    st.info("📜 Updated labor law for IT sector effective from next month.")

with col2:
    st.subheader("⚡ Quick Actions")
    st.button("📄 View Required Documents")
    st.button("✅ Compliance Checklist")
    st.button("🔔 Enable Alerts")
    st.button("🌐 Change Language")

# Footer
st.markdown("---")
st.markdown("**Founder AI © 2025** ")
