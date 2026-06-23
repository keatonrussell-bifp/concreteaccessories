from __future__ import annotations

from pathlib import Path
import base64

import streamlit as st
import streamlit.components.v1 as components


APP_TITLE = "New Steel Distributors Quote Builder"
HTML_FILE = Path(__file__).with_name("Accessories_Quote_Builder_Traders_Products.html")
DEFAULT_HEIGHT = 1200


st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🧾",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      .block-container { padding-top: 1rem; padding-bottom: 1rem; max-width: 100%; }
      header[data-testid="stHeader"] { display: none; }
      div[data-testid="stToolbar"] { display: none; }
      footer { display: none; }
    </style>
    """,
    unsafe_allow_html=True,
)


def read_html() -> str:
    """Read the quote-builder HTML that lives next to this Streamlit app."""
    if not HTML_FILE.exists():
        st.error(f"Missing HTML file: {HTML_FILE.name}")
        st.stop()
    return HTML_FILE.read_text(encoding="utf-8", errors="replace")


def make_download_link(html: str) -> None:
    """Optional download link for the hosted HTML file."""
    b64 = base64.b64encode(html.encode("utf-8")).decode("ascii")
    href = (
        f'<a href="data:text/html;base64,{b64}" '
        f'download="{HTML_FILE.name}">Download current HTML</a>'
    )
    st.sidebar.markdown(href, unsafe_allow_html=True)


def main() -> None:
    html = read_html()

    with st.sidebar:
        st.header("Quote Builder")
        height = st.number_input(
            "Frame height",
            min_value=700,
            max_value=3000,
            value=DEFAULT_HEIGHT,
            step=100,
            help="Increase this if the bottom of the quote builder is cut off.",
        )
        st.caption(
            "Products, Customers, and Traders are loaded inside the quote builder from Products.xlsx. "
            "Click Select Products in the app, then choose the workbook."
        )
        make_download_link(html)

    components.html(html, height=int(height), scrolling=True)


if __name__ == "__main__":
    main()
