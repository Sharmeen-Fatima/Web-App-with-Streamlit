import streamlit as st
import streamlit.components.v1 as components


if "history" not in st.session_state:
    st.session_state.history = []
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False
if "show_animation" not in st.session_state:
    st.session_state.show_animation = False


def toggle_dark_mode():
    st.session_state.dark_mode = not st.session_state.dark_mode


dark_mode_styles = """
    .stApp {
        background: #2c3e50;
        color: #e8eaed;
    }
    .header-box {
        background: #3c4043;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
    }
    .title {
        color: #e8eaed;
    }
    .converter-box {
        background: #3c4043;
        box-shadow: inset 5px 5px 10px rgba(0, 0, 0, 0.5), inset -5px -5px 10px rgba(255, 255, 255, 0.1), 0 8px 20px rgba(0, 0, 0, 0.5);
    }
    .input-field {
        background: #4a4e54;
        color: #e8eaed;
        border: 1px solid #5f6368;
        box-shadow: inset 2px 2px 5px rgba(0, 0, 0, 0.3), inset -2px -2px 5px rgba(255, 255, 255, 0.1);
    }
    .result-box {
        background: #4a4e54;
        color: #e8eaed;
        box-shadow: inset 3px 3px 8px rgba(0, 0, 0, 0.4), inset -3px -3px 8px rgba(255, 255, 255, 0.1);
    }
    .history-box {
        background: #4a4e54;
        color: #e8eaed;
        box-shadow: inset 2px 2px 5px rgba(0, 0, 0, 0.3), inset -2px -2px 5px rgba(255, 255, 255, 0.1);
    }
    .stSelectbox label, .stTextInput label {
        color: #e8eaed;
    }
    .stSelectbox select {
        background: #4a4e54;
        color: #e8eaed;
    }
    .stButton>button {
        background: #ff6f61;
        color: white;
    }
    .stButton>button:hover {
        background: #ff3d00;
        box-shadow: 0 0 15px #ff6f61;
    }
    .star {
        background: #ffd700;
    }
    .flash-overlay {
        background: rgba(255, 215, 0, 0.3);
    }
""" if st.session_state.dark_mode else ""

st.markdown(
    f"""
    <style>
    /* Minimalistic and attractive styling */
    .stApp {{
        background: #e0eafc;
        font-family: 'Roboto', sans-serif;
        color: #202124;
        transition: all 0.3s ease;
    }}
    .header-box {{
        background: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        max-width: 600px;
        margin: 0 auto 30px auto;
        animation: fadeInDown 1s ease-out;
        text-align: center;
    }}
    .title {{
        font-size: 2.5em;
        color: #202124;
        margin: 0;
    }}
    .converter-box {{
        background: #ffffff;
        padding: 40px;
        border-radius: 15px;
        box-shadow: inset 5px 5px 10px rgba(0, 0, 0, 0.2), inset -5px -5px 10px rgba(255, 255, 255, 0.5), 0 8px 20px rgba(0, 0, 0, 0.3);
        max-width: 600px;
        margin: 0 auto;
        animation: slideIn 0.8s ease-out;
        position: relative;
    }}
    .input-field {{
        font-size: 1.2em;
        padding: 12px;
        border-radius: 8px;
        border: 1px solid #dadce0;
        width: 100%;
        background: #ffffff;
        box-shadow: inset 2px 2px 5px rgba(0, 0, 0, 0.2), inset -2px -2px 5px rgba(255, 255, 0.5);
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
        animation: fadeIn 1s ease-in;
    }}
    .input-field:focus {{
        border-color: #ff6f61;
        box-shadow: 0 0 10px rgba(255, 111, 97, 0.5);
        outline: none;
    }}
    .result-box {{
        background: #ffffff;
        padding: 15px;
        border-radius: 8px;
        margin-top: 20px;
        font-size: 1.2em;
        color: #202124;
        box-shadow: inset 3px 3px 8px rgba(0, 0, 0, 0.2), inset -3px -3px 8px rgba(255, 255, 255, 0.5);
        animation: fadeIn 1s ease-in;
        position: relative;
        overflow: hidden;
    }}
    .history-box {{
        background: #ffffff;
        padding: 15px;
        border-radius: 8px;
        margin-top: 10px;
        font-size: 1em;
        color: #202124;
        box-shadow: inset 2px 2px 5px rgba(0, 0, 0, 0.2), inset -2px -2px 5px rgba(255, 255, 255, 0.5);
        animation: fadeIn 1s ease-in;
    }}
    .stSelectbox {{
        animation: fadeIn 1s ease-in;
    }}
    .stSelectbox select {{
        background: #202124;
        color: #ffffff;
        border-radius: 8px;
        padding: 10px;
        box-shadow: inset 2px 2px 5px rgba(0, 0, 0, 0.2), inset -2px -2px 5px rgba(255, 255, 255, 0.5);
        transition: box-shadow 0.3s ease;
    }}
    .stSelectbox select:focus {{
        box-shadow: 0 0 10px rgba(255, 111, 97, 0.5);
    }}
    .stButton>button {{
        background: #ff6f61;
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 8px;
        font-size: 1em;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        transition: transform 0.3s, box-shadow 0.3s;
        animation: pulse 2s infinite ease-in-out;
    }}
    .stButton>button:hover {{
        transform: scale(1.05);
        box-shadow: 0 0 15px #ff6f61;
    }}
    .clear-button {{
        background: #ff6f61;
        color: white;
        border: none;
        padding: 8px 16px;
        border-radius: 8px;
        font-size: 0.9em;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        transition: transform 0.3s, box-shadow 0.3s;
        animation: bounceIn 1s ease-in;
    }}
    .clear-button:hover {{
        transform: scale(1.05);
        box-shadow: 0 0 15px #ff6f61;
    }}
    .dark-mode-toggle {{
        position: fixed;
        top: 20px;
        right: 20px;
        font-size: 1.2em;
        color: #ff6f61;
        cursor: pointer;
        animation: fadeIn 1s ease-in;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
    }}
    /* Star and Flash Animations */
    .star {{
        position: absolute;
        background: #ffd700;
        border-radius: 50%;
        animation: starBurst 1s ease-out;
    }}
    @keyframes starBurst {{
        0% {{ transform: scale(0); opacity: 1; }}
        100% {{ transform: scale(3); opacity: 0; }}
    }}
    .flash-overlay {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(255, 215, 0, 0.5);
        animation: flash 0.5s ease-out;
    }}
    @keyframes flash {{
        0% {{ opacity: 1; }}
        100% {{ opacity: 0; }}
    }}
    /* Additional Animations */
    @keyframes slideIn {{
        0% {{ transform: translateY(-20px); opacity: 0; }}
        100% {{ transform: translateY(0); opacity: 1; }}
    }}
    @keyframes fadeIn {{
        0% {{ opacity: 0; }}
        100% {{ opacity: 1; }}
    }}
    @keyframes fadeInDown {{
        0% {{ opacity: 0; transform: translateY(-20px); }}
        100% {{ opacity: 1; transform: translateY(0); }}
    }}
    @keyframes bounceIn {{
        0% {{ transform: scale(0.8); opacity: 0; }}
        60% {{ transform: scale(1.1); opacity: 1; }}
        100% {{ transform: scale(1); }}
    }}
    @keyframes pulse {{
        0% {{ box-shadow: 0 0 5px #ff6f61; }}
        50% {{ box-shadow: 0 0 20px #ff6f61; }}
        100% {{ box-shadow: 0 0 5px #ff6f61; }}
    }}
    /* Dark Mode Styles */
    {dark_mode_styles}
    </style>
    <!-- Load Animate.css from CDN -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
    """,
    unsafe_allow_html=True
)


