from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import os

def create_resume_pdf(filename):
    doc = SimpleDocTemplate(filename, pagesize=letter,
                            rightMargin=0.5*inch, leftMargin=0.5*inch,
                            topMargin=0.5*inch, bottomMargin=0.5*inch)
    elements = []

    # Define styles
    styles = getSampleStyleSheet()
    styles['Heading1'].fontSize = 20
    styles['Heading1'].textColor = colors.darkblue
    styles['Heading1'].spaceAfter = 8

    styles['Heading2'].fontSize = 16
    styles['Heading2'].textColor = colors.darkblue
    styles['Heading2'].spaceBefore = 14
    styles['Heading2'].spaceAfter = 8

    styles['Normal'].fontSize = 10
    styles['Normal'].leading = 14

    styles['Bullet'].fontSize = 10
    styles['Bullet'].leading = 14
    styles['Bullet'].leftIndent = 20
    styles['Bullet'].bulletIndent = 10

    styles.add(ParagraphStyle(name='Footer', parent=styles['Normal'], fontSize=8, textColor=colors.gray))

    # Header
    elements.append(Paragraph('Nigel van der Laan', styles['Heading1']))
    elements.append(Paragraph('Amsterdam/Valencia | mtbasesix@gmail.com | www.arqnxs.com', styles['Normal']))
    elements.append(Spacer(1, 12))

    # Professional Summary
    elements.append(Paragraph('Professional Summary', styles['Heading2']))
    elements.append(Paragraph('Dynamic and solution-oriented Business & Research Strategic Leader with over 7 years of experience in AI and Machine Learning. Proven track record in leveraging data-driven insights to drive business improvement and optimize overall performance. Excel at bridging the gap between technical and non-technical stakeholders, fostering innovation.', styles['Normal']))

    # Core Competencies
    elements.append(Paragraph('Core Competencies', styles['Heading2']))
    competencies = [
        'AI/ML Development', 'Data Analytics', 'Full-Stack Development', 'Team Leadership',
        'Strategic Planning', 'FinTech & Blockchain', 'Problem Solving', 'Agile Methodologies'
    ]
    comp_text = ' • '.join(competencies)
    elements.append(Paragraph(comp_text, styles['Normal']))

    # Technical Skills
    elements.append(Paragraph('Technical Skills', styles['Heading2']))
    skills = 'Python, R, JavaScript, SQL, SPARQL, Keras/TensorFlow, PyTorch, FastAPI, Django, React, Git, Azure, Elastic Cloud, PostgreSQL, Linux, Solidity, Rust, Pandas, NumPy, Matplotlib, Seaborn, Flask, Pine, Moralis, Chainlink, ATAS/EXO'
    elements.append(Paragraph(skills, styles['Normal']))

    # GitHub Repositories
    elements.append(Paragraph('GitHub Repositories', styles['Heading2']))
    github_repos = [
        ('https://github.com/ARQNXS', 'ARQNXS - Personal projects and collaborative work'),
        ('https://github.com/NKVDL/jupyter_notes', 'Jupyter Notes - Collection of data science and machine learning notebooks')
    ]
    for repo_url, repo_desc in github_repos:
        elements.append(Paragraph(f'<b>{repo_url}</b>', styles['Normal']))
        elements.append(Paragraph(repo_desc, styles['Normal']))
        elements.append(Spacer(1, 6))

    # Professional Experience
    elements.append(Paragraph('Professional Experience', styles['Heading2']))
    experiences = [
        ('ARQNXS, Amsterdam - Founder & AI Solutions Architect', 'July 2017 - Present', [
            'Developed an AI-powered procurement platform, increasing search efficiency by 800%',
            'Engineered ML-driven chatbots capable of handling 1M requests/minute',
            'Created an intelligent trading application with advanced risk management features',
            'Implemented NLP solutions for educational platforms, achieving 95% accuracy in MCQ responses',
            'Designed and deployed multi-instrumental ML-powered trading systems'
        ]),
        ('Dutch Government, Apeldoorn - Information Analyst', 'Oct 2022 - Sept 2023', [
            'Led a high-performing development team, delivering innovative solutions',
            'Optimized operations through Python script refinement and SPARQL query validation',
            'Implemented DevOps practices using GitLab and YAML'
        ]),
        ('Sintryx, Amsterdam - Chief Technology Officer', 'Oct 2021 - Sept 2022', [
            'Conceptualized and developed a high-performing FinTech platform',
            'Led a team of 13 to successfully deliver an NFT Marketplace and DEX',
            'Raised $600k in 10 days through strategic pitching and presentation'
        ]),
        ('GMU, Meppel - Senior Python Developer', 'May 2021 - Dec 2021', [
            'Spearheaded the development of ML/DL models for financial analysis',
            'Created a GUI-integrated bot for crypto trading',
            'Managed a $100k fund portfolio, optimizing allocation strategies'
        ])
    ]

    for job_title, duration, responsibilities in experiences:
        job_table = Table([
            [Paragraph(f'<b>{job_title}</b>', styles['Normal']), Paragraph(duration, styles['Normal'])],
        ], colWidths=[5*inch, 2*inch])
        job_table.setStyle(TableStyle([
            ('ALIGN', (0,0), (0,0), 'LEFT'),
            ('ALIGN', (1,0), (1,0), 'RIGHT'),
        ]))
        elements.append(job_table)
        for resp in responsibilities:
            elements.append(Paragraph(f'• {resp}', styles['Bullet']))
        elements.append(Spacer(1, 6))

    # Education
    elements.append(Paragraph('Education', styles['Heading2']))
    education = [
        ('Vrije Universiteit, Amsterdam', 'MSc in Genes in Behaviour and Health (Partial)', 'Sept 2020 - Mar 2021'),
        ('Vrije Universiteit, Amsterdam', 'MSc in Neuroscience (Partial)', 'Sept 2016 - Mar 2017'),
        ('Vrije Universiteit, Amsterdam', 'BSc in Biological Psychology', 'Sept 2013 - Jun 2016')
    ]
    for school, degree, duration in education:
        edu_table = Table([
            [Paragraph(f'<b>{school}</b>', styles['Normal']), Paragraph(duration, styles['Normal'])],
            [Paragraph(degree, styles['Normal']), ''],
        ], colWidths=[5*inch, 2*inch])
        edu_table.setStyle(TableStyle([
            ('ALIGN', (0,0), (0,1), 'LEFT'),
            ('ALIGN', (1,0), (1,1), 'RIGHT'),
        ]))
        elements.append(edu_table)
        elements.append(Spacer(1, 6))

    # Languages
    elements.append(Paragraph('Languages', styles['Heading2']))
    elements.append(Paragraph('Fluent in Dutch and English; Conversational Spanish', styles['Normal']))

    # Significant Achievements
    elements.append(Paragraph('Significant Achievements', styles['Heading2']))
    achievements = [
        'Pioneered AI-driven solutions increasing procurement efficiency by 800%',
        'Developed ML models handling 1M requests/minute for real-time sentiment analysis',
        'Successfully raised $600k in seed funding for a FinTech startup',
        'Led the delivery of innovative blockchain solutions including NFT marketplace and DEX',
        'Developed advanced software solution with 95% accuracy in educational MCQ responses',
        'Engineered intelligent "trade brain" for enhanced trading app functionality',
        'Created full-stack GUI sentiment analyzer for real-time speech recognition',
        'Implemented liquidity pool solvent algorithm for DeFi environment',
        'Authored in-depth technical paper on FinTech and blockchain technologies'
    ]
    for achievement in achievements:
        elements.append(Paragraph(f'• {achievement}', styles['Bullet']))

    # Footer
    elements.append(Spacer(1, 20))
    elements.append(Paragraph('This resume was generated using an algorithm. The script can be found at https://github.com/ARQNXS/Resume_Creator', styles['Footer']))

    # Build the PDF
    doc.build(elements)

# Call the function
create_resume_pdf('Nigel_van_der_Laan_Resume.pdf')
# Get the absolute path of the created PDF
pdf_path = os.path.abspath('Nigel_van_der_Laan_Resume.pdf')

print(f"Resume PDF has been created successfully!")
print(f"The PDF is saved at: {pdf_path}")