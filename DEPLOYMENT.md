# Streamlit Cloud Deployment Guide

## Quick Start for Streamlit Cloud

### Option 1: Modern Architecture (Recommended) ✅

**Entry Point:** `app.py`

This is the new, clean Streamlit architecture optimized for cloud deployment.

```bash
streamlit run app.py
```

**Structure:**
- Multi-page app with sidebar navigation
- 6 professional dashboards
- Clean Streamlit Cloud integration
- Modern UI with consistent styling

**Deploy to Streamlit Cloud:**
1. Push to GitHub: `git push origin main`
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click "New app"
4. Set **App URL** to: `app.py`
5. Deploy

---

### Option 2: Legacy Support ⚠️

**Entry Point:** `streamlit_app.py`

This maintains backward compatibility with existing backend modules.

```bash
streamlit run streamlit_app.py
```

**Use this if you need:**
- Legacy backend modules (knowledge.py, mas_engine.py, etc.)
- Existing voice features
- Original UI structure

**Deploy to Streamlit Cloud:**
1. Push to GitHub: `git push origin main`
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click "New app"
4. Set **App URL** to: `streamlit_app.py`
5. Deploy

---

## Configuration

### Streamlit Cloud Settings

In **Streamlit Cloud Dashboard** → Your App → **Settings**:

#### 1. **Advanced Settings** (if needed)

```
Python version: 3.9+
Install dependencies using: pip
Requirements file path: requirements.txt
```

#### 2. **Secrets Manager**

Add all secrets here (they map to `.streamlit/secrets.toml`):

```toml
# OpenAI
OPENAI_API_KEY = "sk-..."
OPENAI_MODEL = "gpt-4-turbo"

# Cohere
COHERE_API_KEY = "..."

# Database (Use Neon or Supabase)
DATABASE_URL = "postgresql://..."

# Tavily
TAVILY_API_KEY = "..."

# HuggingFace
HF_API_TOKEN = "..."

# LangChain
LANGCHAIN_API_KEY = "..."
LANGCHAIN_PROJECT = "csc-governance"

# ChromaDB
CHROMA_DB_PATH = "./knowledge_base/vectorstore"

# Other settings
DEBUG_MODE = false
MAX_FILE_UPLOAD_MB = 200
```

---

## Database Setup

### PostgreSQL (Required)

**Choose one:**

#### A. Neon (Recommended - Free tier)
1. Sign up at [neon.tech](https://neon.tech)
2. Create project
3. Copy connection string
4. Add to Streamlit Cloud secrets as `DATABASE_URL`

```
postgresql://[user]:[password]@[neon-host]/[database]?sslmode=require
```

#### B. Supabase (Alternative)
1. Sign up at [supabase.com](https://supabase.com)
2. Create project
3. Go to Settings → Database
4. Copy connection string
5. Add to Streamlit Cloud secrets

#### C. Local Testing
```
postgresql://localhost:5432/csc_governance
```

### ChromaDB (Vector Store)

Persists in `./<repo>/knowledge_base/vectorstore` on Streamlit Cloud

- Automatically created on first run
- Survives redeployments
- Max ~1GB recommended for free tier

---

## Troubleshooting

### Error: "ModuleNotFoundError: No module named 'backend'"

**Fix:**
1. Verify `backend/__init__.py` exists
2. Commit and push to GitHub:
   ```bash
   git add backend/__init__.py
   git commit -m "Ensure backend is proper package"
   git push origin main
   ```
3. Reboot your Streamlit Cloud app
4. Check **Manage app** → **Reboot script**

### Error: "ModuleNotFoundError: No module named 'streamlit_mic_recorder'"

**Fix:**
This is optional. The app handles this gracefully.
```python
try:
    from streamlit_mic_recorder import mic_recorder
except:
    mic_recorder = None  # Feature disabled
```

### App Won't Deploy

1. **Check logs:** Streamlit Cloud → App settings → **View logs**
2. **Verify requirements.txt:** `pip freeze > requirements.txt`
3. **Commit requirements:** `git add requirements.txt && git commit -m "Update deps"`
4. **Force redeploy:** Settings → **Always rerun** → Toggle **Off** then **On**

### Slow Performance

- Reduce `CHROMA_DB_PATH` size (>1GB impacts startup)
- Use external database instead of local
- Optimize imports (lazy loading)

### Port/Connection Issues

Streamlit Cloud automatically assigns a port. Don't specify:
```python
# ❌ Don't do this
streamlit run app.py --server.port 8501

# ✅ Just do this
streamlit run app.py
```

---

## Local Testing Before Deployment

### Test locally first:

```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 2. Install requirements
pip install -r requirements.txt

# 3. Create .streamlit/secrets.toml locally
mkdir -p ~/.streamlit
cp .streamlit/secrets.toml ~/.streamlit/

# 4. Edit with real credentials
# nano ~/.streamlit/secrets.toml

# 5. Run app
streamlit run app.py

# 6. Visit http://localhost:8501
```

---

## Git Workflow for Deployment

```bash
# 1. Make changes
git add .
git commit -m "Add new feature or fix"

# 2. Push to main
git push origin main

# 3. Streamlit Cloud auto-deploys
# (takes 1-2 minutes)

# 4. Check deployment status
# Go to share.streamlit.io → Your App → Status
```

---

## Performance Tips

### 1. Use Streamlit Cloud Cache
```python
@st.cache_data
def expensive_query():
    return fetch_data()

@st.cache_resource
def init_llm():
    return llm_client()
```

### 2. Lazy Load Heavy Modules
```python
import streamlit as st

if "llm" not in st.session_state:
    from backend.mas_engine import ask  # Load only when needed
    st.session_state.llm = ask
```

### 3. Optimize Requirements
Only include needed packages. Remove:
- `jupyter`, `jupyterlab` (not needed for production)
- Heavy ML packages if not used
- Development dependencies

### 4. Stream Responses
```python
with st.spinner("Processing..."):
    for token in llm_stream_response():
        st.write(token, end="")
```

---

## Monitoring

### View Logs
Streamlit Cloud → Your App → **Settings** → **Logs**

### Health Check
Monitor **App resets** and **Memory usage**

### Errors
Check Streamlit Cloud dashboard for:
- Deployment failures
- Runtime errors
- Restart count

---

## Scaling (If Needed)

### When to upgrade:
- App keeps restarting (memory full)
- Timeouts on queries
- Concurrent users > 50

### Options:
1. **Streamlit Cloud Pro** ($5-20/month)
2. **Docker deployment** (Heroku, Railway, Render)
3. **AWS Lambda + API Gateway**

---

## Final Checklist Before Production

- [ ] `backend/__init__.py` exists
- [ ] `requirements.txt` is up-to-date
- [ ] `.streamlit/config.toml` configured
- [ ] All secrets added to Streamlit Cloud
- [ ] Database connection tested locally
- [ ] ChromaDB path configured
- [ ] Deployed and tested in staging
- [ ] Logs reviewed for errors

---

## Support

**Streamlit Cloud Issues:**
- [Streamlit Community Forum](https://discuss.streamlit.io)
- [Streamlit Docs](https://docs.streamlit.io)

**Application Issues:**
- Check `streamlit_app.py` or `app.py` error handling
- Review backend module imports
- Check GitHub Actions logs
