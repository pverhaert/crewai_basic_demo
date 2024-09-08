# CrewAI Basic Demo

This repository contains short demonstrations for using CrewAI, showcasing how to create and manage AI agents for various tasks.

## Table of Contents

- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [Demos](#demos)
- [Tips](#tips)

## Requirements

Before you begin, ensure you have the following installed:

- [Git](https://git-scm.com/)
- [Python](https://www.python.org) version 3.10.x or 3.11.x
- A free [Groq API key](https://console.groq.com/keys)
- A free [Serper API key](https://serper.dev/api-key)

## Getting Started

1. Clone this repository: `git clone https://github.com/pverhaert/crewai_basic_demo`
2. Set up the environment:\
   **Windows:**
   - Double-click the `install.bat` file to automatically:
     - Create the virtual environment
     - Install dependencies
     - Create a `.env` file
   
   **Linux or macOS:**
   - Create a virtual environment: `python -m venv .venv`
   - Activate the virtual environment: `source .venv/bin/activate`
   - Install dependencies: `pip install -r requirements.txt`
   - Rename `.env.example` to `.env`

## Configuration

### Groq API

1. Generate an API key at [Groq Console](https://console.groq.com/keys)
2. Choose your preferred [model](https://console.groq.com/docs/models)
3. Update the `.env` file with your API key and model name:
````sh
OPENAI_API_KEY=gsk_your_api_key_here
OPENAI_MODEL_NAME=llama-3.1-70b-versatile
OPENAI_API_BASE=https://api.groq.com/openai/v1
````


### Serper API

1. Generate an API key at [Serper](https://serper.dev/api-key)
2. Update the `.env` file with your API key:
````sh
SERPER_API_KEY=your_api_key_here
````


## Demos

### Demo 1: Single Agent

This demo features one agent (`researcher`) with one task (`get_info_task`).\
The agent uses only its own knowledge to answer questions, without internet access.

**To run:**
- Windows: Double-click `demo1.bat`
- Manual: 
  1. Activate the virtual environment
  2. Run `python demo1/main.py`

### Demo 2: Multi-Agent Collaboration

This demo showcases three agents (`researcher`, `summarizer`, and `writer`) working on three tasks (`research_task`, `summarize_task`, and `write_task`).\
The goal is to write a paper on a given topic based on recent internet articles.

**To run:**
- Windows: Double-click `demo2.bat`
- Manual:
  1. Activate the virtual environment
  2. Run `python demo2/main.py`

## Tips

- Install the [Markdown Viewer](https://chromewebstore.google.com/detail/markdown-viewer/ckkdlimhmcjmikdlpkmbgfkaikojcbjk) Chrome extension to easily view markdown files in your browser.
- Configure the extension to [access your local files](https://github.com/simov/markdown-viewer?tab=readme-ov-file#manage-origins).
- Drag and drop markdown files into your browser for quick viewing.
   
