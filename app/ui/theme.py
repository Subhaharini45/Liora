def get_css(theme_mode: str = "Light") -> str:
    if theme_mode == "Dark":
        bg_color = "#0b132b"
        text_color = "#e0e7ff"
        card_bg = "rgba(28, 37, 65, 0.6)"
        card_border = "rgba(255, 255, 255, 0.05)"
        glass_shadow = "0 8px 32px 0 rgba(0, 0, 0, 0.4)"
        glass_shadow_hover = "0 12px 40px 0 rgba(92, 107, 192, 0.3)"
        accent_primary = "#5c6bc0"
        accent_secondary = "#3949ab"
        mascot_glow = "rgba(92, 107, 192, 0.6)"
    else:
        # Light Theme defaults
        bg_color = "#f7f9fc"
        text_color = "#2c3e50"
        card_bg = "rgba(255, 255, 255, 0.7)"
        card_border = "rgba(255, 255, 255, 0.5)"
        glass_shadow = "0 8px 32px 0 rgba(161, 196, 253, 0.2)"
        glass_shadow_hover = "0 12px 40px 0 rgba(161, 196, 253, 0.3)"
        accent_primary = "#a1c4fd"
        accent_secondary = "#c2e9fb"
        mascot_glow = "rgba(161, 196, 253, 0.5)"

    return f"""
    <style>
    /* Theme variables mapped explicitly */
    :root {{
        --bg-color: {bg_color};
        --text-color: {text_color};
        --card-bg: {card_bg};
        --card-border: {card_border};
        --glass-shadow: {glass_shadow};
        --glass-shadow-hover: {glass_shadow_hover};
        --accent-primary: {accent_primary};
        --accent-secondary: {accent_secondary};
        --mascot-glow: {mascot_glow};
    }}

    /* Target the main container */
    .stApp {{
        background-color: var(--bg-color);
        color: var(--text-color);
        transition: background-color 0.3s ease, color 0.3s ease;
    }}
    
    /* Glassmorphism Cards */
    .glass-card {{
        background: var(--card-bg);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid var(--card-border);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 24px;
        box-shadow: var(--glass-shadow);
        color: var(--text-color);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }}
    
    .glass-card:hover {{
        transform: translateY(-2px);
        box-shadow: var(--glass-shadow-hover);
    }}
    
    /* Headings inside cards */
    .glass-card h2, .glass-card h3, .glass-card h4 {{
        color: var(--text-color);
        margin-top: 0;
    }}

    /* Mascot Base Styles */
    .mascot-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 20px;
    }}

    .mascot {{
        width: 80px;
        height: 80px;
        background: linear-gradient(135deg, var(--accent-primary) 0%, var(--accent-secondary) 100%);
        border-radius: 50%;
        position: relative;
        box-shadow: 0 0 20px var(--mascot-glow);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}

    .mascot:hover {{
        transform: scale(1.1) translateY(-5px);
    }}

    .mascot-eye {{
        position: absolute;
        width: 12px;
        height: 12px;
        background: white;
        border-radius: 50%;
        top: 25px;
    }}
    
    .mascot-eye::after {{
        content: '';
        position: absolute;
        width: 4px;
        height: 4px;
        background: #1a1a1a;
        border-radius: 50%;
        top: 4px;
        left: 4px;
        transition: transform 0.2s;
    }}

    .mascot:hover .mascot-eye::after {{
        transform: translate(2px, -2px);
    }}

    .eye-left {{ left: 20px; }}
    .eye-right {{ right: 20px; }}

    .mascot-smile {{
        position: absolute;
        width: 24px;
        height: 12px;
        border-bottom: 3px solid rgba(0,0,0,0.6);
        border-radius: 0 0 12px 12px;
        bottom: 20px;
        left: 28px;
        transition: height 0.2s, border-radius 0.2s;
    }}

    .mascot:hover .mascot-smile {{
        height: 16px;
        border-radius: 50%;
    }}
    </style>
    """
