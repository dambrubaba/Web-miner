import re
import json
import nltk
from typing import Dict, List
from nltk.tokenize import sent_tokenize

# Initialize NLTK at module level
def initialize_nltk():
    """Initialize NLTK and download required data."""
    try:
        # Force download of punkt data
        nltk.download('punkt', quiet=True)
    except Exception as e:
        print(f"Failed to download NLTK data: {str(e)}")

# Call initialization when module is loaded
initialize_nltk()

def simple_sentence_tokenize(text: str) -> List[str]:
    """Fallback sentence tokenizer using simple rules."""
    # Split on common sentence endings
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in sentences if s.strip()]

def validate_url(url: str) -> bool:
    """Validate if the input string is a valid URL."""
    url_pattern = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url_pattern.match(url) is not None

def structure_text_content(text: str) -> Dict:
    """Convert extracted text into structured format."""
    if not text:
        return {"error": "No content found"}

    # Split into sentences with fallback
    try:
        sentences = sent_tokenize(text)
    except Exception as e:
        print(f"NLTK tokenization failed: {str(e)}, using fallback tokenizer")
        sentences = simple_sentence_tokenize(text)

    # Create structured format
    structured_data = {
        "document": {
            "text": text,
            "sentences": sentences,
            "metadata": {
                "sentence_count": len(sentences),
                "word_count": len(text.split()),
                "character_count": len(text)
            }
        }
    }

    return structured_data

def format_json_for_display(data: Dict) -> str:
    """Format JSON data for display with proper indentation."""
    return json.dumps(data, indent=2)