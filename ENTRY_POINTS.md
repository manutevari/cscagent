# Repository Entry Points

## ⚡ Quick Reference

### For Streamlit Cloud Deployment

| Use Case | Entry Point | Status |
|----------|------------|--------|
| **New App (Recommended)** | `app.py` | ✅ Modern |
| **Legacy Compatibility** | `streamlit_app.py` | ⚠️ Updated |

---

## 🆕 Modern Entry Point: `app.py`

**Recommended for:** Streamlit Cloud deployment, new projects

### Features
- ✅ Clean multi-page architecture
- ✅ 6 professional dashboards
- ✅ Modern UI with consistent styling
- ✅ Streamlit Cloud optimized
- ✅ No legacy code baggage

### How to Use
```bash
# Local testing
streamlit run app.py

# Streamlit Cloud
# Set App URL to: app.py
```

### Structure
```
app.py (Home)
└── pages/
    ├── 1_CSC_Assistant.py
    ├── 2_Grievance_Redressal.py
    ├── 3_Knowledge_Base.py
    ├── 4_VLE_Dashboard.py
    ├── 5_Officer_Dashboard.py
    └── 6_Admin_Dashboard.py
```

---

## 🔧 Legacy Entry Point: `streamlit_app.py`

**Recommended for:** Existing codebases, backward compatibility

### Features
- ✅ Uses legacy backend modules
- ✅ Voice features support
- ✅ Original UI structure
- ✅ **Fixed import issues** (v2.0)

### What Was Fixed
```python
# ✅ NOW INCLUDES PROPER PATH HANDLING:
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# ✅ ERROR HANDLING FOR MISSING MODULES:
try:
    from backend.knowledge import ingest_knowledge_source
except ImportError as e:
    st.warning(f"⚠️ Could not load module: {e}")
    ingest_knowledge_source = None
```

### How to Use
```bash
# Local testing
streamlit run streamlit_app.py

# Streamlit Cloud
# Set App URL to: streamlit_app.py
```

---

## 📦 Backend Package Structure

All of these are now proper Python packages (contain `__init__.py`):

```
backend/
├── __init__.py              ✅ Makes backend importable
├── agents/
│   ├── __init__.py          ✅ Exports all agents
│   ├── intent_agent.py
│   ├── service_discovery_agent.py
│   ├── eligibility_agent.py
│   ├── document_verification_agent.py
│   ├── compliance_agent.py
│   ├── workflow_guidance_agent.py
│   ├── grievance_agent.py
│   └── fusion_agent.py
├── services/
│   ├── __init__.py          ✅ Package marker
│   ├── ingestion.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── retrieval.py
│   ├── reranker.py
│   └── ...
├── workflows/
│   ├── __init__.py          ✅ Package marker
│   ├── ticket_engine.py
│   ├── sla_engine.py
│   └── ...
├── models/
│   ├── __init__.py          ✅ Package marker
│   └── ...
├── graph/
│   ├── __init__.py          ✅ Package marker
│   └── ...
├── db/
│   ├── __init__.py          ✅ Package marker
│   ├── postgres.py
│   └── schema.sql
│
├── knowledge.py             ✅ Importable module
├── document_extractors.py   ✅ Importable module
├── hitl.py                  ✅ Importable module
├── mas_engine.py            ✅ Importable module
├── guardrails.py            ✅ Importable module
├── voice_assistant.py       ✅ Importable module
└── ...
```

---

## ✅ Verified Imports

All imports from both entry points now work:

```python
# ✅ These all work now:
from backend.knowledge import ingest_knowledge_source
from backend.document_extractors import SUPPORTED_FILE_TYPES
from backend.hitl import list_pending_reviews, resolve_review
from backend.mas_engine import ask
from backend.guardrails import setting as guardrail_setting
from backend.voice_assistant import (
    normalize_voice_language,
    transcribe_with_whisper,
    whisper_stt_enabled,
    synthesize_with_openai,
    openai_audio_enabled,
)

# ✅ Multi-agent system:
from backend.agents import (
    intent_agent,
    service_discovery_agent,
    eligibility_agent,
    document_verification_agent,
    compliance_agent,
    workflow_guidance_agent,
    grievance_agent,
    fusion_agent
)
```

---

## 🚀 Deployment Decision Tree

```
Is this a new project?
├─ YES → Use app.py ✅
│        (Modern, clean, recommended)
│
└─ NO → Use streamlit_app.py ⚠️
        (Legacy support, backward compatible)
```

---

## 🔍 How to Check If Everything Works

### 1. Verify Backend Package
```bash
python -c "import backend; print('✅ Backend package imports correctly')"
```

### 2. Verify Agents
```bash
python -c "from backend.agents import fusion_agent; print('✅ Agents import correctly')"
```

### 3. Test Legacy Imports
```bash
python -c "from backend.knowledge import ingest_knowledge_source; print('✅ Legacy imports work')"
```

### 4. Run Streamlit App
```bash
streamlit run app.py
# OR
streamlit run streamlit_app.py
```

---

## 📝 Key Files Changed/Added (v2.0)

| File | Change | Status |
|------|--------|--------|
| `app.py` | Created (new entry point) | ✨ NEW |
| `streamlit_app.py` | Fixed imports + error handling | 🔧 UPDATED |
| `backend/__init__.py` | Created (package marker) | ✨ NEW |
| `backend/agents/__init__.py` | Created (agent exports) | ✨ NEW |
| `DEPLOYMENT.md` | Created (deployment guide) | ✨ NEW |
| `ENTRY_POINTS.md` | Created (this file) | ✨ NEW |

---

## 🎯 Streamlit Cloud Deployment Steps

### Using Modern Entry Point (app.py)

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "v2.0: Fixed imports and modernized structure"
   git push origin main
   ```

2. **Create Streamlit Cloud App:**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Select your repo
   - **Set "Main file path" to: `app.py`**
   - Click "Deploy"

3. **Add Secrets:**
   - Go to app settings
   - Click "Secrets"
   - Paste contents of `.env.example` (with real values)
   - Save

4. **Test:**
   - Visit your app URL
   - Test each page/feature

---

## ⚡ Quick Test

```bash
# 1. Clone repo
git clone https://github.com/manutevari/cscagent.git
cd cscagent

# 2. Create venv
python -m venv venv
source venv/bin/activate

# 3. Install deps
pip install -r requirements.txt

# 4. Run with modern app
streamlit run app.py

# OR run with legacy app
streamlit run streamlit_app.py

# 5. Visit http://localhost:8501
```

---

## 📚 Documentation

- **DEPLOYMENT.md** - Complete deployment guide
- **README.md** - Project overview and architecture
- **docs/architecture.md** - System design
- **docs/workflow.md** - Workflow examples
- **.env.example** - Environment variables reference

---

## ⚠️ If Import Still Fails on Streamlit Cloud

1. **Verify file exists:**
   ```bash
   ls -la backend/__init__.py
   ```

2. **Commit and push:**
   ```bash
   git add backend/__init__.py
   git commit -m "Ensure backend/__init__.py is tracked"
   git push
   ```

3. **Hard reboot Streamlit Cloud app:**
   - App Settings → "Always rerun" → toggle OFF then ON
   - Or delete and recreate the app

4. **Check logs:**
   - App Settings → "Logs" tab
   - Look for import errors

---

## 🎉 You're Ready!

Both entry points now work. Choose one and deploy to Streamlit Cloud. See **DEPLOYMENT.md** for detailed instructions.
