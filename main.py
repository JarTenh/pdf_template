import pandas as pd
from fpdf import FPDF


# Create a PDF instance.
pdf = FPDF()
pdf.set_auto_page_break(auto=False, margin=0)

# Read the dataframe containing the page information.
df = pd.read_csv("topics.csv")

# Go through the dataframe and create pages according the data.
for index, row in df.iterrows():
    pdf.add_page()

    # Set the header.
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 21, 200, 21)

    # Add horizontal lines.
    for y in range(30, 298, 10):
        pdf.cell(w=0, h=10, txt=" ")
        pdf.line(10, y, 200, y)

    # Add footer.
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    # Create blank pages, as stated in the data.
    for _ in range(row["Pages"] - 1):
        pdf.add_page()

        # Add horizontal lines.
        for y in range(20, 298, 10):
            pdf.cell(w=0, h=10, txt=" ")
            pdf.line(10, y, 200, y)

        # Add blank lines.
        pdf.ln(277)

        # Add footer.
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")
