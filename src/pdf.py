
# Functions related to exporting the report output to a PDF file:

def createPDF(state, textpdf):
    print('\nOne moment, please, a pdf report is being created...')
    from fpdf import FPDF
    pdf = FPDF()
    pdf.add_page()
    # pdf.set_xy(0, 0)
    pdf.image('./images/michelin_2.png',w=190)
    pdf.ln(10)
    pdf.image('./images/michelin_petit.png',w=190)
    pdf.set_font('Arial', '', 12)
    text=textpdf
    pdf.multi_cell(0, 10, text, align='L')
    pdf.ln(10)
    pdf.image('./images/red.png',w=190)
    pdf.set_font('Arial', 'B', 18)
    pdf.cell(0, -12, 'Michelin restaurants in {}:'.format(state), align='C')
    pdf.ln(15)
    pdf.set_font('Arial', '', 12)
    text='The following pie chart classifies restaurants according to their number of Michelin stars:'
    pdf.cell(0, 0, text, align='L')
    pdf.ln(15)
    pdf.image('./output/piechart_stars_{}.png'.format(state),w=150)
    pdf.ln(15)
    pdf.add_page()
    pdf.image('./images/michelin_2.png',w=190)
    pdf.ln(15)
    pdf.set_font('Arial', '', 12)
    text='The following pie chart classifies restaurants according to their type of cuisine:'
    pdf.cell(0, 0, text, align='L')
    pdf.ln(15)
    pdf.image('./output/piechart_cuisine_{}.png'.format(state),w=150)
    pdf.output('./output/PieChart-{}.pdf'.format(state), 'F')




'''
OLD VERSION

def createPDF(state, typechart):
    # typechart = 'cuisine'
    # typechart = 'stars'
    print('\nOne moment, please, a pdf report is being created...')
    from fpdf import FPDF
    if typechart == 'cuisine':
        sentence = 'type of cuisine'
    elif typechart == 'stars':
        sentence = 'number of Michelin stars'
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font('Arial', 'B', 16)
    pdf.multi_cell(0, 10, 'Michelin restaurants in {}'.format(state), align='C')
    pdf.ln(10)

    pdf.set_font('Arial', '', 12)
    text='The following pie chart classifies restaurants according to their {}.'.format(sentence)
    pdf.multi_cell(0, 5, text.format(state,typechart),align='L')
    pdf.ln(10)

    pdf.image('./output/piechart_{}.png'.format(typechart)) # ,w=150,h=100
    pdf.output('./output/PieChart-{}-{}.pdf'.format(state,typechart), 'F')
'''
