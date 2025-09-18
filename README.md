# AI Code Assistant

AI Code Assistant is a simple command-line tool that uses Google's Gemini model to help you understand modify and debug code. It works like a mini AI agent iteratively inspecting files reading contents, running code and writing updates based on your prompts.

## Features

- Understands your code and suggests fixes or improvements.
- Can list files, read file content, write files, and run Python scripts.
- Iterative: keeps using its tools until the task is done.
- Optional verbose mode to see each step it takes.

### Installation

1. **Clone this repository**
```bash
git clone https://github.com/UlutasAlperen/ai_agent
cd ai_agent
```
### create a virtual environment at the top level of your project directory
```bash
python -m venv .venv
source .venv/bin/active
```
### Install dependencies

```bash
pip install -r requirements.txt
```
- google-genai==1.12.1

- python-dotenv==1.12.1

- requires-python = ">=3.13"

### create Gemini API key

https://ai.google.dev/gemini-api/docs/api-key

### Add your Gemini API key in a .env file
```
GEMINI_API_KEY=your_api_key_here
```
## Usage

### Run the assistant with a prompt

```bash
python3 main.py "Fix the bug in the calculator" --verbose
```
>**or:**
```bash
uv run main.py "Fix the bug in the calculator" --verbose
```
- The --verbose flag shows each function call and its result.
- The assistant will iteratively analyze your project, use the available tools, and finally provide a solution or explanation.

### Example:
```bash
python main.py "Explain how the calculator prints results"
```
>**or:**
```bash
uv run main.py "Explain how the calculator prints results"
```
#### Output: 
```sql
 - Calling function: get_files_info
 - Calling function: get_file_content
Final response:
The calculator prints results using `print()`, formatting them with `format_json_output`...
```
# Notes
- Tools are defined in call_function.py (get_files_info, get_file_content, run_python_file, write_file).
- System prompts and configuration are in prompts.py.
