import streamlit as st
import json
import pandas as pd
from crawler import WebCrawler
from utils import validate_url, structure_text_content, format_json_for_display
from styles import apply_custom_styles

# Page configuration must be the first Streamlit command
st.set_page_config(
    page_title="Web Crawler for LLM Training",
    page_icon="🕸️",
    layout="wide"
)

def main():
    # Apply custom styles
    apply_custom_styles()

    # Header
    st.title("🕸️ Web Crawler for LLM Training")
    st.markdown("""
    Transform website content into structured data suitable for LLM training.
    Enter a URL below to start crawling.
    """)

    # Initialize session state
    if 'crawled_data' not in st.session_state:
        st.session_state.crawled_data = None

    # URL input
    url = st.text_input("Enter website URL:", placeholder="https://example.com")

    # Validation and crawling
    if url:
        if not validate_url(url):
            st.error("Please enter a valid URL starting with http:// or https://")
        else:
            with st.spinner("Crawling website..."):
                crawler = WebCrawler()

                # Get metadata
                metadata = crawler.get_metadata(url)

                # Extract content
                content = crawler.fetch_content(url)

                if content:
                    # Structure the data
                    structured_data = structure_text_content(content)
                    structured_data["metadata"] = metadata

                    # Store in session state
                    st.session_state.crawled_data = structured_data

                    # Display results
                    st.success("Website crawled successfully!")

                    # Display metadata
                    st.subheader("📑 Website Metadata")
                    st.json(metadata)

                    # Display statistics
                    st.subheader("📊 Content Statistics")
                    stats = structured_data["document"]["metadata"]
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Sentences", stats["sentence_count"])
                    with col2:
                        st.metric("Words", stats["word_count"])
                    with col3:
                        st.metric("Characters", stats["character_count"])

                    # Display extracted content
                    st.subheader("📝 Extracted Content")
                    with st.expander("View extracted text"):
                        st.text_area("", value=content, height=200, disabled=True)

                    # Display structured data
                    st.subheader("🔍 Structured Data")
                    with st.expander("View structured JSON"):
                        st.code(format_json_for_display(structured_data), language="json")

                    # Download options
                    st.subheader("💾 Download Options")

                    # JSON download
                    json_str = json.dumps(structured_data, indent=2)
                    st.download_button(
                        label="Download JSON",
                        data=json_str,
                        file_name="crawled_data.json",
                        mime="application/json"
                    )

                    # CSV download (sentences)
                    df = pd.DataFrame(structured_data["document"]["sentences"], columns=["sentence"])
                    csv = df.to_csv(index=False)
                    st.download_button(
                        label="Download Sentences as CSV",
                        data=csv,
                        file_name="sentences.csv",
                        mime="text/csv"
                    )
                else:
                    st.error("Failed to extract content from the website. Please try another URL.")

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #4A5568; padding: 20px;'>
        Built with Streamlit • Uses Trafilatura for content extraction • Ready for LLM training
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()