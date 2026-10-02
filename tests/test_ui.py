import pytest
import os
import sys

# Add the project root to the path so that app imports work
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_ui_theme_generation():
    """Verify that CSS theme generation returns a non-empty string for both themes."""
    from app.ui.theme import get_css
    
    css_light = get_css("Light")
    assert isinstance(css_light, str)
    assert len(css_light) > 0
    assert "glass-card" in css_light
    assert "#f7f9fc" in css_light  # Light bg color
    
    css_dark = get_css("Dark")
    assert isinstance(css_dark, str)
    assert len(css_dark) > 0
    assert "glass-card" in css_dark
    assert "#0b132b" in css_dark  # Dark bg color

def test_app_imports():
    """Verify that the main app modules can be imported without errors."""
    try:
        import app.ui.main
        import app.ui.theme
        import app.ui.mascot
        success = True
    except ImportError as e:
        success = False
        pytest.fail(f"Failed to import app modules: {e}")
    assert success
