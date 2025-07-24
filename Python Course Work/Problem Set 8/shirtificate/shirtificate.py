from fpdf import FPDF

def main():
    make_shirt(input("Name: ").title().strip())

def make_shirt(name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", style="B", size=40)
    pdf.cell(0, 50, "CS50 Shirtificate", align="C")
    pdf.image("shirtificate.png", w=190, h=190, x=9, y=70)
    pdf.set_font("helvetica", size=24)
    page_width = pdf.w
    text_width = pdf.get_string_width(f"{name} took CS50")
    x = (page_width - text_width) / 2
    y = 130
    pdf.set_text_color(255, 255, 255)
    pdf.text(x, y, f"{name} took CS50")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()

