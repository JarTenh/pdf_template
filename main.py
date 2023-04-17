from fpdf import FPDF


pdf = FPDF()

pdf.add_page()

pdf.set_font(family="Times", style="B", size=12)
pdf.cell(w=0, h=12, txt="Hello there!", align="L", ln=1, border=1)
pdf.cell(w=0, h=12, txt="Hi there!", align="L", ln=1, border=1)

pdf.output("output.pdf")
