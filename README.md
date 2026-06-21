# CSC Mitra AI

An intelligent, multi-agent platform for Citizen Service Centre (CSC) governance powered by LangGraph, ChromaDB, and LLMs.

## 🎯 Overview

CSC Mitra AI transforms citizen service delivery through:

- **Multi-Agent Architecture**: Specialized agents for intent, discovery, eligibility, verification, compliance, guidance, and grievances
- **Agentic RAG**: Knowledge-powered responses with semantic search and reranking
- **LangGraph Orchestration**: Intelligent workflow management and agent coordination
- **Streamlit Frontend**: User-friendly interfaces for citizens, VLEs, officers, and admins
- **Streamlit Cloud Ready**: Optimized for serverless deployment

## ✨ Key Features

### 🤖 Multi-Agent System

- **Intent Agent**: Understands user intent
- **Service Discovery**: Finds relevant services
- **Eligibility Assessment**: Verifies user eligibility
- **Document Verification**: AI-powered document validation
- **Compliance Checking**: Ensures policy compliance
- **Workflow Guidance**: Step-by-step process assistance
- **Grievance Management**: Complaint lifecycle handling
- **Fusion Agent**: Orchestrates all agents intelligently

### 📱 User Interfaces

- **CSC Assistant**: AI-powered query resolution
- **Grievance Redressal**: Complaint filing and tracking
- **Knowledge Base**: Document management and search
- **VLE Dashboard**: Officer case management
- **Compliance Dashboard**: Officer review and approval
- **Admin Dashboard**: Analytics and system monitoring

### 💡 Capabilities

- Service discovery across multiple schemes
- Eligibility assessment with detailed criteria
- Document verification with OCR support
- Workflow guidance with step tracking
- Real-time SLA monitoring
- Knowledge base with semantic search
- Multi-language support
- Voice input/output support

## 🏗️ Repository Structure

```
csc_governance_platform/

├── .streamlit/
│   ├── config.toml              # Streamlit configuration
│   └── secrets.toml             # Secrets management
│
├── app.py                        # Home page entry point
├── requirements.txt              # Python dependencies
├── .env.example                  # Environment template
│
├── pages/                        # Streamlit pages
│   ├── 1_CSC_Assistant.py       # Multi-agent assistant
│   ├── 2_Grievance_Redressal.py # Complaint management
│   ├── 3_Knowledge_Base.py      # Document management
│   ├── 4_VLE_Dashboard.py       # VLE case tracking
│   ├── 5_Officer_Dashboard.py   # Compliance review
│   └── 6_Admin_Dashboard.py     # System administration
│
├── backend/
│   ├── agents/                   # Multi-agent system
│   │   ├── intent_agent.py
│   │   ├── service_discovery_agent.py
│   │   ├── eligibility_agent.py
│   │   ├── document_verification_agent.py
│   │   ├── compliance_agent.py
│   │   ├── workflow_guidance_agent.py
│   │   ├── grievance_agent.py
│   │   └── fusion_agent.py       # Orchestrator
│   │
│   ├── graph/                    # LangGraph workflows
│   │   ├── workflow.py
│   │   ├── state.py
│   │   └── nodes/
│   │
│   ├── services/                 # Business logic
│   │   ├── ingestion.py
│   │   ├── chunking.py
│   │   ├── embeddings.py
│   │   ├── retrieval.py
│   │   ├── reranker.py
│   │   ├── citation.py
│   │   └── metadata_filter.py
│   │
│   ├── workflows/                # Engines
│   │   ├── token_manager.py
│   │   ├── planner.py
│   │   ├── ticket_engine.py
│   │   ├── sla_engine.py
│   │   └── assignment_engine.py
│   │
│   ├── models/                   # Data models
│   │   ├── complaint.py
│   │   ├── citizen.py
│   │   ├── authority.py
│   │   └── resolution.py
│   │
│   └── db/                       # Database access
│       ├── postgres.py
│       └── schema.sql
│
├── knowledge_base/               # Knowledge management
│   ├── uploads/
│   ├── processed/
│   ├── vectorstore/              # ChromaDB
│   └── metadata/
│
├── data/                         # Service-specific data
│   ├── csc/
│   ├── pmkisan/
│   ├── passport/
│   ├── ayushman/
│   └── digipay/
│
├── assets/                       # Static assets
│   ├── css/
│   ├── logo.png
│   └── README.md
│
├── docs/                         # Documentation
│   ├── architecture.md
│   ├── workflow.md
│   └── README.md
│
└── tests/                        # Test suite
```

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- PostgreSQL (use Neon or Supabase for Streamlit Cloud)
- OpenAI API key
- Streamlit account (for cloud deployment)

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/csc-governance-platform.git
   cd csc-governance-platform
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your credentials
   ```

5. **Set up Streamlit secrets**
   ```bash
   mkdir -p ~/.streamlit
   cp .streamlit/secrets.toml ~/.streamlit/
   # Edit with your actual API keys
   ```

6. **Run locally**
   ```bash
   streamlit run app.py
   ```

### Streamlit Cloud Deployment

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Deploy to Streamlit Cloud"
   git push origin main
   ```

