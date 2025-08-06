import fitz

doc = fitz.open("enem2024.pdf")

print(f"Número de páginas: {len(doc)}")
print(f"Metadados: {doc.metadata}")
print(f"Título do documento: {doc.metadata.get('title')}")

for i, page in enumerate(doc):
    text = page.get_text()
    print(f"\n--- Página {i + 1} ---\n")
    print(text)
