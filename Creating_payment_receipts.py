# Importing required modules
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# Data in the form of a list of lists
data = [
    ['Name', 'Amount', 'Date'],
    ['John Doe', '$100', '2022-01-01'],
    ['Jane Smith', '$200', '2022-01-02'],
    ['Mike Johnson', '$150', '2022-01-03']
]

# Creating a simple doc template with A4 paper size
doc = SimpleDocTemplate("payment_receipts.pdf", pagesize=A4)


# Getting a sample style sheet and adding styling
styles = getSampleStyleSheet()
style_table = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 12),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 10),
    ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
])

# Creating a table object with data and style
table = Table(data)
table.setStyle(style_table)

# Building the PDF document
elements = []
elements.append(table)
doc.build(elements)
