from fpdf import FPDF

def crea_pdf(contenuto, nome_file="output.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, contenuto)
    pdf.output(nome_file)
    print(f"\n PDF creato: {nome_file}")

if __name__ == "__main__":
    print(" Inserisci il testo da inserire nel PDF (premere due volte invio per terminare):\n")


    righe = []
    while True:
        riga = input()
        if riga == "":
            break
        righe.append(riga)

    contenuto = "\n".join(righe)

    nome_file = input("\n Inserisci il nome del file PDF da salvare senza estensione .pdf\n")
    if not  nome_file.endswith(".pdf"):
        nome_file += ".pdf"

crea_pdf(contenuto, nome_file)