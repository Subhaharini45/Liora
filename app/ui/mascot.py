import streamlit as st

def render_mascot():
    """Renders the Liora placeholder mascot using HTML/CSS."""
    st.markdown("""
        <div class="mascot-container">
            <div class="mascot">
                <div class="mascot-eye eye-left"></div>
                <div class="mascot-eye eye-right"></div>
                <div class="mascot-smile"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray; font-size: 0.8em;'>Liora (Idle)</p>", unsafe_allow_html=True)
