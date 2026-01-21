import langextract as lx

def extract_medications(text, medication_list):
    """
    Extract medications from clinical text using a custom dictionary of known names.
    Demonstrates custom dictionary usage by including it in the prompt.
    """
    prompt = "Extract any medications mentioned. Known medications: " + ", ".join(medication_list) + "."
    examples = [
        lx.data.ExampleData(
            text=("The patient has been prescribed metformin and lisinopril for diabetes and "
                  "hypertension."),
            extractions=[
                lx.data.Extraction(extraction_class="medication", extraction_text="metformin"),
                lx.data.Extraction(extraction_class="medication", extraction_text="lisinopril")
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
        meds = [ex.extraction_text for ex in result.extractions if ex.extraction_class == "medication"]
        print("Medications found:", meds)
    except Exception as e:
        print(f"Error during medication extraction: {e}")

# Example usage:
known_meds = ["aspirin", "ibuprofen", "metformin", "lisinopril"]
clinical_note = "Patient reported taking aspirin daily. Also started metformin recently."
extract_medications(clinical_note, known_meds)
