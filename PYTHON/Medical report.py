from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import matplotlib.pyplot as plt
import io


def create_medical_report(output_file, patient_data):
    doc = SimpleDocTemplate(output_file, pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'Title',
        parent=styles['Heading1'],
        fontSize=14,
        textColor=colors.black,
        alignment=1,
        backColor=colors.lightgreen, 
        spaceBefore=10,
        spaceAfter=10,
    )
    header_style = ParagraphStyle(
        'Header',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.black,
        alignment=1,
        backColor=colors.lightgreen,  
    )

    company_info = """
    <h1>Helixify x Clinico Labs</h1><br/>
    1234 Lab Street, City, Country<br/>
    Phone: +1 (123) 456-7890 | Email: email@helixify.com
    """
    elements.append(Paragraph(company_info, title_style))
    elements.append(Spacer(1, 0.25*inch))

    elements.append(Paragraph("Patient Demographics", header_style))
    elements.append(Spacer(1, 0.1*inch))
    data = [
        ["Name", patient_data['name'], "Gender", patient_data['gender']],
        ["Patient ID", patient_data['id'], "Date of Birth", patient_data['dob']],
        ["Phone no.", patient_data['phone'], "Nationality", patient_data['nationality']]
    ]
    table = Table(data, colWidths=[1.5*inch, 2*inch, 1.5*inch, 2*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.lightgreen), 
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('BACKGROUND', (1, 0), (-1, -1), colors.white),
        ('TEXTCOLOR', (1, 0), (-1, -1), colors.black),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    elements.append(table)
    elements.append(Spacer(1, 0.25*inch))

    data = [
        ["Admission Date / Time", patient_data['admission_time']],
        ["Disease Prediction", patient_data['disease_prediction']],
        ["Drug Recommendations", patient_data['drug_recommendations']],
        ["Lifestyle Recommendations", patient_data['lifestyle_recommendations']]
    ]
    table = Table(data, colWidths=[3*inch, 4*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgreen),  
        ('TEXTCOLOR', (0, 0), (0, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('BACKGROUND', (1, 0), (-1, -1), colors.white),
        ('TEXTCOLOR', (1, 0), (-1, -1), colors.black),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    elements.append(table)

    elements.append(Spacer(1, 0.5*inch))

    add_graphs(elements, patient_data)

    disclaimer = "Disclaimer: The information provided in this report is accurate based on the data available at the time of generation."
    elements.append(Paragraph(disclaimer, styles['Normal']))

    contact_info = "Contact: email@helixify.com |<br/> Phone: +1 (123) 456-7890"
    elements.append(Paragraph(contact_info, styles['Normal']))

    doc.build(elements)

def add_graphs(elements, patient_data):
    # Bar chart data (Example values)
    diseases = ['Disease Prediction', 'Drug Recommendations', 'Lifestyle Recommendations']
    values = [60, 80, 90]

    fig, ax = plt.subplots()
    ax.bar(diseases, values, color='lightgreen')
    ax.set_ylabel('Score')
    ax.set_title('Health Overview')

    buf_bar = io.BytesIO()
    plt.savefig(buf_bar, format='png')
    buf_bar.seek(0)

    img_bar = Image(buf_bar, width=5*inch, height=3*inch)
    elements.append(img_bar)

    plt.close(fig)

    fig, ax = plt.subplots()
    pie_values = [30, 50, 20]
    pie_labels = ['Low Risk', 'Moderate Risk', 'High Risk']
    ax.pie(pie_values, labels=pie_labels, colors=['lightgreen', 'green', '#024b30'], autopct='%1.1f%%', startangle=140)
    ax.set_title('Risk Distribution')

    buf_pie = io.BytesIO()
    plt.savefig(buf_pie, format='png')
    buf_pie.seek(0)

    img_pie = Image(buf_pie, width=5*inch, height=3*inch)
    elements.append(img_pie)

patient_data = {
    'name': 'Celeste Lim',
    'gender': 'Female',
    'id': '1234565',
    'dob': 'March 9, 2015',
    'phone': '+91 568345947',
    'nationality': 'Filipino',
    'admission_time': 'September 8, 2021 / 22:00H',
    'disease_prediction': 'Example disease prediction',
    'drug_recommendations': 'Example drug recommendations',
    'lifestyle_recommendations': 'Example lifestyle recommendations'
}

create_medical_report('personalized_medical_report.pdf', patient_data)