# Week 3.1: Tool Calling

## Introduction
Gain insights into how tool calling transforms interactions with LLMs, enabling structured outputs like dictionaries for enhanced API interaction, code execution, and JSON object creation.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- You have installed Python 3.9.x - 3.11x.

## Setup Instructions

### Step 1: Clone the Repository
First, clone the repository to your local machine using the following command:
```bash
git clone [repository-url]
cd [repository-name]
```

### Step 2: Create a Python Virtual Environment
Create a virtual environment using `venv`:
```bash
python3 -m venv .venv
```

### Step 3: Activate the Virtual Environment
Activate the virtual environment:
- On Windows:
  ```bash
  .venv\Scripts\activate
  ```
- On MacOS/Linux:
  ```bash
  source .venv/bin/activate
  ```

### Step 4: Install Required Packages
Install the required packages using `pip`:
```bash
pip install -r requirements.txt
```

### Step 5: Create a `.env` File
Create a `.env` file in the root directory of the project. Use the `.env.sample` file as a reference:
```bash
cp .env.sample .env
```

### Step 6: Update `.env` File
Open the `.env` file and update the key values as necessary.

### Step 7: Run Environment Setup Script
Run the environment setup script:
```bash
python3 setup_env.py
```

## Usage

#### Running In-Class Examples
To run any in-class examples, execute the specific file directly from the command line. For example:

```bash
python3 in_class_examples/openai_function_call.py
```

#### Using Tools Inside `tool_lib`
To use any tools inside the tool_lib, you need to attach them to an agent. Follow these steps:

1. Copy the Function from `tool_lib` to Your Agent Script.

2. Annotate the copied function with the `@tool` decorator.

3. Add the annotated function to your agent's toolkit.

4. Bind the toolkit to the agent executor to make the tool available for use within the agent's workflow.