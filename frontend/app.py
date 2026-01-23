import streamlit as st
import requests
from typing import List
import time

# Configuration
API_BASE_URL = "http://localhost:8000"  # Change this to your FastAPI server URL

# Page config
st.set_page_config(
    page_title="Code Documentation Generator",
    page_icon="📚",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .success-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        margin: 1rem 0;
    }
    .error-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
        margin: 1rem 0;
    }
    .info-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        color: #0c5460;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'uploaded_files' not in st.session_state:
    st.session_state.uploaded_files = []
if 'ingested' not in st.session_state:
    st.session_state.ingested = False
if 'documentation' not in st.session_state:
    st.session_state.documentation = None

# Header
st.markdown('<div class="main-header">📚 Code Documentation Generator</div>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("⚙️ Configuration")
    api_url = st.text_input("API Base URL", value=API_BASE_URL)
    
    st.markdown("---")
    st.header("📋 Instructions")
    st.markdown("""
    1. **Upload** Python files (.py)
    2. **Ingest** files to process them
    3. **Generate** documentation
    
    The AI will create structured documentation including:
    - Module summaries
    - Classes and methods
    - Functions with I/O
    - Usage examples
    """)
    
    st.markdown("---")
    st.header("📊 Status")
    st.metric("Files Uploaded", len(st.session_state.uploaded_files))
    st.metric("Ingestion Status", "✅ Complete" if st.session_state.ingested else "⏳ Pending")

# Main content
tab1, tab2, tab3 = st.tabs(["📤 Upload Files", "🔄 Process & Generate", "📄 Documentation"])

# Tab 1: Upload Files
with tab1:
    st.header("Upload Python Files")
    st.info("Upload one or more Python (.py) files to generate documentation.")
    
    uploaded_files = st.file_uploader(
        "Choose Python files",
        type=['py'],
        accept_multiple_files=True,
        key="file_uploader"
    )
    
    col1, col2 = st.columns([1, 4])
    with col1:
        upload_button = st.button("🚀 Upload Files", type="primary", use_container_width=True)
    
    if upload_button and uploaded_files:
        with st.spinner("Uploading files..."):
            try:
                files = [("files", (file.name, file.getvalue(), "text/x-python")) 
                        for file in uploaded_files]
                
                response = requests.post(f"{api_url}/upload", files=files)
                
                if response.status_code == 200:
                    result = response.json()
                    st.session_state.uploaded_files = result.get("filename", [])
                    st.session_state.ingested = False  # Reset ingestion status
                    st.markdown(f'<div class="success-box">✅ Successfully uploaded {len(st.session_state.uploaded_files)} file(s)!</div>', 
                              unsafe_allow_html=True)
                    
                    # Show uploaded files
                    st.write("**Uploaded files:**")
                    for filename in st.session_state.uploaded_files:
                        st.write(f"- {filename}")
                else:
                    st.markdown(f'<div class="error-box">❌ Error: {response.text}</div>', 
                              unsafe_allow_html=True)
                    
            except Exception as e:
                st.markdown(f'<div class="error-box">❌ Connection error: {str(e)}</div>', 
                          unsafe_allow_html=True)
    
    elif upload_button and not uploaded_files:
        st.warning("⚠️ Please select at least one Python file to upload.")
    
    # Show current uploaded files
    if st.session_state.uploaded_files:
        st.markdown("---")
        st.subheader("📁 Current Files")
        for filename in st.session_state.uploaded_files:
            st.write(f"✓ {filename}")

# Tab 2: Process & Generate
with tab2:
    st.header("Process Files & Generate Documentation")
    
    if not st.session_state.uploaded_files:
        st.warning("⚠️ Please upload Python files first in the 'Upload Files' tab.")
    else:
        col1, col2 = st.columns(2)
        
        # Ingest step
        with col1:
            st.subheader("Step 1: Ingest Files")
            st.write("Process uploaded files and create vector embeddings.")
            
            ingest_button = st.button("🔄 Ingest Files", type="secondary", use_container_width=True)
            
            if ingest_button:
                with st.spinner("Ingesting files... This may take a moment."):
                    try:
                        response = requests.post(f"{api_url}/ingest")
                        
                        if response.status_code == 200:
                            result = response.json()
                            st.session_state.ingested = True
                            st.markdown('<div class="success-box">✅ Files ingested successfully!</div>', 
                                      unsafe_allow_html=True)
                            st.json(result)
                        else:
                            st.markdown(f'<div class="error-box">❌ Error: {response.text}</div>', 
                                      unsafe_allow_html=True)
                            
                    except Exception as e:
                        st.markdown(f'<div class="error-box">❌ Connection error: {str(e)}</div>', 
                                  unsafe_allow_html=True)
        
        # Generate documentation step
        with col2:
            st.subheader("Step 2: Generate Docs")
            st.write("Create AI-powered structured documentation.")
            
            generate_button = st.button("📝 Generate Documentation", type="primary", use_container_width=True)
            
            if generate_button:
                if not st.session_state.ingested:
                    st.warning("⚠️ Please ingest files first!")
                else:
                    with st.spinner("Generating documentation... This may take a moment."):
                        try:
                            response = requests.post(f"{api_url}/generate_docs")
                            
                            if response.status_code == 200:
                                result = response.json()
                                st.session_state.documentation = result.get("documentation", "")
                                st.markdown('<div class="success-box">✅ Documentation generated successfully!</div>', 
                                          unsafe_allow_html=True)
                                st.info("📄 View the documentation in the 'Documentation' tab.")
                            else:
                                st.markdown(f'<div class="error-box">❌ Error: {response.text}</div>', 
                                          unsafe_allow_html=True)
                                
                        except Exception as e:
                            st.markdown(f'<div class="error-box">❌ Connection error: {str(e)}</div>', 
                                      unsafe_allow_html=True)

# Tab 3: View Documentation
with tab3:
    st.header("Generated Documentation")
    
    if st.session_state.documentation:
        st.success("✅ Documentation is ready!")
        
        # Add download button
        col1, col2, col3 = st.columns([1, 1, 3])
        with col1:
            st.download_button(
                label="📥 Download as TXT",
                data=st.session_state.documentation,
                file_name="documentation.txt",
                mime="text/plain"
            )
        with col2:
            if st.button("🔄 Clear", use_container_width=True):
                st.session_state.documentation = None
                st.rerun()
        
        st.markdown("---")
        
        # Display documentation
        st.markdown(st.session_state.documentation)
        
    else:
        st.info("ℹ️ No documentation generated yet. Please upload files, ingest them, and generate documentation in the 'Process & Generate' tab.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem;'>
    <p>Built with Streamlit | Powered by FastAPI & LangChain</p>
</div>
""", unsafe_allow_html=True)