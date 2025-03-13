import streamlit as st
from src.core.rag_chain import retrieval_chain  # Ensure retrieval_chain is defined in app.py or the appropriate module
import os

# Define the data directory
DATA_DIR = "data/raw_documents"
os.makedirs(DATA_DIR, exist_ok=True)  # Create directory if it doesn't exist

def move_to_dataFolder(pdf_docs):
    """Move uploaded PDF files to the data directory."""
    for uploaded_file in pdf_docs:
        file_path = os.path.join(DATA_DIR, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
    st.success("All files have been successfully uploaded and saved.")

def generate_message(user_input):
    """Generate a response from the retrieval chain based on user input and maintain conversation history."""
    if "conversation" not in st.session_state:
        st.session_state.conversation = []
    
    try:
        response = retrieval_chain.invoke({"input": user_input})
        answer = response.get("answer", "Sorry, I could not generate an answer.")
    except Exception as e:
        answer = f"Error: {str(e)}"
    
    st.session_state.conversation.append({"user": user_input, "assistant": answer})

def display_chat_history():
    """Display chat history with professional-looking avatars and alignment."""
    st.write("### Chat History")
    for chat in st.session_state.conversation:
        with st.chat_message("user", avatar="👤"):
            st.markdown(f"<div style='text-align: right; font-weight: bold;'>You</div> <div style='text-align: right;'>{chat['user']}</div>", unsafe_allow_html=True)
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(f"<div style='text-align: left; font-weight: bold;'>Assistant</div> <div style='text-align: left;'>{chat['assistant']}</div>", unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="HR Policy Chatbot", layout="wide")
    st.header("📚 Information Retrieval System")

    # Display chat history
    if "conversation" in st.session_state and st.session_state.conversation:
        display_chat_history()
    
    # User question input field
    user_question = st.chat_input("Ask a Question from the PDF Files")
    if user_question:
        generate_message(user_question)
        display_chat_history()
    
    with st.sidebar:
        st.title("📂 Menu")
        pdf_docs = st.file_uploader(
            "Upload your PDF Files and Click on the Submit & Process Button",
            accept_multiple_files=True,
            type=["pdf"]
        )
        
        if st.button("Submit & Process"):
            if pdf_docs:
                with st.spinner("Processing..."):
                    move_to_dataFolder(pdf_docs)
                    global retrieval_chain  # Ensure retrieval_chain is available after processing
            else:
                st.warning("Please upload at least one PDF file before processing.")

if __name__ == "__main__":
    main()
