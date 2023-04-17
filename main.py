import pandas as pd
from fpdf import FPDF


# Create a PDF instance.
pdf = FPDF()

# Read the dataframe containing the page information.
df = pd.read_csv("topics.csv")

# Go through the dataframe and create pages according the data.
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=1)
    pdf.line(10, 21, 200, 21)

    # Create blank pages, as stated in the data.
    for _ in range(row["Pages"] - 1):
        pdf.add_page()

pdf.output("output.pdf")
