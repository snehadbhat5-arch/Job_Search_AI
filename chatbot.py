def chatbot_response(user_input):
    user_input = user_input.lower()

    if "job" in user_input:
        return "Search roles like Python Developer or Data Analyst."
    elif "resume" in user_input:
        return "Upload your resume to get ATS score and suggestions."
    elif "skills" in user_input:
        return "Focus on Python, SQL, and Machine Learning."
    else:
        return "I can help with jobs, resume, and career advice!"