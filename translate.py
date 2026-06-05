import streamlit as st
from deep_translator import GoogleTranslator

# Page Title
st.set_page_config(page_title="Language Translation Tool", page_icon="🌍")

st.title("🌍 Language Translation Tool")
st.write("Translate text from one language to another.")

# Get all supported languages
languages = GoogleTranslator().get_supported_languages(as_dict=True)

# User Input
text = st.text_area("Enter Text to Translate")

# Language Selection
source_lang = st.selectbox(
    "Select Source Language",
    list(languages.keys())
)

target_lang = st.selectbox(
    "Select Target Language",
    list(languages.keys())
)

# Translate Button
if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:
            translated_text = GoogleTranslator(
                source=languages[source_lang],
                target=languages[target_lang]
            ).translate(text)

            st.success("Translation Successful!")

            st.subheader("Translated Text")
            st.text_area(
                "Output",
                translated_text,
                height=150
            )

            st.code(translated_text)

        except Exception as e:
            st.error(f"Error: {e}")

# Footer
st.markdown("---")
st.markdown("Created using Python, Streamlit and Deep Translator")