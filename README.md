# AI Log Analyzer

AI Log Analyzer is a web application that uses Generative AI to analyze technical logs.

The application can help identify problems in server, network, system, and security logs and provide recommended actions.

## Features

- Paste technical logs directly into the web application
- Upload `.txt` and `.log` files
- Analyze logs using the Gemini API
- Display structured AI analysis
- Save successful analyses in a SQLite database
- View previous analyses in Analysis History
- Handle temporary AI API errors without crashing
- Simple and responsive web interface

## AI Analysis

The AI provides the result using the following sections:

- Category
- Severity
- Finding
- Explanation
- Recommended Actions

## Technologies

- Python
- Flask
- Google Gemini API
- SQLite
- HTML
- CSS
- Git and GitHub

## Project Structure

```text
ai-log-analyzer/
├── app.py
├── requirements.txt
├── README.md
├── static/
│   └── style.css
└── templates/
    ├── index.html
    └── history.html
    ```

## Installation

Clone the repository:

```bash
git clone https://github.com/jan0307/ai-log-analyzer.git
cd ai-log-analyzer
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Environment Variable

Create a `.env` file in the project directory:

```text
GEMINI_API_KEY=your_api_key_here
```

The `.env` file is excluded from Git to protect the API key.

## Run the Application

```bash
python app.py
```

Open the application in a web browser:

```text
http://127.0.0.1:5000
```

## Database

The application uses SQLite to store successful log analyses.

Each saved analysis contains:

- Original log
- AI analysis
- Date and time

Previous analyses can be viewed on the Analysis History page.

## Error Handling

If the Gemini API is temporarily unavailable, the application displays an error message instead of crashing.

## Deployment

The application will be deployed to AWS as the final deployment step.