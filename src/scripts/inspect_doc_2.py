from llama_index.core.schema import Document

doc = Document(text="test\x00")
print(f"Original: {doc.text.encode('utf-8')}")

if hasattr(doc, "set_content"):
    doc.set_content(doc.text.replace("\x00", ""))
    print(f"Modified: {doc.text.encode('utf-8')}")
else:
    print("No set_content")
