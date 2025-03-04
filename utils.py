import re
import json
from typing import Dict, List
import nltk
from nltk.tokenize import sent_tokenize

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

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
    
    # Split into sentences
    sentences = sent_tokenize(text)
    
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
