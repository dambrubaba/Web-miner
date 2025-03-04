# Web Crawler for LLM Training - Master Prompt

## Project Overview
A web-based tool that utilizes web crawling to transform website content into structured data suitable for Large Language Model (LLM) training or querying.

## Core Requirements

### Functionality
1. Input field for website URLs to crawl
2. Crawl websites and extract relevant text content
3. Convert extracted content into structured, LLM-compatible format
4. Download or view the processed data

### Technical Stack
- Frontend Framework: Streamlit
- Web Crawling: Trafilatura
- Text Processing: NLTK
- Data Handling: Pandas
- Web Scraping: BeautifulSoup4
- HTTP Requests: Requests

### Design Guidelines

#### Color Scheme
- Primary: #2D3748 (slate blue)
- Secondary: #4A5568 (grey blue)
- Background: #F7FAFC (off-white)
- Text: #1A202C (dark grey)
- Accent: #3182CE (bright blue)

#### Typography
- Main Font: Inter
- Code Font: JetBrains Mono
- Base Size: 16px

#### Layout
- Minimalist single-column layout
- Clear visual hierarchy
- Responsive design
- Collapsible sections
- 16px padding standard

### Visual References
Inspired by:
- OpenAI's Playground
- Langchain's data tools

## Implementation Details

### Data Processing
1. URL validation
2. Content extraction
3. Text structuring
4. Metadata collection
5. Export formatting

### User Interface
1. URL input field
2. Processing status indicators
3. Structured data display
4. Download options
5. Error messaging

### Error Handling
1. Invalid URLs
2. Failed crawling attempts
3. Processing errors
4. Download issues

## Deployment
- Platform: Replit
- Configuration: Streamlit server
- Port: 5000
- Access: Public URL

## Success Criteria
1. Successfully crawls websites
2. Extracts relevant content
3. Structures data appropriately
4. Provides downloadable output
5. Maintains responsive UI
6. Handles errors gracefully
