import langextract as lx

def extract_named_entities(text):
    """Extract person and organization names from text using LangExtract."""
    prompt = "Extract all person and organization names mentioned in the text."
    examples = [
        lx.data.ExampleData(
            text="Barack Obama met with Microsoft executives in 2021.",
            extractions=[
                lx.data.Extraction(extraction_class="person",    extraction_text="Barack Obama"),
                lx.data.Extraction(extraction_class="organization", extraction_text="Microsoft"),
            ]
        )
    ]
    try:
        result = lx.extract(
            text_or_documents=text,
            prompt_description=prompt,
            examples=examples,
            model_id="gemini-2.5-flash"   # use Google Gemini LLM
        )
        for ex in result.extractions:
            print(f"Class: {ex.extraction_class}, Text: {ex.extraction_text}")
    except Exception as e:
        print(f"Error during extraction: {e}")

# Example usage:
text = ("Barack Obama was born in Hawaii and later worked with Microsoft. "
        "Michelle Obama founded a non-profit organization called 'When We All Vote'.")
extract_named_entities(text)
