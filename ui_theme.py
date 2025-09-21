import streamlit as st
from typing import Optional

CSS_PATH = "styles.css"

def apply_theme():
    try:
        with open(CSS_PATH, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("styles.css não encontrado.")

def section(title: str, subtitle: str = ""):
    st.markdown(f"<div class='h1'>{title}</div>", unsafe_allow_html=True)
    if subtitle:
        st.markdown(f"<div class='subtle'>{subtitle}</div>", unsafe_allow_html=True)
    st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

def card(title: str, body: str, badge: Optional[str] = None, badge_class: str = ""):
    badge_html = f"<span class='badge {badge_class}'>{badge}</span>" if badge else ""
    st.markdown(
        f"""
        <div class="card">
          <div style="display:flex;align-items:center;justify-content:space-between;gap:.5rem">
            <h3>{title}</h3>{badge_html}
          </div>
          <p>{body}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
