# Cody

**A Command-Line AI Coding Assistant powered by Google Gemini**

Cody is an intelligent coding companion that brings AI-powered assistance directly to your terminal. Built with Python and integrated with Google's Gemini API, Cody can read, write, execute, and explain code while maintaining a conversational interface that feels natural and intuitive.

## Features

- **Terminal Interface**: Chat with your AI coding assistant directly from the command line
- **Code Generation**: Generate code snippets and complete programs based on prompts
- **Code Execution**: Run Python scripts with real-time feedback and error handling
- **File Operations**: Read from and write to files in your project directory
- **Code Explanation**: Get detailed explanations for complex code structures and algorithms
- **Conversational AI**: Talk with it XD.

## Quick Start

### Prerequisites

- **Python 3.10+** installed on your system
- **Google Gemini API key** (Get yours here: https://makersuite.google.com/app/apikey)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/darginmathi/Cody
   cd Cody
   ```

2. **Set up virtual environment** (recommended)
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   touch .env
   ```
   Add your Gemini API key to the `.env` file:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

5. **Configure settings**
   - Update `WORKING_DIR` in the config file to point to your project directory
   - Adjust `MAX_CHARS` if you need to work with larger files

### Usage

Start Cody with:
```bash
python main.py
```

Once started, you can interact with Cody using natural language:

```
> Explain how bubble sort works
> Create a function to reverse a string
> Run the script in ./examples/hello.py
> Write a class for a simple calculator
```

## Example Interactions

**Code Generation:**
```
User: Create a function that finds the factorial of a number
Cody: Here's a factorial function with both recursive and iterative approaches...
```

**Code Explanation:**
```
User: Explain the code in my_algorithm.py
Cody: This code implements a depth-first search algorithm. Let me break it down...
```

**File Operations:**
```
User: Read the contents of ./data/config.json and explain its structure
Cody: I'll read the file and analyze its structure for you...
```

## Current Limitations

- **Python Only**: Code execution is currently limited to Python scripts
- **Path Specification**: Need to manually set working directory so that Cody only has access to specified directory
