from pypdf import PdfWriter

merger = PdfWriter()

for pdf in ["Internet_Speed_Test_Location_A.pdf", "Internet_Speed_Test_Location_B.pdf", "Internet_Speed_Test_Location_C.pdf"]:
    merger.append(pdf)

merger.write("Merged-pdf.pdf")
merger.close()