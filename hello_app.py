import streamlit as st

def main():
    """
    Main function to run the Streamlit app.
    """
    st.set_page_config(
        page_title="Hello World Streamlit App",
        page_icon="👋"
    )

    st.title("Hello World App in Streamlit! 👋")

    st.write("---") # A horizontal line for separation

    st.header("1. Displaying Plain Text")
    st.write("This is a simple plain text line displayed using `st.write()`.")
    st.text("You can also use `st.text()` for preformatted text.")

    st.header("2. Displaying Markdown")
    st.markdown("""
    This section demonstrates displaying text using **Markdown** in Streamlit.
    You can easily format text with different styles:

    * **Bold Text**: Use double asterisks like `**bold**` or double underscores `__bold__`.
    * *Italic Text*: Use single asterisks like `*italic*` or single underscores `_italic_`.
    * ~~Strikethrough Text~~: Use double tildes like `~~strikethrough~~`.
    * `Inline Code`: Use backticks like `` `inline code` ``.

    ---

    ### A Small Markdown List Example:

    1.  First item in an ordered list.
    2.  Second item, which can have
        * Nested unordered items (use hyphens or asterisks).
        * Another nested item.
    3.  Third item in the ordered list.

    > This is a blockquote, often used for quoting text.
    """)

    st.header("3. Basic Formatting with Python (within st.write)")
    st.write("You can combine plain text with **bold** or *italic* formatting directly within `st.write()` using Markdown syntax, as `st.write()` supports Markdown by default.")
    st.write(f"Here's an example using an f-string: This is some **dynamic bold** text and some *dynamic italic* text.")

    st.success("Your 'Hello World' Streamlit app is ready!")
    st.info("Run this app by opening your terminal/command prompt, navigating to the directory where you saved this file, and typing `streamlit run hello_app.py`")

if __name__ == "__main__":
    main()