from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import NameObject, TextStringObject
from gemini_helper import generate_question


def fill_pdf(input_pdf: str, output_pdf: str, model, lang: str = "en") -> None:
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    fields = reader.get_fields()
    filled_data = {}

    print(f"\n🌍 Language set to: {lang}")
    print("🤖 Gemini will ask you questions to fill in the form fields...\n")

    for field_name, field_data in fields.items():
        field_type = field_data.get("/FT")
        pretty_name = field_data.get("/TU", field_name)

        if field_type == "/Tx":
            question = generate_question(model, pretty_name, lang)
            user_input = input(f"📝 {question}\n> ").strip()
            filled_data[field_name] = TextStringObject(user_input)

        elif field_type == "/Btn":
            question = generate_question(
                model, f"Should the checkbox '{pretty_name}' be checked? (yes/no)", lang
            )
            user_input = input(f"☑️ {question}\n> ").strip().lower()
            filled_data[field_name] = (
                NameObject("/Yes")
                if user_input in ["yes", "y", "sí", "si", "oui"]
                else NameObject("/Off")
            )

        elif field_type == "/Ch":
            options = field_data.get("/Opt", [])
            if isinstance(options[0], list):
                options = [opt[0] for opt in options]
            question = generate_question(
                model, f"Choose one for '{pretty_name}': {options}", lang
            )
            print(f"🔽 {question}")
            print("Options:", options)
            user_input = input("> ").strip()
            filled_data[field_name] = TextStringObject(
                user_input if user_input in options else options[0]
            )

        else:
            print(
                f"⚠️ Skipping unsupported field type '{field_type}' for '{field_name}'"
            )

    writer.update_page_form_field_values(writer.pages[0], filled_data)

    with open(output_pdf, "wb") as f:
        writer.write(f)

    print(f"\n✅ PDF filled and saved to: {output_pdf}")
