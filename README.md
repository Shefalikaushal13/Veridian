# 🧬 Veridian – AI Resume Analyzer & Job Match Optimizer

**Track, Improve, and Optimize Your Resume for ATS**  
Most resumes fail before a human ever sees them — Veridian helps you beat the bots and get noticed for the right reasons.

Recruiters often rely on **Applicant Tracking Systems (ATS)** to filter resumes before any human reads them. That means a great-looking resume can still get ignored if it lacks the right keywords or structure. **Veridian** changes that.

**Veridian** is an AI-powered web application that evaluates your resume against a job description using **Google Gemini**, providing honest, actionable insights with no sugarcoating — just real feedback that actually works.

---

## 🧠 What Veridian Does

Veridian provides a set of AI-driven tools, each activated via a dedicated button:

- ✅ **Modular Interface with Separate Buttons**  
  Choose which analysis to perform: job match, resume overview, or missing keywords.
  
- 📊 **Job Match Percentage**  
  Analyze how closely your resume aligns with a given job description using semantic similarity and gives you high, medium and low match areas.

- 📄 **Resume Overview**  
  Get a clear, AI-generated summary of your resume highlighting its core strengths and weaknesses.

- 🧩 **Missing Keywords**  
  Identify important keywords present in the job description but missing from your resume — essential for ATS optimization.

Each module runs independently, giving users full control over what they want to analyze.

---

## 🖼️ Demo

🔗 **Live App**: [https://shefalikaushal13-veridian-app-st6cqt.streamlit.app/](https://shefalikaushal13-veridian-app-st6cqt.streamlit.app/)
<img width="1919" height="904" alt="Screenshot 2025-07-27 200900" src="https://github.com/user-attachments/assets/86ef25ca-4cac-4144-9824-2f0fd96152d6" />
<img width="1919" height="901" alt="Screenshot 2025-07-27 201217" src="https://github.com/user-attachments/assets/e78b147a-69c8-4a70-83ce-3aa49012a93a" />
<img width="1919" height="901" alt="Veridian3" src="https://github.com/user-attachments/assets/ddd46c84-b918-4ccb-8042-cf8fa4b837ba" />

---

## 🚀 Tech Stack

| Layer         | Technology                       |
|---------------|----------------------------------|
| Language      | Python                           |
| Framework     | Streamlit                        |
| AI Model      | Google Gemini - 2.5-flash           |
| Resume Parsing| `pdf2image`, `Pillow (PIL)`      |
| Deployment    | Streamlit Cloud                  |

---

## ⚙️ How It Works

### 1. Input Stage
- The user provides a **Job Description** via text input.
- The **Resume** can either be pasted as text or uploaded as a PDF file.
- If a PDF is uploaded, it is converted into text using `pdf2image` and `PIL`.

### 2. Feature Execution via Buttons
Each feature is activated using its own button, giving users control over the analysis they want to perform:

#### 📊 Job Match Percentage
- Compares the semantic similarity between the resume and job description.
- Uses Gemini to analyze both and returns a **match percentage score**.
- Helps determine how well your resume aligns with the job’s requirements.

#### 📄 Resume Overview
- Sends the resume text to Gemini to generate a **natural language summary**.
- Provides an AI-curated overview of strengths, tone, and focus areas.
- Useful for quickly understanding how your resume presents you.

#### 🧩 Missing Keywords
- Extracts relevant keywords from the job description.
- Compares them with those found in your resume.
- Returns a list of **missing or underused keywords** to improve your ATS performance.

### 3. Output Stage
- Results from each button are displayed in separate, neatly formatted sections.
- Users can interact with one or more tools in any order.
- The app ensures a lightweight, responsive UI using Streamlit for seamless navigation.

---

## 📌 Why “Veridian”?

The name **Veridian** blends the ideas of **verification**, **verdant** (symbolizing green, growth), and **honesty** — representing clarity, transparency, and a fresh approach to career development.

It reflects the app's core mission:  
To help users grow professionally by making their resumes **smarter**, more **honest**, and **strategically aligned** with job descriptions — so they can beat the bots and get noticed for the right reasons.

---

## ✍️ Author

**Shefali Kaushal**  
📍 India  
🔗 [LinkedIn](https://www.linkedin.com/in/shefalikaushal13)  
🌐 [Peerlist](https://peerlist.io/shefalikaushal)

---


