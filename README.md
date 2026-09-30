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

The application was deployed to an AWS EC2 instance using infrastructure created with Terraform.

The application runs on the EC2 server and is managed by a systemd service. This allows the application to continue running without an active SSH connection and start automatically when the server starts.


## Documentation

Phase 1 – Research
Project Idea
The project is an AI Log Analyzer, a web application that uses Generative AI to analyze technical logs from computers, servers and network systems.
The user can paste log data into the application. The AI analyzes the log and identifies important information such as errors, warnings, network problems or authentication problems.
The result is presented in a structured and easy-to-understand format.
Purpose
The purpose of the application is to make technical logs easier to understand. Log files can contain a large amount of technical information, which can make troubleshooting difficult and time-consuming.
The AI Log Analyzer helps the user identify possible problems, understand what the log messages mean and receive recommended troubleshooting actions.
The application can be useful for IT support technicians, network technicians and system administrators.
Information Gathering
Before starting the development, information was gathered about log analysis, Generative AI, web development and AWS hosting.
Previous experience from the AI Network Assistant project was also used to understand how a Generative AI API can be integrated into a Python web application.
Research was focused on how technical logs can be analyzed, how AI can explain errors and warnings, and how the application can be deployed to AWS.
Information about Python, Flask, Google Gemini, AWS and Terraform was reviewed to plan the technical solution.

Tools and Technologies
The following tools and technologies were selected for the project:
•	Python – used as the main programming language for the application.
•	Flask – used to build the web application and connect the user interface with the backend.
•	HTML, CSS and JavaScript – used to create a modern and responsive user interface.
•	Google Gemini API – used as the Generative AI model to analyze technical logs and generate explanations and recommended actions.
•	SQLite – used to store previous log analyses and create an analysis history.
•	AWS EC2 – used to host the application and make it available online.
•	Terraform – used to create and manage the AWS infrastructure.
•	Git and GitHub – used for version control, backup and publishing the project source code.


Project Plan
The project will be developed step by step.
1.	Create the basic project structure and Flask web application.
2.	Design the user interface using HTML, CSS and JavaScript.
3.	Create an input area where users can paste technical logs.
4.	Integrate the Google Gemini API to analyze the logs.
5.	Present the AI analysis with category, severity, explanation and recommended actions.
6.	Add an SQLite database to save previous analyses and create a history.
7.	Test the application with different types of logs.
8.	Create the AWS infrastructure using Terraform.
9.	Deploy the application to an AWS EC2 instance and make it available online.
10.	Test the final deployed application and make improvements if necessary.
11.	Publish the source code and documentation on GitHub.

Problems and Solutions During Research
Problem 1 – Defining the Project Scope
It was important to make the new project more advanced than the previous AI Network Assistant while keeping the project realistic to develop within the available time.
Solution:
The project was divided into smaller parts. The main functionality will focus on AI log analysis, while additional features such as analysis history and a dashboard will make the application more advanced.
Problem 2 – Selecting the Technologies
Several technologies and AI services could be used for the project, which made it necessary to select tools that work well together.
Solution:
Python, Flask and Google Gemini were selected because they provide a simple way to build and integrate the AI functionality. AWS EC2 and Terraform were selected for deployment and infrastructure management.
Problem 3 – Planning Secure API Key Management
The application requires an API key to communicate with the Generative AI service. Publishing the API key in the source code or on GitHub would create a security risk.
Solution:
The API key will be stored as an environment variable and excluded from GitHub using a .gitignore file.

Phase 2 – Implementation
Starting the Development
The development started by creating the basic structure of the AI Log Analyzer.
Python and Flask were used to create the backend of the application. The first goal was to create a working web application where the user could enter a technical log and receive an AI-generated analysis.
The project was first developed and tested locally before deployment to AWS.
Project Structure
The project was organized into different files and folders to keep the application structured.
The main parts of the project were:
•	app.py – contains the Flask application, Gemini API integration and SQLite database functions.
•	templates/index.html – contains the main user interface.
•	templates/history.html – displays previously saved analyses.
•	static/style.css – contains the design and styling of the application.
•	requirements.txt – contains the required Python packages.
•	.env – stores the Gemini API key locally.
•	.gitignore – prevents sensitive and unnecessary files from being uploaded to GitHub.
•	test-log.txt – used for testing log file uploads.
Creating the Web Application
The Flask application was created in app.py.
The main page allows the user to paste a technical log into a text area. A file upload function was also added so that the user can upload a .txt or .log file instead of manually pasting the log.
When the user clicks Analyze Log, Flask receives the log and sends it to the Generative AI service for analysis.
Generative AI Integration
Google Gemini was integrated using the google-genai Python package.
A prompt was created to instruct the AI to analyze the technical log and return the result using the following structure:
•	Category
•	Severity
•	Finding
•	Explanation
•	Recommended Actions
This makes the AI response easier for the user to understand and provides useful troubleshooting information.
SQLite Database and Analysis History
SQLite was added to store successful log analyses.
The database contains the original log, the AI-generated analysis and the date and time of the analysis.
A separate Analysis History page was created. This allows the user to view previous analyses without analyzing the same log again.
Testing During Development
The application was tested step by step during development.
Different technical logs were entered manually and through the file upload function. The AI responses were checked to make sure that the application returned structured and useful information.
The Analysis History page was also tested to verify that successful analyses were saved correctly in the SQLite database.
Problems and Solutions During Implementation
Problem 1 – Flask Project Structure
Some files and folders were not initially connected correctly, which caused problems when Flask tried to load templates and static files.
Solution:
The project structure was checked and the HTML templates were placed in the templates folder while the CSS file was placed in the static folder.
Problem 2 – Gemini API Errors
During testing, the Gemini model sometimes returned a 503 UNAVAILABLE error because the model was experiencing high demand.
Solution:
The API connection and API key were tested separately. The available Gemini models were checked and gemini-3.6-flash was successfully tested with a simple API request. The application was updated to use this model. Error handling was also used so that an API failure does not crash the complete web application.
Problem 3 – Protecting the API Key
The Gemini API key must not be included directly in the source code or uploaded to GitHub.
Solution:
The API key was stored in a .env file and loaded using python-dotenv. The .env file was added to .gitignore, and Git was checked to confirm that the file was ignored.
Problem 4 – Database Storage
The application needed a simple way to store previous analyses without requiring a separate database server.
Solution:
SQLite was selected because it can run directly with the Python application. A database table was created automatically when the application starts, and successful analyses are saved to the database.

