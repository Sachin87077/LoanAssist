from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

def generate_pdf(context):
    os.makedirs("outputs/sanction_letters", exist_ok=True)
    path = "outputs/sanction_letters/sanction_demo.pdf"

    c = canvas.Canvas(path, pagesize=A4)
    c.drawString(100, 750, "Loan Sanction Letter")
    c.drawString(100, 720, f"Amount: {context['loan_amount']}")
    c.drawString(100, 700, f"Tenure: {context['tenure']} months")
    c.drawString(100, 680, f"EMI: {context.get('emi')}")
    c.save()

    return path
