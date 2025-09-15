### how to create uv project
```bash
uv init your-project-name
cd your-project-name
```

### create a virtual environment at the top level of your project directory
```bash
uv venv
```

### create a virtual environment
```bash
source .venv/bin/active
```


### use uv to add two dependecies to the project they will be added to the file pyproject.toml
```bash
uv add google-genai==1.12.1
uv add python-dotenv==1.12.1
```

### To run the project using the uv virtual environment, you use
```bash
uv run main.py
```





