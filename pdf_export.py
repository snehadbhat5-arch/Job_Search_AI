from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def export_pdf(jobs):
    doc = SimpleDocTemplate("jobs.pdf")
    styles = getSampleStyleSheet()

    content = []

    for job in jobs:
        content.append(Paragraph(f"{job['title']} at {job['company']}", styles["Normal"]))

    doc.build(content)