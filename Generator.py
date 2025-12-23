# pdf_report_generator.py
# Simple PDF Report Generator using reportlab

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

def generate_pdf(filename, title, data):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    # Title
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(width / 2, height - 50, title)

    # Date
    c.setFont("Helvetica", 10)
    c.drawRightString(width - 40, height - 80, f"Date: {datetime.now().date()}")

    # Content
    y = height - 130
    c.setFont("Helvetica", 12)

    for key, value in data.items():
        c.drawString(50, y, f"{key}: {value}")
        y -= 25

    c.save()
    print("PDF report generated successfully.")

if __name__ == "__main__":
    report_data = {
        "Name": "Divya Reddy",
        "Department": "CSE (Data Science)",
        "Project": "PDF Report Generator",
        "Status": "Completed"
    }

    generate_pdf(
        "report.pdf",
        "Student Project Report",
        report_data
    )
