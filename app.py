import streamlit as st
from pypdf import PdfReader
from groq import Groq
import os

# Load API key from environment variable (set it in your terminal: export GROQ_API_KEY=your_key)
# Or replace os.getenv(...) with your key string directly — but don't share it publicly!
api_key = os.getenv("GROQ_API_KEY", "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")
client = Groq(api_key=api_key)

st.title("📄 AI Document Q&A App")
st.write("Upload a PDF and ask questions about its content.")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

question = st.text_input("Ask a question about the document")


def read_pdf(file):
    """Extract text from all pages of a PDF using pypdf."""
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"
    return text.strip()


if st.button("Ask"):

    if uploaded_file is None:
        st.warning("Please upload a PDF file first.")
    elif question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Reading document and generating answer..."):
            document_text = read_pdf(uploaded_file)

            if not document_text:
                st.error(
                    "Could not extract text from this PDF. "
                    "It may be a scanned image-based PDF, which requires OCR."
                )
            else:
                # Limit document size to avoid token limits (first ~8000 chars)
                truncated_text = document_text[:8000]
                if len(document_text) > 8000:
                    st.info("Note: Document is large — only the first portion was used for context.")

                prompt = f"""You are a helpful assistant. Answer the user's question based on the document provided below.
If the question is vague or general (like "explain about this" or "what is this"), 
give a full summary of the document covering all key points.
If the answer is clearly stated in the document, give it directly.
If the document does not contain enough information to answer, say so honestly.

Document:
{truncated_text}

Question:
{question}

Answer:"""

                try:
                    chat = client.chat.completions.create(
                        messages=[
                            {
                                "role": "system",
                                "content": "You are a helpful document assistant. Answer questions accurately based on the provided document content."
                            },
                            {"role": "user", "content": prompt}
                        ],
                        model="llama-3.1-8b-instant",
                        temperature=0.2,  # Lower = more focused, factual answers
                    )

                    answer = chat.choices[0].message.content

                    st.subheader("Answer")
                    st.write(answer)

                except Exception as e:
                    st.error(f"Error getting answer from AI: {e}")
