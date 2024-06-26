import streamlit as st
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.vectorstores import Chroma
from langchain.llms import Ollama
import os
import time

# Constants
model = os.environ.get("MODEL", "mistral")
embeddings_model_name = os.environ.get("EMBEDDINGS_MODEL_NAME", "all-MiniLM-L6-v2")
persist_directory = os.environ.get("PERSIST_DIRECTORY", "db")
target_source_chunks = int(os.environ.get('TARGET_SOURCE_CHUNKS', 4))

def main():
    # Initialize embeddings and database
    embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)
    db = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
    retriever = db.as_retriever(search_kwargs={"k": target_source_chunks})
    callbacks = [StreamingStdOutCallbackHandler()]  # StreamingStdOutCallbackHandler is always active

    llm = Ollama(model=model, callbacks=callbacks)
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

    st.title("SQL Analyzer")

    # Interactive questions and answers
    query = st.text_input("Enter a query:")
    if st.button("Ask"):
        if query:
            st.write(f"You asked: {query}")
            st.write("Thinking...")

            # Get the answer from the chain
            start = time.time()
            res = qa("you are an advanced sql coder, read my :"+query+", and only give sql code for sql retreival (mandatory: whithout any descriptive language on top) on the provided context")
            answer = res['result']
            end = time.time()

            # Display the answer
            st.write("Answer:")
            st.write(answer)

            # Optionally display source documents
            # No need to check args.hide_source in Streamlit context
            # if not args.hide_source:
            #     docs = res['source_documents']
            #     st.write("Source Documents:")
            #     for doc in docs:
            #         st.write(f"- {doc.metadata['source']}")

if __name__ == "__main__":
    main()
