from cover_letter_generator import generate_cover_letter
from docx import Document

def read_text_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def save_to_docx(text, filename):
    doc = Document()
    doc.add_paragraph(text)
    doc.save(filename)

if __name__ == "__main__":
    resume_text = "Mark Bowman, Business Analyst..."  # Replace with resume parser if needed
    job_text = read_text_file("job_description.txt")

    print("🔧 Generating cover letter...")
    letter = generate_cover_letter(job_text, resume_text)

    print("💾 Saving cover letter to cover_letter.docx")
    save_to_docx(letter, "cover_letter.docx")
    print("✅ Done.")
