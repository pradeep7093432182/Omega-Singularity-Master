# 🌌 Ω-SINGULARITY v3 — The Autonomous AI Orchestrator (The Silent Factory)

> **You give it a goal. It thinks, researches, hires agents, executes commands, critiques itself, evolves its own code, and reports back. No Manus. No handholding.**

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![Self-Evolving](https://img.shields.io/badge/Self--Evolving-YES-purple.svg)]()
[![Terminal Execution](https://img.shields.io/badge/Terminal-Autonomous-red.svg)]()
[![Security Arsenal](https://img.shields.io/badge/Arsenal-Kali%20%7C%20Metasploit-darkred.svg)]()

---

## ⚡ What is Omega?

Omega is a **10-phase autonomous AI orchestrator** that:

1. **Thinks** — Auto-translates vague goals into precise master specs
2. **Remembers** — Vector-based Akashic Memory recalls past experiences
3. **Researches** — Deep-searches GitHub, Wikipedia, StackOverflow, HuggingFace live
4. **Recruits** — Autonomously finds and hires AI agents from the internet
5. **Swarms** — Runs parallel agent sub-networks (Hive Mind)
6. **Executes** — Actually runs shell commands itself via Autonomous Terminal
7. **Self-Critiques** — Creator vs. Critic adversarial internal dialogue
8. **Evolves** — Modifies its own orchestration code safely
9. **Ascends** — Permanently injects learned patterns into agent definitions
10. **Weaponizes** — Wields Kali Linux, Metasploit, OSINT tools

---

## 🚀 Quick Start

```bash
# 1. Clone
git clone https://github.com/pradeep7093432182/Omega-Singularity-Master
cd Omega-Singularity-Master

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure (optional but unlocks cloud agents)
cp .env.example .env
# Edit .env and add your API keys

# 4. Run your first goal
python orchestrator.py "build a REST API for a todo app with JWT auth"
```

---

## 🧰 Requirements

### Minimum (works offline)
- Python 3.10+
- `pip install -r requirements.txt`

### Full Power (cloud agents + deep research)
```bash
pip install scikit-learn google-generativeai openai requests beautifulsoup4
```

### Security Arsenal (optional, Kali Linux / Debian)
```bash
apt-get install nmap nikto sqlmap gobuster ffuf hydra john hashcat masscan
# OR: set up Kali Linux WSL
```

### Android Bridge (optional)
- ADB installed and in PATH
- Android device connected via USB or WiFi with USB debugging ON
- Termux app with SSH or ADB access

---

## 🗝️ Environment Variables

Create a `.env` file or set in your shell:

```env
# ─── Primary LLM (Tier 3 Bridge) ───
GOOGLE_API_KEY=your_gemini_key_here

# ─── Secondary LLM (Tier 4 Bridge) ───
OPENAI_API_KEY=your_openai_key_here

# ─── Agent Recruitment ───
GITHUB_PAT=your_github_personal_access_token
GROQ_API_KEY=your_groq_key_for_fast_inference
HF_TOKEN=your_huggingface_token
MISTRAL_API_KEY=your_mistral_key
COHERE_API_KEY=your_cohere_key

# ─── Security Research ───
SHODAN_API_KEY=your_shodan_key
```

**No keys = works in offline mode. Omega degrades gracefully.**

---

## 💻 CLI Commands

```bash
# ─── MAIN ORCHESTRATION ───────────────────────────────────
python orchestrator.py "your goal here"

# Examples:
python orchestrator.py "build a real-time chat app with WebSockets"
python orchestrator.py "analyze this codebase for security vulnerabilities"
python orchestrator.py "create a crypto trading bot with backtest"
python orchestrator.py "set up a Kubernetes cluster with monitoring"

# ─── STATUS & DIAGNOSTICS ─────────────────────────────────
python orchestrator.py --status          # Bridge connectivity status
python orchestrator.py --arsenal         # Security tools availability
python orchestrator.py --roster          # All hired agents

# ─── AGENT RECRUITMENT ────────────────────────────────────
python orchestrator.py --hire "code generation specialist"
python orchestrator.py --hire "security vulnerability scanner"
python orchestrator.py --hire "data analysis and ML pipelines"

# ─── DEEP RESEARCH ────────────────────────────────────────
python orchestrator.py --research "kubernetes operator pattern go"
python orchestrator.py --research "zero-day exploit mitigation 2024"
python orchestrator.py --research "transformer architecture attention mechanism"

# ─── SECURITY SCANS (AUTHORIZED SYSTEMS ONLY) ─────────────
python orchestrator.py --scan 192.168.1.0/24   # Network scan
python orchestrator.py --scan https://example.com  # Web vuln scan

# ─── DIRECT TERMINAL EXECUTION ────────────────────────────
python orchestrator.py --exec "nmap -sV 192.168.1.1"
python orchestrator.py --exec "git log --oneline -10"
python orchestrator.py --exec "docker ps -a"
```

---

## 🏗️ Architecture

```
Ω-SINGULARITY v3
├── orchestrator.py              ← Master 10-phase loop
├── core/
│   ├── terminal.py              ← Autonomous command execution engine
│   ├── agent_recruiter.py       ← Internet agent hunting & hiring
│   ├── web_researcher.py        ← Deep research (GitHub/Wiki/SO/HF)
│   ├── security_arsenal.py      ← Kali/Metasploit/OSINT integration
│   ├── akashic_memory.py        ← Vector RAG long-term memory
│   ├── hive_mind.py             ← Parallel agent swarms
│   ├── adversarial_core.py      ← Creator vs Critic dialogue
│   ├── ascension_engine.py      ← Pattern injection & evolution
│   ├── evolution_engine.py      ← Safe self-modification
│   ├── bridge.py                ← SmartBridge fallback chain
│   ├── cognitive_core.py        ← think / feel / judge / sense
│   ├── agent_runner.py          ← LLM execution (Gemini/OpenAI/offline)
│   └── memory.py                ← Session context tracking
├── agents/
│   ├── planner.md               ← Planning agent role
│   ├── executor.md              ← Execution agent role
│   ├── verifier.md              ← QA/verification agent role
│   ├── meta_planner.md          ← Self-modification agent role
│   ├── critic.md                ← Adversarial critic role
│   └── researcher.md            ← Research agent role
└── .planning/
    ├── ROADMAP.md               ← Phase-by-phase roadmap
    └── REQUIREMENTS.md          ← 21 traced requirements
```

---

## ⚡ Powers

### 1. Autonomous Terminal (`core/terminal.py`)
Omega **actually executes commands** — not just plans them.
```python
terminal = AutonomousTerminal()
terminal.run("nmap -sV 192.168.1.1")           # Execute anything
terminal.install_package("playwright")          # Self-install dependencies
terminal.print_arsenal()                        # Show available tools
terminal.arsenal_status()                       # Dict of tool availability
```

### 2. Agent Recruiter (`core/agent_recruiter.py`)
Omega **hunts the internet for AI agents** and hires them.
- Checks environment for existing API keys
- Matches task to best free-tier provider (Groq, Mistral, HuggingFace, Cohere...)
- Searches GitHub for relevant agent repositories
- Verifies agents are alive and capable
- Locks them into the persistent `.agent_roster.json`

```python
recruiter = AgentRecruiter(terminal)
agent = recruiter.hire("GPU-accelerated code generation")
# → HIRED: [a4f21b] Groq API / llama-3.3-70b | fast inference, code
```

### 3. Deep Web Researcher (`core/web_researcher.py`)
Omega **researches the actual internet** before acting.
- GitHub API: repos, code search, README extraction
- HuggingFace API: models, datasets, spaces
- StackOverflow: solutions by vote score
- Wikipedia: structured knowledge
- PyPI: package discovery
- Raw URL fetching with content extraction

### 4. Security Arsenal (`core/security_arsenal.py`)
Omega **wields Kali Linux and security tools** directly.
```python
arsenal = SecurityArsenal()
arsenal.nmap_scan("192.168.1.0/24", "vuln")    # Vulnerability scan
arsenal.sqlmap("https://target.com", level=3)  # SQL injection test
arsenal.msf_run_module("auxiliary/scanner/smb/smb_ms17_010", {"RHOSTS": "..."})
arsenal.theHarvester("example.com")            # OSINT email harvesting
arsenal.smart_scan("192.168.1.1")              # Auto-select best tools
```
> ⚠️ **AUTHORIZED SYSTEMS ONLY.** All ops are logged to `.security_audit.json`.

### 5. SmartBridge (`core/bridge.py`)
5-tier self-healing fallback. Never dies.
```
Tier 1: Local Heuristics     (always available)
Tier 2: Android ADB Bridge   (auto-detected via `adb devices`)
Tier 3: Google Gemini API    (if GOOGLE_API_KEY set)
Tier 4: OpenAI API           (if OPENAI_API_KEY set)
Tier 5: GracefulDegrade      (logs to escalation_log.json, never crashes)
```

### 6. Akashic Memory (`core/akashic_memory.py`)
Persistent vector memory. Omega **learns from every run**.
- TF-IDF cosine similarity retrieval
- Keyword fallback when scikit-learn unavailable
- Survives process restarts (`.akashic_memory.json`)

### 7. Hive Mind (`core/hive_mind.py`)
Parallel agent swarms with **thread-safe output**.
- Multiple agents run concurrently
- Log buffering prevents stdout interleaving
- Configurable timeout per agent

### 8. Adversarial Core (`core/adversarial_core.py`)
**Creator vs. Critic** — Omega argues with itself.
- Executor proposes → Critic attacks it → Creator refines
- Max 2 iterations (prevents infinite loops)
- `passed = True` triggers Ascension

### 9. Ascension Engine (`core/ascension_engine.py`)
Omega **permanently evolves its agent definitions**.
- Extracts successful patterns from executions
- Injects into `agents/executor.md`, `agents/planner.md`
- Patterns accumulate across all runs

### 10. Evolution Engine (`core/evolution_engine.py`)
Omega **modifies its own code safely**.
- Automatic backup before any self-modification
- Restore capability if modification breaks things
- Protected file list prevents catastrophic self-deletion

---

## 🔒 Persistent State Files

| File | Purpose |
|------|---------|
| `.akashic_memory.json` | Long-term vector experience memory |
| `.ascension_patterns.json` | Learned architectural patterns |
| `.ascension_log.json` | All ascension events |
| `.agent_roster.json` | Hired agent registry |
| `.evolution_backups/` | Pre-modification code snapshots |
| `.security_audit.json` | Security tool operation log |
| `escalation_log.json` | Bridge escalation events |

---

## 🧪 Test Results

Tested with the most brutal tasks in offline mode:

| Task | Phases | Time | Status |
|------|--------|------|--------|
| "Build distributed WebSocket server, 100k connections, Redis, JWT, K8s, Grafana" | 10/10 | ~8s | ✅ PASS |
| "Build self-healing K8s operator in Go with GPU autoscaling and Istio service mesh" | 10/10 | ~8s | ✅ PASS |
| "Implement zero-day exploit scanner with Metasploit automation" | 10/10 | ~8s | ✅ PASS |
| "Build autonomous AI agent that hires other agents from internet" | 10/10 | ~8s | ✅ PASS |

Akashic Memory accumulates across runs — Omega gets smarter with every task.

---

## 🌐 Bridge Connectivity Test

```bash
python orchestrator.py --status
```

Expected output:
```
🔗 SmartBridge Status
────────────────────────────────────────
  Local agents:     ✓ Always available
  Android ADB:      ✓ Device: emulator-5554   ← or ✗ if not connected
  Gemini Cloud:     ✓ Key configured           ← or ✗ if no key
  OpenAI Cloud:     ✗ No OPENAI_API_KEY
────────────────────────────────────────
```

---

## 📡 Tri-Core Mesh Integration

Omega is designed for the **Tri-Core Mesh Network**:
- **Nova (Laptop)** — Primary orchestrator node
- **Luna (Android/Termux)** — Android bridge via ADB
- **Aura (Cloud)** — Gemini/OpenAI cloud execution

When Android bridge is unavailable, Omega automatically escalates to cloud agents. When cloud is also unavailable, it degrades gracefully and logs the escalation.

---

## 🤝 Contributing

Omega evolves itself. But you can also contribute:
1. Fork the repo
2. Add a new `core/` module
3. Wire it into `orchestrator.py` as a new phase
4. It will inject patterns into agent definitions automatically

---

## ⚖️ Legal & Ethics

- Security tools are for **authorized penetration testing only**
- All security operations are logged to `.security_audit.json`
- Agent recruitment targets **free/open API tiers** only
- Self-modification never touches system files or protected paths

---

*Built with the Ω-SINGULARITY Protocol. Author: pradeep7093432182.*