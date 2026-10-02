import streamlit as st
import time

st.set_page_config(page_title="Liora Mascot Spike", layout="centered")

# Custom CSS for Glass-style cards and UI Foundation
st.markdown("""
<style>
    :root {
        --glass-bg: rgba(255, 255, 255, 0.1);
        --glass-border: rgba(255, 255, 255, 0.2);
    }
    
    [data-theme="dark"] {
        --glass-bg: rgba(0, 0, 0, 0.3);
        --glass-border: rgba(255, 255, 255, 0.1);
    }

    .glass-card {
        background: var(--glass-bg);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid var(--glass-border);
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }
    
    .glass-card:hover {
        transform: translateY(-5px);
    }
    
    /* Mascot CSS */
    .mascot-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 200px;
        cursor: pointer;
    }
    
    .mascot {
        width: 100px;
        height: 100px;
        background: linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 100%);
        border-radius: 50%;
        position: relative;
        transition: all 0.3s ease;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    
    .mascot:hover {
        transform: scale(1.1) rotate(5deg);
        background: linear-gradient(135deg, #fbc2eb 0%, #a6c1ee 100%);
    }
    
    .eye {
        width: 15px;
        height: 15px;
        background: white;
        border-radius: 50%;
        position: absolute;
        top: 35px;
    }
    
    .eye.left { left: 25px; }
    .eye.right { right: 25px; }
    
    .eye::after {
        content: '';
        width: 6px;
        height: 6px;
        background: #333;
        border-radius: 50%;
        position: absolute;
        top: 4px;
        left: 4px;
        transition: all 0.1s;
    }
    
    .mascot:hover .eye::after {
        transform: translate(2px, -2px);
    }
    
    .mouth {
        width: 30px;
        height: 15px;
        border-bottom: 3px solid #333;
        border-radius: 0 0 15px 15px;
        position: absolute;
        bottom: 25px;
        left: 35px;
        transition: all 0.3s ease;
    }
    
    .mascot:hover .mouth {
        height: 20px;
        border-bottom: 4px solid #333;
        border-radius: 50%;
    }
</style>
""", unsafe_allow_html=True)

st.title("Liora UI Foundation Spike")

st.markdown("### Glass-Style Component")
st.markdown("""
<div class="glass-card">
    <h4>Test Card</h4>
    <p>This verifies that we can create custom glassmorphism styles in Streamlit.</p>
</div>
""", unsafe_allow_html=True)


st.markdown("### Mascot Spike (CSS-based)")
st.markdown("""
<div class="mascot-container">
    <div class="mascot">
        <div class="eye left"></div>
        <div class="eye right"></div>
        <div class="mouth"></div>
    </div>
</div>
""", unsafe_allow_html=True)

st.info("Note: True cursor tracking for the mascot's eyes requires custom JavaScript injections (e.g., via `components.html`) which can be brittle in Streamlit. Hover animations work cleanly via CSS.")

# Mock Authentication Test
if "auth_status" not in st.session_state:
    st.session_state.auth_status = "Logged Out"

if st.button("Simulate Login"):
    st.session_state.auth_status = "Logged In"
    st.success("Logged in successfully!")

st.write(f"Current Status: **{st.session_state.auth_status}**")
