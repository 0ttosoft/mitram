from llama_index.core.schema import Document

doc = Document(text="test")
print(dir(doc))
try:
    doc.text = "new text"
except Exception as e:
    print(f"Error setting text: {e}")

if hasattr(doc, "set_content"):
    print("Has set_content")
    
print(f"Doc text: {doc.text}")
