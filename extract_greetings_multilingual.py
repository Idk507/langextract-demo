import langextract as lx

def extract_greetings_multilingual(text):
    """Extract greeting phrases and identify their language."""
    prompt = "Extract greeting phrases from the text and label each with its language."
    examples = [
        lx.data.ExampleData(
            text="Hello! ¡Hola! Bonjour!",
            extractions=[
                lx.data.Extraction(extraction_class="greeting", extraction_text="Hello", attributes={"language": "English"}),
                lx.data.Extraction(extraction_class="greeting", extraction_text="¡Hola!", attributes={"language": "Spanish"}),
                lx.data.Extraction(extraction_class="greeting", extraction_text="Bonjour", attributes={"language": "French"}),
            ]
        )
    ]
    try:
        result = lx.extract(
            text_or_documents=text,
            prompt_description=prompt,
            examples=examples,
            model_id="gemini-2.5-flash"
        )
        for ex in result.extractions:
            lang = ex.attributes.get("language", "unknown")
            print(f"Greeting: '{ex.extraction_text}', Language: {lang}")
    except Exception as e:
        print(f"Error during multilingual extraction: {e}")

# Example usage:
text = "Bonjour, how are you? ¡Hola, cómo estás?"
extract_greetings_multilingual(text)
