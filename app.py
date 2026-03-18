import streamlit as st
import re

st.title("📝 Smarter Offline Notes Creator")

# Input text
text = st.text_area("Paste your lecture, article, or text here:")

# Button to generate notes
if st.button("Create Notes") and text:
    st.subheader("Generated Notes")

    # 1. Split text into sentences
    sentences = re.split(r'(?<=[.!?]) +', text.strip())

    # 2. Optional: Group sentences into paragraphs of 2-3 for mini-sections
    grouped = [sentences[i:i+3] for i in range(0, len(sentences), 3)]

    # 3. Extract simple keywords (first nouns or capitalized words)
    keywords = set(re.findall(r'\b[A-Z][a-zA-Z]+\b', text))

    # 4. Display notes
    for i, group in enumerate(grouped, 1):
        st.markdown(f"**Section {i}:**")
        for s in group:
            st.markdown(f"- {s.strip()}")
        st.markdown("")

    # 5. Display keywords
    if keywords:
        st.subheader("📌 Key Terms / Highlights")
        st.markdown(", ".join(sorted(keywords)))