from utils.pdf_generator import generate_pdf

class SanctionAgent:
    def generate(self, context: dict):
        return generate_pdf(context)
