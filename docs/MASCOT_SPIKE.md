# Mascot Technical Spike

## Context
Liora features an interactive mascot. We need to determine the technical feasibility of implementing this in Streamlit.

## Findings
Streamlit fundamentally sanitizes and isolates custom components via iframes, which limits direct DOM interaction between the main app and custom components.

1. **Static Mascot (Light/Dark Theme)**:
   - **Feasible**: YES. We can inject custom CSS (`st.markdown("<style>...</style>", unsafe_allow_html=True)`) that responds to Streamlit's data-theme attribute, allowing light/dark mascot variants.

2. **Basic Hover Reaction**:
   - **Feasible**: YES. CSS `:hover` states work perfectly for scaling, rotation, and minor animations (e.g., eye movement or smile adjustment on hover).

3. **Cursor Tracking (Eyes following cursor across entire page)**:
   - **Feasible**: PARTIALLY / HACKY. Because Streamlit components often run in iframes, capturing global mouse coordinates (`mousemove`) and passing them to the mascot is brittle and introduces latency. Injecting global JS via `unsafe_allow_html` is possible but discouraged as it may break with Streamlit updates.

4. **Click Detection**:
   - **Feasible**: YES. We can use standard `st.button` or wrap a custom HTML component to pass events back to Streamlit, though it forces a full script rerun.

5. **State Machines (Wave, Celebration)**:
   - **Feasible**: YES. We can conditionally render different CSS classes or Lottie animations based on `st.session_state` (e.g., `if st.session_state.celebrate: render_celebration_mascot()`).

## Recommendation
We will use a **CSS-based SVG/HTML mascot** injected via `st.markdown(unsafe_allow_html=True)`. 
We will **AVOID** complex global cursor tracking via JS, as it is fragile in Streamlit. Instead, we will rely on CSS hover effects and session-state-driven animation states (idle, thinking, celebrating).
