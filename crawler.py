import trafilatura
import requests
from bs4 import BeautifulSoup
from typing import Dict, Optional
import logging

class WebCrawler:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def fetch_content(self, url: str) -> Optional[str]:
        """Fetch content from URL using trafilatura."""
        try:
            downloaded = trafilatura.fetch_url(url)
            if downloaded:
                return trafilatura.extract(downloaded)
            return None
        except Exception as e:
            logging.error(f"Error fetching content: {str(e)}")
            return None

    def get_metadata(self, url: str) -> Dict:
        """Get basic metadata about the webpage."""
        try:
            response = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            metadata = {
                "title": soup.title.string if soup.title else "No title found",
                "meta_description": soup.find("meta", {"name": "description"})["content"] 
                    if soup.find("meta", {"name": "description"}) else "No description found",
                "url": url
            }
            return metadata
        except Exception as e:
            logging.error(f"Error fetching metadata: {str(e)}")
            return {
                "title": "Error fetching metadata",
                "meta_description": "Error fetching metadata",
                "url": url
            }
