import streamlit as st

from modules.extract import extract_text_from_pdf
from modules.cleaning import clean_text
from modules.chunk import chunk_text
from modules.openai_integration import ask_openai
from modules.vector_store import store_chunks
from modules.retriever import retrieve_chunks
# Page configuration
st.set_page_config(
    page_title="AI Smart File Assistant",
    page_icon="📄",
    layout="wide"
)

# Decent professional styling
st.markdown("""
<style>

/* Main background */
.stApp {
background-color: #f5f7fb;
}

/* Header */
h1 {
color: #2c3e50 !important;
font-weight: 700;
}

/* Subtitle */
p {
color: #555;
}

/* Sidebar */
section[data-testid="stSidebar"] {
background-color: #ffffff;
border-right: 1px solid #e6e6e6;
}

/* Upload box */
[data-testid="stFileUploader"] {
background-color: #ffffff;
padding: 15px;
border-radius: 8px;
border: 1px solid #e6e6e6;
}

/* Question input */
[data-testid="stTextInput"] {
background-color: #ffffff;
padding: 10px;
border-radius: 8px;
border: 1px solid #e6e6e6;
}

/* Success message */
[data-testid="stAlert"] {
border-radius: 8px;
}

/* Footer text */
footer {
visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# Header
st.markdown(
    """
    <h1 style='text-align: center;'>📄 AI Smart File Assistant</h1>
    <p style='text-align: center; font-size:18px;'>
    Upload documents and ask questions to instantly extract information using AI.
    </p>
    """,
    unsafe_allow_html=True
)


# Sidebar
with st.sidebar:
    st.title("📚 About This App")

    st.write(
        """
        **AI Smart File Assistant**

        This application allows users to upload PDF documents
        and ask questions about the content.

        The system:
        - Extracts text from PDFs
        - Cleans and processes the data
        - Splits it into smaller chunks
        - Uses AI to answer your questions

        **Technologies Used**
        - Streamlit
        - OpenAI API
        - PyMuPDF
        - Python
        """
    )


# Layout with columns
col1, col2 = st.columns([1, 2])


with col1:
    st.subheader("📤 Upload Document")
    uploaded_file = st.file_uploader("Upload a PDF", type="pdf")


with col2:
    st.subheader("❓ Ask a Question")
    question = st.text_input("Enter your question about the document")


# Processing the document
if uploaded_file:

    with st.spinner("Processing document... Please wait"):
        text = extract_text_from_pdf(uploaded_file)
        cleaned_text = clean_text(text)
        chunks = chunk_text(cleaned_text)
        store_chunks(chunks)

    st.success(f"✅ Document processed into {len(chunks)} chunks")


    if question:

        relevant_chunks = retrieve_chunks(question)
        context = " ".join(relevant_chunks)

        with st.spinner("Generating answer..."):
            answer = ask_openai(context, question)

        st.markdown("### 🤖 AI Answer")
        
        
        st.markdown(
            f"""
            <div style="
                background-color:#ffffff;
                padding:20px;
                border-radius:10px;
                border-left:6px solid #4CAF50;
                box-shadow:0 2px 8px rgba(0,0,0,0.1);
                font-size:16px;
            ">
            {answer}
            </div>
            """,
            unsafe_allow_html=True
        )


# Footer
st.markdown("---")
st.markdown(
    "<center style='color:#555;'>AI Smart File Assistant • Document Query System</center>",
    unsafe_allow_html=True
)
