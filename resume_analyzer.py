def analyze_resume(text, job_desc=""):
    keywords = ["python", "sql", "ml", "excel", "java", "c++", "html", "css", "javascript"]

    text = text.lower()
    job_desc = job_desc.lower()

    found = [k for k in keywords if k in text]
    missing = [k for k in keywords if k not in text]

    score = int((len(found) / len(keywords)) * 100)

    jd_keywords = [k for k in keywords if k in job_desc]
    jd_missing = [k for k in jd_keywords if k not in text]

    learning_map = {
        "python": "Learn Python (Coursera/Udemy)",
        "sql": "Practice SQL (LeetCode)",
        "ml": "Machine Learning course",
        "excel": "Excel for Data Analysis"
    }

    recommendations = [learning_map.get(skill, f"Learn {skill}") for skill in missing]

    return score, found, missing, jd_missing, recommendations