# AI Chatbot with Memory

A simple AI chatbot built with Streamlit that maintains conversation history and provides contextual responses based on previous interactions.

## Features

* Interactive chat interface
* Conversation memory
* Chat history display
* Streamlit-based web UI
* Simple and easy to customize

## Technologies Used

* Python
* Streamlit
* LangChain
* AI Language Models

## Project Structure

```text
aiagents/
└── day1/
    ├── basic_ai_agents.py
    ├── requirements.txt
    └── README.md
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Ai-agent-repository.git
cd Ai-agent-repository/aiagents/day1
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit langchain langgraph langchain-community langchain-ollama
```

## Running the Application

```bash
python -m streamlit run basic_ai_agents.py
```

The application will be available at:

```text
http://localhost:8501
```

## Usage

1. Open the Streamlit application in your browser.
2. Enter a question in the input field.
3. Submit your query.
4. View the AI response.
5. Previous conversations will be stored in the chat history section.

## Example Questions

* What is an AI agent?
* What is machine learning?
* Explain large language models.
* What is LangChain?

## Future Improvements

* Multiple chat sessions
* Database-backed memory
* User authentication
* File upload support
* Voice input/output
* Integration with cloud AI models

## Author

Navya Manoj

## License

This project is for educational and learning purposes.
