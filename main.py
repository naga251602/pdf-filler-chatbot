import os
from dotenv import load_dotenv
from gemini_helper import configure_gemini
from pdf_filler import fill_pdf


def main():
    load_dotenv()
    input_pdf = input("📄 Enter path to the input PDF: ").strip()
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GEMINI_MODEL = os.getenv("GEMINI_MODEL")

    while not os.path.isfile(input_pdf):
        input_pdf = input("❌ File not found. Please re-enter: ").strip()

    output_pdf = input("💾 Output PDF file name: ").strip()
    if not output_pdf.endswith(".pdf"):
        output_pdf += ".pdf"

    lang = input("🌐 Preferred language (e.g., en, es, hi, fr): ").strip() or "en"

    model = configure_gemini(GEMINI_API_KEY, GEMINI_MODEL)
    fill_pdf(input_pdf, output_pdf, model, lang)


if __name__ == "__main__":
    main()
