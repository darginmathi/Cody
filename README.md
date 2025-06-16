# Cody – CLI Coding Agent

Cody is a command-line coding assistant powered by the Gemini API. It can read, write, and execute code, acting like a chatbot right in your terminal.

---

## Requirements

**Python:**
Cody is written in Python and requires Python 3.10 or above.

```bash
sudo apt update
sudo apt install python3 python3-pip
```

**Virtual Environment (Recommended):**
To avoid dependency conflicts, it's recommended to use a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Install Dependencies:**
```bash
pip install -r requirements.txt
```
**.env File:**
```bash
touch .env
```
``` bash
GEMINI_API_KEY=your_api_key_here
```

Installation
Clone the repository and install Cody locally:
```bash
git clone https://github.com/darginmathi/cody
cd cody
```

Start
```bash
python main.py
```
This starts an interactive chat interface in your terminal. You can talk to Cody like a coding assistant. Ask questions, get explanations, generate code, or run Python snippets — all from your CLI(need to mention the relative path to directory or file the agent needs to access).

**Notes: **
- Change the WORKING_DIR in config file to the project directory
- Modify MAX_CHARS to allow large files
- Agent can only run python scripts atm
