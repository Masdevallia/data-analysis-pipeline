
# Functions related to exporting the report output to a PDF file:

def createPDF(state, typechart):
    '''
    typechart = 'cuisine'
    typechart = 'stars'
    '''
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
    pdf.image('./output/piechart_{}.png'.format(typechart),w=150,h=100)
    pdf.output('./output/PieChart-{}-{}.pdf'.format(state,typechart), 'F')

