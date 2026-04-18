import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import streamlit as st
import pandas as pd
import PyPDF2

# Local imports (fixed)
from scraper import scrape_jobs
from jobs_api import fetch_api_jobs
from db.database import connect_db, create_table
from utils.resume_analyzer import analyze_resume
from utils.job_filter import filter_jobs
from utils.company_info import get_company_info
from utils.chatbot import chatbot_response
from export.pdf_export import export_pdf

# -----------------------------
# INIT
# -----------------------------
create_table()

st.set_page_config(page_title="AI Career Assistant", layout="wide")
st.title("💼 AI Career Assistant")

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.header("Filters")
experience = st.sidebar.selectbox("Experience", ["All", "0-2", "2-5", "5+"])

# -----------------------------
# SKILLS INPUT
# -----------------------------
skills_input = st.text_input("Enter your skills (comma separated)")
user_skills = [s.strip().lower() for s in skills_input.split(",")] if skills_input else []

# -----------------------------
# JOB SEARCH
# -----------------------------
role = st.text_input("Search Jobs (e.g. developer, analyst)")

# Static jobs
jobs_data = [
    {"title": "Software Engineer", "company": "TCS", "location": "Bangalore", "salary": 4, "skills": ["python", "sql"], "exp": 1},
    {"title": "Data Analyst", "company": "Infosys", "location": "Mumbai", "salary": 5, "skills": ["python", "excel"], "exp": 3},
]

# API + Scraper jobs
api_jobs = fetch_api_jobs(role) if role else []
scraped_jobs = scrape_jobs(role) if role else []

# Combine all jobs
all_jobs = jobs_data + api_jobs + scraped_jobs

# Filter + match
jobs = filter_jobs(all_jobs, user_skills, experience)

# -----------------------------
# DISPLAY JOBS
# -----------------------------
st.subheader("📋 Job Listings")

if jobs:
    for i, job in enumerate(jobs):
        st.write(f"### {job['title']} at {job['company']}")
        st.write(f"📍 {job['location']} | 💰 {job['salary']} LPA")
        st.write(f"🧠 Match Score: {job['match']}")

        # Company info
        st.info(get_company_info(job["company"]))

        # Save job
        if st.button("💾 Save Job", key=i):
            with connect_db() as conn:
                conn.execute(
                    "INSERT INTO jobs VALUES (NULL,?,?,?,?,?)",
                    (job["title"], job["company"], job["location"], str(job["salary"]), "Saved")
                )
            st.success("Job saved!")

        st.markdown("---")
else:
    st.warning("No jobs found")

# -----------------------------
# RESUME ANALYSIS
# -----------------------------
st.subheader("📄 Resume Analyzer")

job_desc = st.text_area("Paste Job Description")

file = st.file_uploader("Upload Resume", type=["pdf", "txt"])

if file:
    text = ""

    if file.type == "application/pdf":
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
    else:
        text = file.read().decode()

    score, found, missing, jd_missing, recs = analyze_resume(text, job_desc)

    st.progress(score / 100)
    st.write(f"🎯 ATS Score: {score}/100")

    st.write("✅ Skills Found:", found)
    st.write("❌ Missing Skills:", missing)
    st.write("📌 Missing from Job Description:", jd_missing)

    st.subheader("📚 Recommendations")
    for r in recs:
        st.write("👉", r)

# -----------------------------
# CHATBOT
# -----------------------------
st.subheader("🤖 Career Chatbot")

msg = st.text_input("Ask something...")

if msg:
    st.write("🤖:", chatbot_response(msg))

# -----------------------------
# JOB TRACKER
# -----------------------------
st.subheader("📊 Job Tracker")

conn = connect_db()
df = pd.read_sql("SELECT * FROM jobs", conn)

if not df.empty:
    for i, row in df.iterrows():
        st.write(f"### {row['title']} - {row['company']}")

        status = st.selectbox(
            "Application Status",
            ["Saved", "Applied", "Interview"],
            index=["Saved", "Applied", "Interview"].index(row["status"]) if row["status"] in ["Saved", "Applied", "Interview"] else 0,
            key=i
        )

        if st.button("Update Status", key=f"update_{i}"):
            conn.execute("UPDATE jobs SET status=? WHERE id=?", (status, row["id"]))
            conn.commit()
            st.success("Updated!")

        st.markdown("---")
else:
    st.info("No saved jobs yet")

conn.close()

# -----------------------------
# EXPORT
# -----------------------------
st.subheader("⬇ Export Data")

if st.button("Download CSV"):
    conn = connect_db()
    df = pd.read_sql("SELECT * FROM jobs", conn)
    conn.close()

    st.download_button("Download CSV", df.to_csv(index=False), "jobs.csv")

if st.button("Download PDF"):
    export_pdf(jobs)
    with open("jobs.pdf", "rb") as f:
        st.download_button("Download PDF", f, "jobs.pdf")