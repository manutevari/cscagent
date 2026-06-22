"""CSC Mitra AI — Home Page"""

import streamlit as st

st.set_page_config(
    page_title="CSC Mitra AI",
    page_icon="🤝",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Header ────────────────────────────────────────────────────────────────
st.markdown(
    """
    <div style='text-align:center; padding:2rem 0 1rem'>
      <h1 style='font-size:2.8rem; color:#FF6B35;'>🤝 CSC Mitra AI</h1>
      <p style='font-size:1.2rem; color:#555;'>
        Intelligent multi-agent platform for Common Service Centre governance
      </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

# ── Feature cards ─────────────────────────────────────────────────────────
cols = st.columns(3)
cards = [
    ("🤖", "CSC Assistant", "Get instant answers on PM-KISAN, PAN, e-Shram, DigiPay, PMAY, Aadhaar and 30+ other CSC services.", "1_CSC_Assistant"),
    ("📋", "Grievance Redressal", "File a complaint, track its status, and get an AI-drafted resolution — routed automatically to the right authority.", "2_Grievance_Redressal"),
    ("📚", "Knowledge Base", "Upload PDFs, Word docs, and URLs to expand the assistant's knowledge with your own service documents.", "3_Knowledge_Base"),
    ("🏢", "VLE Dashboard", "Review assigned cases, action HITL escalations, and track SLA compliance as a Village Level Entrepreneur.", "4_VLE_Dashboard"),
    ("⚖️", "Officer Dashboard", "Approve resolutions, review escalated complaints, and manage authority assignments.", "5_Officer_Dashboard"),
    ("⚙️", "Admin Dashboard", "Monitor system health, manage knowledge ingestion, configure guardrails, and audit HITL queues.", "6_Admin_Dashboard"),
]

for i, (icon, title, desc, page) in enumerate(cards):
    with cols[i % 3]:
        st.markdown(
            f"""
            <div style='
                border:1px solid #e0e0e0; border-radius:12px;
                padding:1.4rem; margin-bottom:1rem;
                background:#fafafa;
                min-height:170px;
            '>
              <div style='font-size:2rem;'>{icon}</div>
              <h3 style='margin:0.4rem 0 0.5rem; color:#FF6B35;'>{title}</h3>
              <p style='color:#555; font-size:0.9rem; line-height:1.5;'>{desc}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.page_link(f"pages/{page}.py", label=f"Open {title} →")
        st.markdown("")

st.divider()

# ── Quick status ──────────────────────────────────────────────────────────
st.markdown("### 🔍 System Status")

c1, c2, c3 = st.columns(3)

with c1:
    try:
        from backend.guardrails import setting
        has_llm = any(
            setting(k) for k in ("OPENAI_API_KEY", "HF_TOKEN", "GROQ_API_KEY", "OPENROUTER_API_KEY")
        )
        st.success("✅ LLM configured" if has_llm else "⚠️ No LLM key — offline mode (builtin guides only)")
    except Exception as e:
        st.warning(f"⚠️ Backend: {e}")

with c2:
    try:
        from backend.guardrails import setting
        db_host = setting("DB_HOST", "")
        grv_url = setting("GRIEVANCE_DATABASE_URL", "")
        if db_host:
            st.success("✅ Knowledge DB configured")
        else:
            st.info("ℹ️ Knowledge DB: offline (builtin guides active)")

        if grv_url or True:   # SQLite fallback is always available
            st.success("✅ Grievance DB ready (SQLite fallback)")
    except Exception:
        pass

with c3:
    try:
        from backend.hitl import list_pending_reviews
        pending = list_pending_reviews(limit=100)
        n = len(pending)
        if n:
            st.warning(f"⚠️ {n} pending HITL review{'s' if n>1 else ''}")
        else:
            st.success("✅ No pending escalations")
    except Exception:
        st.info("ℹ️ HITL queue: initialising")

st.divider()
st.caption("CSC Mitra AI · Powered by LangGraph, pgvector, and multi-agent RAG · Built for Streamlit Cloud")
