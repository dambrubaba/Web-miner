# Web Crawler for LLM Training

A Streamlit-based web application that crawls websites and transforms their content into structured data suitable for training Large Language Models (LLMs).

## Features

- 🌐 Web Crawling: Extract content from any public website
- 📊 Data Structuring: Convert raw content into LLM-friendly format
- 📑 Metadata Extraction: Capture page titles, descriptions, and other metadata
- 📥 Multiple Export Options: Download data in JSON or CSV formats
- 📊 Content Statistics: View word counts, sentence counts, and character counts
- 🎨 Clean, Modern UI: Intuitive interface with responsive design

## Getting Started

### Prerequisites
- Python 3.11+
- Required packages (automatically installed):
  - streamlit
  - trafilatura
  - nltk
  - beautifulsoup4
  - pandas
  - requests

### Running the Application

1. The application is hosted on Replit and can be accessed directly through the provided `.replit.app` URL
2. To run locally in development:
   ```bash
   streamlit run main.py
   ```

### Usage

1. Enter a website URL in the input field
2. Click to start crawling
3. View extracted content and metadata
4. Download processed data in your preferred format

## Project Structure

```
├── main.py           # Main Streamlit application
├── crawler.py        # Web crawling functionality
├── utils.py          # Utility functions and text processing
├── styles.py         # Custom UI styling
└── .streamlit/       # Streamlit configuration
    └── config.toml   # Streamlit settings
```

## Data Output Format

The application outputs structured data in the following format:

```json
{
  "metadata": {
    "title": "Page Title",
    "meta_description": "Page Description",
    "url": "https://example.com"
  },
  "document": {
    "text": "Full extracted text",
    "sentences": ["Sentence 1", "Sentence 2", ...],
    "metadata": {
      "sentence_count": 10,
      "word_count": 150,
      "character_count": 750
    }
  }
}
```

## Deployment

This application can be deployed on various platforms. See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions on deploying to:

- Streamlit Cloud (Recommended)
- Heroku
- Google Cloud Run
- AWS Elastic Beanstalk
- DigitalOcean App Platform

For the simplest deployment experience, we recommend using either Replit or Streamlit Cloud.

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open-source and available under the MIT License.