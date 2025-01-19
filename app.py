import streamlit as st
import pandas as pd
import re

def escape_apostrophes(text):
    """Escapes apostrophes in the given text."""
    return re.sub(r"(?<!\\)'", r"\\'", text)

def format_names_normal(names):
    formatted = [f"'{escape_apostrophes(name.strip())}'" for name in names if name.strip()]
    return f"({', '.join(formatted)})"

def format_names_ps(names):
    formatted = [f"'{escape_apostrophes(name.strip().replace(' ', '_'))}'" for name in names if name.strip()]
    return f"({', '.join(formatted)})"

def format_product_codes(codes):
    formatted = []
    for code in codes:
        code = code.strip()
        if code.isdigit() and len(code) == 10:
            code = f"0{code}"
        formatted.append(f"'{code}'")
    return f"({', '.join(formatted)})"

# Streamlit App
st.title("Name Formatter")
st.write("Paste a list of names, IDs, or product codes from an Excel file, and choose a formatting style.")

# Input area
names_input = st.text_area("Paste your list of names, IDs, or product codes here (one per line):", height=200)

# Radio button for formatting style
format_style = st.radio("Choose formatting style:", ("Normal Data", "PS Names", "Product Code Formatting"))

# Process input and format names or codes
if st.button("Format Names/IDs/Product Codes"):
    names = names_input.splitlines()
    if format_style == "Normal Data":
        result = format_names_normal(names)
    elif format_style == "PS Names":
        result = format_names_ps(names)
    elif format_style == "Product Code Formatting":
        result = format_product_codes(names)
    
    # Display formatted result
    st.code(result, language="python")
