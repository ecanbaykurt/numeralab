from fpdf import FPDF

def generate_report(equation, method, result_text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="NumeraLab - Numerical Analysis Report", ln=True, align='C')
    pdf.ln(10)
    pdf.multi_cell(0, 10, f"Equation: {equation}\n\nMethod: {method}\n\nResult:\n{result_text}")
    pdf.output("numeralab_report.pdf")
    return "numeralab_report.pdf"
