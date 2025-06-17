# 🤖 PDF Form Filler with Gemini AI

Fill out PDF forms effortlessly with the help of Google's **Gemini AI**! This tool uses AI to ask you intelligent, polite questions in your preferred language, then fills in PDF forms based on your responses. Perfect for making form-filling faster, friendlier, and multilingual.

---

## ✨ Features

- ✅ Automatically detects and processes form fields in PDFs
- 🌍 Multilingual support (e.g., English, Spanish, Hindi, French...)
- 🤖 AI-generated questions via Gemini for each field
- 📝 Supports text fields, checkboxes, and dropdowns
- 💾 Saves your completed PDF with all inputs

---

## 📦 Requirements

Install dependencies using pip:

```bash
pip install -r requirements.txt
````

---

## 🚀 Usage

Run the program from the command line:

```bash
python -m fillform
```

You’ll be prompted to:

1. Enter the path to your input PDF
2. Choose a name for the output PDF
3. Select your preferred language
4. Answer the AI-generated questions to fill in the form

---

## 🧠 How It Works

1. Loads your PDF and scans for form fields
2. Uses [Gemini 1.5 Flash](https://ai.google.dev/) to generate human-like prompts
3. Interacts with you via CLI to gather responses
4. Fills the PDF with your answers and saves the final file

---

## 🔐 Configuration

Your API key and model name are stored in `config.py`:

```python
GEMINI_API_KEY = 'your-api-key-here'
GEMINI_MODEL = 'gemini-1.5-flash'
```

> 💡 For security, consider loading your API key from environment variables or a secrets manager in production.

---

## 🗂️ Project Structure

```
fillform/
├── __main__.py          # Entry point
├── config.py            # API config
├── gemini_helper.py     # Gemini integration
├── pdf_filler.py        # Core logic for PDF filling
└── requirements.txt     # Python dependencies
```

---

## 🙌 Contributing

Pull requests are welcome! If you have ideas to improve multilingual support, field detection, or UI/UX, feel free to contribute.

---


---

## 💬 Example Output

```
📄 Enter path to the input PDF: form.pdf
💾 Output PDF file name: filled_form.pdf
🌐 Preferred language (e.g., en, es, hi, fr): es

🤖 Gemini will ask you questions to fill in the form fields...

📝 Por favor, proporcione su nombre completo.
> Juan Pérez

☑️ ¿Debe marcarse la casilla 'Acepta los términos'? (sí/no)
> sí

✅ PDF filled and saved to: filled_form.pdf
```

---

## 🌟 Why You'll Love It

* No manual editing of PDF fields
* Works with any AcroForm-compatible PDF
* Gemini handles the prompting for you — just respond naturally!

---

Happy automating! 🤖📄✨

```

---

Let me know if you'd like badges, a logo, or a version that includes screenshots!
```
# pdf-form-filler-chatbot
