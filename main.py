import streamlit as st
import time
import random

    # --- REVISED VIBE SETTINGS ---
st.set_page_config(page_title="MVP1: Diagnostic Agent", page_icon="🚗", layout="centered")

# --- STYLING ---
st.markdown("""
<style>
    /* Main app background - light cream color for readability */
    .stApp {
        background-color: #FAFAFA;
    }
    
    /* Ensure all text is dark and readable */
    .stApp, .stApp p, .stApp span, .stApp div {
        color: #1E1E1E !important;
    }
    
    /* Chat messages with good contrast */
    .stChatMessage {
        background-color: #FFFFFF;
        border-radius: 10px;
        padding: 10px;
        border: 1px solid #E0E0E0;
    }
    
    /* Title and headers */
    h1, h2, h3, .stTitle {
        color: #1E1E1E !important;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #F0F2F6;
    }
    
    /* Button styling */
    .stButton button {
        background-color: #4A90E2; 
        color: white !important;
        border-radius: 20px;
    }
    
    /* Caption text */
    .stCaption {
        color: #555555 !important;
    }
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- MAIN INTERFACE ---
st.title("💸 Claims Triage & Cost Estimation Agent")
st.caption("Input claim details (e.g., Claim ID C2025-481 or 'Customer states vehicle hit a deer').")

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- THE AGENTIC LOGIC (VIBE CODED) ---
def simulate_agent_thinking(prompt):
    """
    Simulates the specific diagnostic loop: Listen -> Check -> Diagnose -> Recommend.
    """

    # 1. LISTENING & ANALYSIS PHASE
    with st.status("👂 **Analyzing Symptoms...**", expanded=True) as status:
        time.sleep(1)
        st.write(f"Processing symptom description: '{prompt}'")
        time.sleep(1.2)
        st.write("Cross-referencing common fault codes and known issues...")
        time.sleep(0.8)
        status.update(label="✅ Initial Analysis Complete", state="complete", expanded=False)

    # 2. DIAGNOSTIC EXECUTION PHASE (The "Action")
    with st.status("🔬 **Running Virtual Diagnostics...**", expanded=True) as status:
        st.write("🔍 Searching database for probability scores...")
        time.sleep(1.5)
        st.write("⚙️ Synthesizing potential causes based on make/model...")
        time.sleep(1)
        st.write("⚠️ Checking severity index...")
        time.sleep(1)
        status.update(label="✅ Diagnosis Complete", state="complete", expanded=False)

    # Structured B2B Triage Output
    return (
        f"Triage complete for the input: **'{prompt}'**. My assessment protocol suggests:\n\n"
        "### 💸 Risk & Allocation Triage\n"
        "1. **Adjuster Action:** *Flagged as Medium Priority.* Requires human review of photos.\n"
        "2. **Estimated Severity:** *Total Repair Cost Range: $3,200 - $4,500* (due to potential frame damage).\n"
        "3. **Recommended Allocation:** *Auto-assign to Tier 2 Certified Body Shop* (Avoid independent shops due to high cost volatility).\n\n"
        "### 📝 Key Data Extracted\n"
        "* **Date of Loss:** [Simulated] 2025-11-20\n"
        "* **Estimated TTO (Time to Out-of-service):** 10-14 days"
    )

# --- USER INPUT ---
# The prompt is now highly specific to the automotive context
if prompt := st.chat_input("Enter Claim ID or copy/paste key claim notes for triage..."):
    # 1. Display User Message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Trigger Agent
    with st.chat_message("assistant"):
        response_text = simulate_agent_thinking(prompt)
        st.markdown(response_text)

    # 3. Save Assistant Message
    st.session_state.messages.append({"role": "assistant", "content": response_text})
