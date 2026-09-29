import os
import sqlite3
from flask import Flask, render_template, request
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("logs.db")

    conn.execute("""
        CREATE TABLE IF NOT EXISTS analyses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            log_text TEXT NOT NULL,
            analysis TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.close()

init_db()


@app.route("/", methods=["GET", "POST"])
def home():
    log_text = ""
    analysis = ""

    if request.method == "POST":
        log_text = request.form.get("log", "").strip()
        log_file = request.files.get("log_file")

        if log_file and log_file.filename:
            try:
                log_text = log_file.read().decode("utf-8")
            except UnicodeDecodeError:
                analysis = "The uploaded file could not be read. Please upload a UTF-8 text or log file."
           
        if log_text:
            prompt = f"""
            Analyze the following technical log.

            Provide the result using these sections:
            Category:
            Severity:
            Finding:
            Explanation:
            Recommended Actions:

            Log:
            {log_text}
            """
            try:
                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt
                )

                analysis = response.text

                conn = sqlite3.connect("logs.db")

                conn.execute(
                    "INSERT INTO analyses (log_text, analysis) VALUES (?, ?)",
                    (log_text, analysis)
                )

                conn.commit()
                conn.close()

            except Exception as e:
                print("GEMINI ERROR:", e)
                analysis = "AI service is temporarily unavailable. Please try again later."

    return render_template(
        "index.html",
        log_text=log_text,
        analysis=analysis
    )


@app.route("/history")
def history():
    conn = sqlite3.connect("logs.db")

    analyses = conn.execute(
        "SELECT id, log_text, analysis, created_at FROM analyses ORDER BY id DESC"
    ).fetchall()

    conn.close()

    return render_template("history.html", analyses=analyses)


if __name__ == "__main__":
    app.run(debug=True)