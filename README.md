# 💼 AI Career Assistant

An intelligent career assistant built with **Python + Streamlit** that helps users search jobs, analyze resumes using ATS scoring, track applications, and get personalized career insights.

---

## 🌟 Overview

This project is designed to simplify the job search process by combining multiple tools into a single platform:

* 🔍 Job discovery
* 📄 Resume evaluation
* 🧠 Skill gap analysis
* 📊 Application tracking
* 🤖 Career guidance

---

## 🚀 Key Features

### 🔍 Job Search Dashboard

* Search jobs by role (e.g., Developer, Analyst)
* Combines:

  * Static job listings
  * API-based jobs
  * Scraped job data
* Skill-based matching system

---

### 📄 ATS-Friendly Resume Analyzer

* Upload resume (PDF / TXT)
* Extracts and analyzes skills
* Provides:

  * 🎯 ATS Score (0–100)
  * ✅ Skills found
  * ❌ Missing skills
  * 📌 Job description keyword match
* Actionable improvement suggestions

---

### 🧠 Skills Gap Analysis

* Identifies missing skills
* Recommends learning paths

---

### 🏢 Company Insights

* Displays company-level information
* Helps understand work culture and expectations

---

### 📊 Job Application Tracker

* Save jobs locally using SQLite
* Update status:

  * Saved
  * Applied
  * Interview
* Organized tracking system

---

### 📥 Export Functionality

* Download job data as:

  * CSV
  * PDF

---

### 🤖 Career Chatbot

* Provides guidance on:

  * Job search strategies
  * Resume improvement
  * Skill development

---

## 🛠️ Tech Stack

* Python
* Streamlit
* SQLite
* Pandas
* Requests
* BeautifulSoup
* PyPDF2
* ReportLab

---

## 📁 Project Structure

```bash
agentic_ai/
│
├── app.py
├── scraper.py
├── jobs_api.py
│
├── utils/
├── db/
├── export/
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/ai-career-assistant.git
cd ai-career-assistant
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

---

### 5️⃣ Open in Browser

```
http://localhost:8501
```

---

## 🧪 How to Use

1. Enter your skills
2. Search job roles
3. Upload your resume
4. Paste job description
5. Save jobs & track status
6. Export job data
7. Use chatbot for guidance

---

## ⚠️ Limitations

* Some job scraping may fail due to website restrictions
* Chatbot is rule-based (not a full AI model)
* Resume parsing depends on PDF text extraction

---

## 🔮 Future Improvements

* Integration with real job APIs (LinkedIn, Naukri)
* AI-powered chatbot (LLM integration)
* Improved UI/UX design
* Authentication system
* Resume builder feature

---

## 🎯 Project Status

✅ Fully functional
✅ Deployable
✅ Portfolio-ready

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
