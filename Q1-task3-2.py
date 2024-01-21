from transformers import AutoTokenizer
from collections import Counter

def read_text_file(file_path):
    """Read the content of a text file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def count_unique_tokens(text, tokenizer, top_n=30):
    """Count the occurrences of unique tokens in the text."""
    try:
        # Tokenize the text
        tokens = tokenizer.tokenize(text)
        
        # Count token occurrences
        token_counts = Counter(tokens)
        
        # Get the top N tokens
        top_tokens = token_counts.most_common(top_n)
        
        return top_tokens
    except Exception as e:
        print(f"Error counting tokens: {e}")
        return None

def main():
    # File path to the text file
    text_file_path = 'output/Q1-task1_output.txt'

    # Load the BioBERT tokenizer
    tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.2")

    # Read the text file
    text_content = read_text_file(text_file_path)

    if text_content is not None:
        # Count and retrieve top tokens
        top_tokens = count_unique_tokens(text_content, tokenizer, top_n=30)

        if top_tokens is not None:
            # Display the top tokens and their counts
            for token, count in top_tokens:
                print(f"Token: {token}, Count: {count}")

if __name__ == "__main__":
    main()
