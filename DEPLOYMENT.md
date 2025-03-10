# Deployment Options for Web Crawler Application

# Streamlit Cloud Deployment Guide

## Quick Setup

1. Create a GitHub repository and push your code including:
   ```
   main.py
   utils.py
   crawler.py
   styles.py
   .streamlit/config.toml
   packages.txt
   requirements.txt
   ```

2. Visit [Streamlit Cloud](https://share.streamlit.io) and:
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Select main.py as the main file
   - Deploy

## Configuration Files

### .streamlit/config.toml
```toml
[server]
address = "0.0.0.0"
headless = true
enableCORS = false
enableXsrfProtection = false

[theme]
primaryColor = "#3182CE"
backgroundColor = "#F7FAFC"
secondaryBackgroundColor = "#4A5568"
textColor = "#1A202C"
font = "sans serif"
```

### packages.txt
```
python3-dev
build-essential
```

## Troubleshooting

If you encounter deployment issues:

1. Check the deployment logs in Streamlit Cloud dashboard
2. Verify that NLTK data is being downloaded correctly
3. Ensure all dependencies are properly listed in requirements.txt
4. The app will automatically use the port provided by Streamlit Cloud

## Health Checks

Streamlit Cloud performs health checks automatically. The configuration ensures:
- The app binds to the correct address (0.0.0.0)
- Uses the port provided by Streamlit Cloud
- CORS and XSRF protection are properly configured

## 2. Heroku
- **Required Changes**:
  1. Add `Procfile`:
    ```
    web: streamlit run main.py
    ```
  2. Add `runtime.txt`:
    ```
    python-3.11.x
    ```
  3. Configure `PORT` environment variable in Heroku dashboard
  4. Add NLTK data download to startup

## 3. Google Cloud Run
- **Required Changes**:
  1. Create `Dockerfile`:
    ```dockerfile
    FROM python:3.11-slim

    WORKDIR /app
    COPY . .
    RUN pip install -r requirements.txt
    RUN python -c "import nltk; nltk.download('punkt')"

    EXPOSE 8080
    CMD streamlit run --server.port 8080 --server.address 0.0.0.0 main.py
    ```
  2. Enable Cloud Build API
  3. Deploy using Google Cloud Console or CLI

## 4. AWS Elastic Beanstalk
- **Required Changes**:
  1. Create `.ebextensions/01_python.config`:
    ```yaml
    option_settings:
      aws:elasticbeanstalk:container:python:
        WSGIPath: main:app
    ```
  2. Add `requirements.txt`
  3. Configure environment variables in EB Console

## 5. DigitalOcean App Platform
- **Required Changes**:
  1. Add `requirements.txt`
  2. Configure as a Python web service
  3. Set environment variables:
    ```
    PORT=8080
    ```

## Important Considerations

### Environment Setup
For all platforms, ensure:
1. NLTK data is downloaded during deployment
2. Port configuration matches platform requirements
3. Dependencies are properly specified
4. Environment variables are configured

### Code Modifications
Add platform detection in main.py:
```python
import os

# Get port from environment variable or use default
port = int(os.environ.get("PORT", 5000))

# Update Streamlit config
st.set_page_config(
    page_title="Web Crawler for LLM Training",
    page_icon="🕸️",
    layout="wide"
)
```

### Security Considerations
1. Implement rate limiting for web crawling
2. Add error handling for platform-specific issues
3. Configure CORS appropriately
4. Monitor resource usage

### Cost Considerations
- Streamlit Cloud: Free tier available
- Heroku: Paid plans only (since removal of free tier)
- Google Cloud Run: Pay-per-use, free tier available
- AWS: Free tier available, then pay-per-use
- DigitalOcean: Starting at $5/month

### Recommended Choice
**Streamlit Cloud** is recommended because:
1. Native Streamlit support
2. Minimal configuration needed
3. Straightforward deployment process
4. Free tier available
5. Automatic HTTPS and scaling