2. **Connect to Streamlit Cloud**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Select your repository and main file (`app.py`)
   - Deploy

3. **Add secrets**
   - In Streamlit Cloud dashboard, go to Settings
   - Click "Secrets"
   - Add your OpenAI, Cohere, and database credentials

## 📋 Configuration

### Streamlit Settings (`.streamlit/config.toml`)

```toml
[theme]
primaryColor = "#FF6B35"
backgroundColor = "#FFFFFF"

[server]
port = 8501
maxUploadSize = 200
enableXsrfProtection = true
```

### Environment Variables (`.env`)

See `.env.example` for complete list. Key variables:

- `OPENAI_API_KEY`: GPT-4 access
- `COHERE_API_KEY`: Cohere models access
- `DATABASE_URL`: PostgreSQL connection
- `CHROMA_DB_PATH`: Vector database path
- `LANGCHAIN_API_KEY`: LangChain tracing

## 🔌 Agent Architecture

### Fusion Agent Orchestration

```
User Query
    ↓
Fusion Agent
    ├─ Intent Detection
    ├─ Agent Selection
    ├─ Execution Planning
    ├─ Dependency Resolution
    └─ Result Synthesis
         ↓
    [Output]
```

### Example: Service Discovery Query

```
Q: "What services can I get for farmers?"

Fusion Agent:
  ├─ Intent: SERVICE_DISCOVERY (95% confidence)
  ├─ Invoke: ServiceDiscoveryAgent
  └─ Enhance with: EligibilityAgent, WorkflowGuidanceAgent

Result:
  ✓ PM-KISAN (99% relevant)
  ✓ e-Shram (95% relevant)
  ✓ With eligibility criteria and workflow steps
```

## 📚 Knowledge Base

### Supported Formats

- PDF documents
- Word files (DOCX)
- Plain text (TXT)
- URLs

### Processing Pipeline

```
Upload → OCR → Chunking → Embedding → ChromaDB
             ↓
        Metadata Extraction
```

### Search Features

- Semantic search with BGE embeddings
- Reranking for relevance
- Metadata filtering
- Citation tracking

## 🎯 Capstone Requirements Coverage

✅ **Multi-Agent Architecture**: 8 specialized agents
✅ **Agentic RAG**: Knowledge base with semantic search
✅ **Service Discovery**: Find relevant government services
✅ **Eligibility Assessment**: Check scheme eligibility
✅ **Document Verification**: AI document validation
✅ **Compliance Validation**: Policy compliance checks
✅ **Grievance Management**: Complaint lifecycle
✅ **Human-in-Loop**: Officer approval workflows
✅ **Analytics Dashboard**: System monitoring and insights

## 🛠️ Development

### Adding a New Agent

1. Create `backend/agents/your_agent.py`
2. Implement agent class with async methods
3. Add to `backend/agents/__init__.py`
4. Register with Fusion Agent

### Adding a New Page

1. Create `pages/X_PageName.py`
2. Use Streamlit components
3. Import backend services
4. Deploy automatically

### Backend Services

- **Ingestion**: Document upload and processing
- **Chunking**: Semantic or fixed-size chunking
- **Embeddings**: BGE model for vector generation
- **Retrieval**: Semantic search with top-K
- **Reranker**: Re-rank for relevance
- **Citation**: Track source documents

## 📊 Workflows

### Grievance Resolution (SLA: 48 hours for High priority)

```
File → Ticket Created → Assigned → Under Review → Resolved → Closed
        ↓                ↓         ↓               ↓
    Notification    SLA Alert  Compliance      Citizen Notified
```

### Service Registration

```
Query Service → Check Eligibility → Gather Docs → Visit CSC → Submit → Confirm
    ↓               ↓                    ↓            ↓         ↓        ↓
 Browse        Assessment            Guidance      Verification  Approval  Track
```

## 🔐 Security

- JWT-based authentication
- CORS protection
- Encrypted credentials
- Audit logging
- Role-based access control
- Document encryption

## 📈 Performance

- LLM response caching
- Vector DB indexing
- Connection pooling
- Query optimization
- Streaming responses

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

## 🙏 Acknowledgments

- LangChain team for LangGraph
- Streamlit for amazing framework
- OpenAI and Cohere for LLMs
- Hugging Face for embeddings

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing documentation
- Review workflow examples

## 🗺️ Roadmap

- [ ] Multi-language support expansion
- [ ] Mobile app integration
- [ ] Advanced analytics
- [ ] Custom workflow builder
- [ ] Blockchain audit trail
- [ ] Real-time notifications
- [ ] Voice conversation UI
- [ ] Integration with state systems

---

**CSC Mitra AI** - Empowering Citizens Through Intelligent Service Delivery
