from fpdf import FPDF


class PDFGenerator:
    def generate_pdf(self, results):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Add a title
        pdf.cell(200, 10, txt="Competition Results", ln=True, align="C")

        # Add table headers
        pdf.cell(40, 10, txt="Participant ID", border=1)
        pdf.cell(40, 10, txt="Start Time", border=1)
        pdf.cell(40, 10, txt="Finish Time", border=1)
        pdf.cell(40, 10, txt="Total Time", border=1)
        pdf.cell(40, 10, txt="Penalties", border=1)
        pdf.ln()

        # Add table rows
        for result in results:
            pdf.cell(40, 10, txt=str(result.participant_id), border=1)
            pdf.cell(40, 10, txt=str(result.start_time), border=1)
            pdf.cell(40, 10, txt=str(result.finish_time), border=1)
            pdf.cell(40, 10, txt=str(result.total_time), border=1)
            pdf.cell(40, 10, txt=str(result.penalties), border=1)
            pdf.ln()

        # Save PDF to a file
        pdf_path = "/tmp/results.pdf"
        pdf.output(pdf_path)

        return pdf_path
