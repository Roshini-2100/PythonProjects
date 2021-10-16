from fpdf import FPDF

pdf = FPDF()

pdf.add_page()

pdf.set_font("Arial", size=15)

fd = open("Sample.txt", "r")
for i in fd:
    pdf.cell(200, 10, txt=i, ln=1, align="C")

pdf.output("test.pdf")
print("successfully PDF Created:")
