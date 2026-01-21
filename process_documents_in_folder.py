import langextract as lx
import os

def process_documents_in_folder(folder_path, prompt, example):
    """
    Run LangExtract on all .txt files in a folder, emulating a content pipeline.
    Aggregates results into a list of dicts for further processing or indexing.
    """
    aggregated = []
    for fname in os.listdir(folder_path):
        if not fname.lower().endswith(".txt"):
            continue
        fpath = os.path.join(folder_path, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        try:
            result = lx.extract(
                text_or_documents=content,
                prompt_description=prompt,
                examples=[example],
                model_id="gemini-2.5-flash"
            )
            for ex in result.extractions:
                aggregated.append({
                    "document": fname,
                    "class": ex.extraction_class,
                    "text": ex.extraction_text
                })
        except Exception as e:
            print(f"Failed to extract from {fname}: {e}")
    return aggregated

# Define the task: extract names and dates from contract texts
prompt = "Extract client names and contract dates from the contract text."
example = lx.data.ExampleData(
    text=("This contract is between Alice Smith (signed on January 1, 2023) "
          "and Bob Jones (signed on February 5, 2023)."),
    extractions=[
        lx.data.Extraction(extraction_class="client", extraction_text="Alice Smith"),
        lx.data.Extraction(extraction_class="date",   extraction_text="January 1, 2023"),
        lx.data.Extraction(extraction_class="client", extraction_text="Bob Jones"),
        lx.data.Extraction(extraction_class="date",   extraction_text="February 5, 2023")
    ]
)

# Process all contracts in the 'contracts' folder
results = process_documents_in_folder("contracts", prompt, example)
for row in results:
    print(row)