st.markdown(
    f'<div class="dark-mode-toggle" onclick="st.session_state.dark_mode = !st.session_state.dark_mode">'
    f'{"🌙 Dark Mode" if not st.session_state.dark_mode else "☀️ Light Mode"}'
    f'</div>',
    unsafe_allow_html=True
)
if st.button("Toggle Theme", key="theme_toggle"):
    toggle_dark_mode()


with st.container():
    st.markdown(
        '<div class="header-box">'
        '<h1 class="title">Google Unit Converter</h1>'
        '</div>',
        unsafe_allow_html=True
    )
    
    units = ["Meters", "Centimeters", "Kilometers", "Millimeters"]
    col1, col2 = st.columns([1, 1])
    with col1:
        unit_from = st.selectbox("From", units, index=0, key="unit_from")
    with col2:
        unit_to = st.selectbox("To", units, index=1, key="unit_to")

    
    st.markdown('<p style="font-size: 1.1em; margin-bottom: 10px; margin-top: 20px;">Enter Value:</p>', unsafe_allow_html=True)
    value = st.text_input("", value="1", key="value_input", help="Enter a numeric value to convert")

    
    if st.button("Convert"):
        st.session_state.show_animation = True
        try:
            value = float(value)
            if value < 0:
                st.error("Please enter a positive value.")
            else:
               
                conversion_factors = {
                    "Meters": {"Meters": 1, "Centimeters": 100, "Kilometers": 0.001, "Millimeters": 1000},
                    "Centimeters": {"Meters": 0.01, "Centimeters": 1, "Kilometers": 0.00001, "Millimeters": 10},
                    "Kilometers": {"Meters": 1000, "Centimeters": 100000, "Kilometers": 1, "Millimeters": 1000000},
                    "Millimeters": {"Meters": 0.001, "Centimeters": 0.1, "Kilometers": 0.000001, "Millimeters": 1}
                }
                result = value * conversion_factors[unit_from][unit_to]
                result_text = f"{value} {unit_from.lower()} = {result:.2f} {unit_to.lower()}"

               
                st.markdown(
                    f'<div class="result-box">'
                    f'{result_text}'
                    f'{"<div class='flash-overlay'></div>" if st.session_state.show_animation else ""}'
                    f'{"<div class='star' style='top: 10px; left: 10px; width: 10px; height: 10px;'></div>" if st.session_state.show_animation else ""}'
                    f'{"<div class='star' style='top: 10px; right: 10px; width: 10px; height: 10px;'></div>" if st.session_state.show_animation else ""}'
                    f'{"<div class='star' style='bottom: 10px; left: 10px; width: 10px; height: 10px;'></div>" if st.session_state.show_animation else ""}'
                    f'{"<div class='star' style='bottom: 10px; right: 10px; width: 10px; height: 10px;'></div>" if st.session_state.show_animation else ""}'
                    f'</div>',
                    unsafe_allow_html=True
                )

                
                if result_text not in st.session_state.history:
                    st.session_state.history.append(result_text)
        except ValueError:
            st.error("Please enter a valid numeric value.")
            st.session_state.show_animation = False

    
    with st.expander("Conversion History", expanded=True):
        if st.session_state.history:
            for entry in st.session_state.history:
                st.markdown(f'<div class="history-box">{entry}</div>', unsafe_allow_html=True)
            
            st.button("Clear History", key="clear_history")
            if st.session_state.get("clear_history"):
                st.session_state.history = []  
                st.success("History cleared successfully!")

    st.markdown('</div>', unsafe_allow_html=True)