Phase 3 – Finalization and Improvements
AWS Deployment
After the application worked locally, the next step was to deploy it to AWS.
Terraform was used to create the AWS infrastructure. An EC2 instance was created to host the AI Log Analyzer. A Security Group was configured to allow the required network traffic.
SSH was used to connect securely to the EC2 instance and manage the server.
Deploying the Application
The project files were transferred from the local computer to the EC2 instance using SCP.
A Python virtual environment was created on the server. The required Python packages were then installed from requirements.txt.
The .env file containing the Gemini API key was configured separately on the server and was not uploaded to GitHub.
The Flask application was configured to listen on 0.0.0.0 so that it could accept connections from outside the EC2 instance.
Testing on AWS
After deployment, the application was opened using the public IP address of the EC2 instance.
The following functions were tested:
•	Opening the AI Log Analyzer from a web browser
•	Entering a technical log
•	Sending the log to Gemini
•	Displaying the AI analysis
•	Uploading a log file
•	Saving successful analyses to SQLite
•	Opening the Analysis History page
The tests confirmed that the main application functions also worked in the AWS environment.
Running the Application as a Service
Initially, the Flask application was started manually with python app.py. This meant that the application depended on the SSH session.
To improve this, a systemd service was created for the AI Log Analyzer.
The service starts the application in the background and was enabled to start automatically when the EC2 server starts.
The SSH connection was then closed and the public website was tested again. The application continued to work, confirming that the service was running independently.
GitHub
Git and GitHub were used to manage and publish the project source code.
Before pushing the final changes, .gitignore was checked to make sure that sensitive files such as .env and local database files were not included.
The final project changes were committed and pushed to the GitHub repository.
Problems and Solutions During Finalization
Problem 1 – Python Virtual Environment on EC2
When the Python virtual environment was first created on Ubuntu, the required python3-venv package was not installed.
Solution:
The required package was installed and the virtual environment was created again successfully.
Problem 2 – Accessing Flask from the Internet
The Flask application initially listened only on 127.0.0.1, which means localhost.
Solution:
Flask was changed to listen on 0.0.0.0 on port 5000. This allowed the application to accept external connections through the EC2 network configuration.
Problem 3 – Keeping the Application Running
Running the application manually meant that it could stop when the SSH session was closed.
Solution:
A systemd service was created and enabled. The application was tested after closing the SSH connection and remained available.
Problem 4 – Gemini Service Availability
During final testing, Gemini sometimes returned a 503 UNAVAILABLE response because of high demand.
Solution:
Different available models were tested directly. gemini-3.6-flash returned a successful test response and was used by the application. Error handling also prevents a temporary AI service error from crashing the web application.

Phase 4 – Problems and Solutions Summary
During the project, several technical problems occurred. Troubleshooting these problems was an important part of the development process.
Problem – Gemini API returned 503 errors
Solution: The API connection and available models were tested separately. The application was changed to use gemini-3.6-flash, which worked during testing. Error handling was also added so that temporary API problems do not crash the application.
Problem – Protecting the API key
Solution: The Gemini API key was stored in a .env file. The file was added to .gitignore and Git was checked to confirm that the API key would not be uploaded to GitHub.
Problem – Python virtual environment could not be created on EC2
Solution: The required python3-venv package was installed on Ubuntu and the virtual environment was created again.
Problem – The application was not externally accessible at first
Solution: Flask was configured to listen on 0.0.0.0 and the required network access was configured for the EC2 instance.
Problem – The application stopped when running manually
Solution: A systemd service was created and enabled so that the application can run in the background and start automatically with the EC2 server.
Problem – Storing previous analyses
Solution: SQLite was integrated into the application to store successful analyses and provide an Analysis History page.


## Conclusion

The goal of this project was to create an AI Log Analyzer that can help users understand technical logs and identify possible problems.

The final application allows users to paste a technical log or upload a log file. Google Gemini analyzes the log and returns a structured result with category, severity, finding, explanation and recommended actions. Successful analyses are stored in SQLite and can be viewed on the Analysis History page.

The application was successfully deployed to AWS EC2 using infrastructure created with Terraform. A systemd service was also configured so that the application can continue running without an active SSH connection and start automatically with the server.

During this project, I learned more about Python, Flask, Generative AI APIs, SQLite, AWS EC2, Terraform, Linux, Git and GitHub. I also gained more experience in troubleshooting problems step by step.

One possible improvement would be to use a production WSGI server instead of the Flask development server. The application could also be improved with better error handling, more advanced log analysis and additional security features.

Overall, the project resulted in a working AI-powered log analysis application that can run online in an AWS environment.