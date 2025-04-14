from datetime import datetime
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class ReportWriter:
    def __init__(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.report_path = os.path.join("reports", f"report_{timestamp}.txt")
        self.pdf_path = os.path.join("reports", f"report_{timestamp}.pdf")
        self.html_path = os.path.join("reports", f"report_{timestamp}.html")

    def generate_report(self, results):
        with open(self.report_path, "w") as f:
            f.write("BreakerZero Attack Report\n")
            f.write("="*40 + "\n")
            for item in results:
                f.write(f"- {item}\n")
        print(f"[+] Text report saved to {self.report_path}")

    def generate_pdf(self, results):
        c = canvas.Canvas(self.pdf_path, pagesize=letter)
        c.drawString(100, 750, "BreakerZero Attack Report")
        y = 730
        for item in results:
            c.drawString(100, y, f"- {item}")
            y -= 20
        c.save()
        print(f"[+] PDF report saved to {self.pdf_path}")

    def generate_html(self, results):
        with open(self.html_path, "w") as f:
            f.write("<html><head><title>BreakerZero Report</title></head><body>")
            f.write("<h1>BreakerZero Attack Report</h1><ul>")
            for item in results:
                f.write(f"<li>{item}</li>")
            f.write("</ul></body></html>")
        print(f"[+] HTML report saved to {self.html_path}")
