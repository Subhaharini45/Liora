import streamlit as st
from app.ui.theme import get_css
from app.ui.mascot import render_mascot

# Dummy views for placeholders
def view_dashboard():
    st.markdown("""
        <div class="glass-card">
            <h2>Welcome to Liora</h2>
            <p>Your AI-powered, adaptive, memory-aware learning assistant.</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <div class="glass-card">
                <h3>Quick Resume</h3>
                <p>Continue your recent learning path.</p>
                <p><em>(Placeholder)</em></p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class="glass-card">
                <h3>Daily Goal</h3>
                <p>Progress: 60%</p>
                <p><em>(Placeholder)</em></p>
            </div>
        """, unsafe_allow_html=True)

def view_ai_tutor():
    st.markdown("""
        <div class="glass-card">
            <h2>AI Tutor</h2>
            <p>Ask questions and explore concepts interactively.</p>
            <p><em>(RAG and Chat functionality to be implemented)</em></p>
        </div>
    """, unsafe_allow_html=True)

def view_knowledge_base():
    st.markdown("""
        <div class="glass-card">
            <h2>Knowledge Base</h2>
            <p>Upload and manage your study documents.</p>
            <p><em>(Vector DB integration pending)</em></p>
        </div>
    """, unsafe_allow_html=True)

def view_practice():
    st.markdown("""
        <div class="glass-card">
            <h2>Practice</h2>
            <p>Test your knowledge with adaptive quizzes.</p>
            <p><em>(Quiz generation engine pending)</em></p>
        </div>
    """, unsafe_allow_html=True)

def view_progress():
    st.markdown("""
        <div class="glass-card">
            <h2>Progress & Analytics</h2>
            <p>Track your learning journey over time.</p>
            <p><em>(Analytics dashboard pending)</em></p>
        </div>
    """, unsafe_allow_html=True)

def main():
    st.set_page_config(
        page_title="Liora Learning Assistant",
        page_icon="✨",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Initialize theme in session state
    if "theme_mode" not in st.session_state:
        st.session_state.theme_mode = "Light"

    # Sidebar setup
    with st.sidebar:
        render_mascot()
        st.markdown("---")
        
        # Explicit Theme Toggle
        theme_mode = st.radio("Theme", ["Light", "Dark"], index=0 if st.session_state.theme_mode == "Light" else 1, horizontal=True)
        st.session_state.theme_mode = theme_mode
        
        # Mock Authentication
        if "user_authenticated" not in st.session_state:
            st.session_state.user_authenticated = False
            
        if not st.session_state.user_authenticated:
            st.warning("Running in Dev Mode (Unauthenticated)")
            if st.button("Simulate Login"):
                st.session_state.user_authenticated = True
                st.rerun()
        else:
            st.success("Authenticated as: Test User")
            if st.button("Logout"):
                st.session_state.user_authenticated = False
                st.rerun()
                
        st.markdown("---")
        
        # Navigation
        st.subheader("Navigation")
        page = st.radio(
            "Go to",
            ["Dashboard", "AI Tutor", "Knowledge Base", "Practice", "Progress"],
            label_visibility="collapsed"
        )
    
    # Inject Custom CSS Theme based on explicit toggle
    st.markdown(get_css(st.session_state.theme_mode), unsafe_allow_html=True)
    
    # Main content area
    if page == "Dashboard":
        view_dashboard()
    elif page == "AI Tutor":
        view_ai_tutor()
    elif page == "Knowledge Base":
        view_knowledge_base()
    elif page == "Practice":
        view_practice()
    elif page == "Progress":
        view_progress()

if __name__ == "__main__":
    main()
