import requests
from bs4 import BeautifulSoup

def scrape_jobs(role):
    try:
        url = f"https://remoteok.com/remote-{role}-jobs"
        headers = {"User-Agent": "Mozilla/5.0"}

        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")

        jobs = []

        for job in soup.select("tr.job")[:5]:
            title = job.get("data-position")
            company = job.get("data-company")

            if title:
                jobs.append({
                    "title": title,
                    "company": company or "Unknown",
                    "location": "Remote",
                    "salary": 6,
                    "skills": ["python"],
                    "exp": 2
                })

        return jobs

    except:
        return []