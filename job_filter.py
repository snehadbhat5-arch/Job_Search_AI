def filter_jobs(jobs, user_skills, experience):
    filtered = []

    for job in jobs:
        if experience == "0-2" and job.get("exp", 1) > 2:
            continue
        elif experience == "2-5" and not (2 <= job.get("exp", 3) <= 5):
            continue
        elif experience == "5+" and job.get("exp", 5) < 5:
            continue

        job["match"] = sum(1 for s in user_skills if s in job["skills"])
        filtered.append(job)

    return sorted(filtered, key=lambda x: x["match"], reverse=True)