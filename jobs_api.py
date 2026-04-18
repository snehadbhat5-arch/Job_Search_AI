import requests

def fetch_api_jobs(role):
    try:
        url = f"https://remotive.com/api/remote-jobs?search={role}"
        res = requests.get(url, timeout=5)
        res.raise_for_status()

        data = res.json()

        return [{
            "title": j["title"],
            "company": j["company_name"],
            "location": "Remote",
            "salary": 8,
            "skills": ["python"],
            "exp": 2
        } for j in data.get("jobs", [])[:5]]

    except:
        return []