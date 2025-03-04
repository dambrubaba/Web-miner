import streamlit as st

def apply_custom_styles():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }
        
        code {
            font-family: 'JetBrains Mono', monospace;
        }
        
        .stTextInput > div > div > input {
            padding: 16px;
        }
        
        .stButton > button {
            background-color: #3182CE;
            color: white;
            padding: 16px 24px;
            border-radius: 6px;
        }
        
        .stProgress > div > div > div > div {
            background-color: #3182CE;
        }
        
        .stDownloadButton > button {
            background-color: #2D3748;
            color: white;
            padding: 16px 24px;
            border-radius: 6px;
        }
        
        .output-container {
            background-color: white;
            padding: 16px;
            border-radius: 8px;
            border: 1px solid #E2E8F0;
        }
        </style>
    """, unsafe_allow_html=True)
