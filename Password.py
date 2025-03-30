import streamlit as st
import random
import string
import re
import time
import math
from streamlit.components.v1 import html


COMMON_PASSWORDS = {'password', 'password123', '12345678', 'qwerty', 'admin123'}

def calculate_entropy(password):
    """Calculate password entropy based on character pool"""
    pool_size = 0
    if re.search("[a-z]", password): pool_size += 26
    if re.search("[A-Z]", password): pool_size += 26
    if re.search("[0-9]", password): pool_size += 10
    if re.search("[!@#$%^&*]", password): pool_size += 8
    return len(password) * math.log2(pool_size) if pool_size > 0 else 0

def check_password_strength(password):
    score = 0
    feedback = []
    
    
    length = len(password)
    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        feedback.append(f"Password is too short ({length}/8 min)")
    
    uppercase_count = sum(1 for c in password if c.isupper())
    if uppercase_count >= 2:
        score += 2
    elif uppercase_count == 1:
        score += 1
    else:
        feedback.append("Add uppercase letters (A-Z)")
    
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters (a-z)")
    
    digit_count = sum(1 for c in password if c.isdigit())
    if digit_count >= 2:
        score += 2
    elif digit_count == 1:
        score += 1
    else:
        feedback.append("Add numbers (0-9)")
    
    special_count = len(re.findall("[!@#$%^&*]", password))
    if special_count >= 2:
        score += 2
    elif special_count == 1:
        score += 1
    else:
        feedback.append("Add special characters (!@#$%^&*)")
    
    if password.lower() in COMMON_PASSWORDS:
        score = min(score, 3)
        feedback.append("Avoid common passwords!")
    
    return min(score, 10), feedback

def generate_strong_password(length=16):
    characters = (string.ascii_lowercase + string.ascii_uppercase + 
                 string.digits + "!@#$%^&*")
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*")
    ]
    password.extend(random.choice(characters) for _ in range(length - 4))
    random.shuffle(password)
    return ''.join(password)

def get_strength_info(score):
    if score <= 3:
        return "Weak", "#FF4444", "⚠️", 20
    elif score <= 7:
        return "Moderate", "#FFA500", "🔒", 60
    else:
        return "Strong", "#00CC00", "✅", 100


def main():
    st.set_page_config(page_title="CyberShield Password Analyzer", layout="wide")

   
    if "theme" not in st.session_state:
        st.session_state.theme = "dark"

   
    st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    }
    .title {
        font-size: 3em;
        color: #00ddeb;
        text-align: center;
        animation: neonGlow 1.5s ease-in-out infinite alternate;
    }
    .strength-container {
        padding: 20px;
        border-radius: 15px;
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        animation: fadeIn 1s ease-in;
    }
    .metric-box {
        background: rgba(255, 255, 255, 0.1);
        padding: 15px;
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        transition: transform 0.3s, box-shadow 0.3s;
        color: #e0e0e0;
    }
    .metric-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 0 15px rgba(0, 221, 235, 0.3);
    }
    .circular-meter {
        position: relative;
        width: 150px;
        height: 150px;
        margin: 0 auto;
    }
    .circular-meter svg {
        transform: rotate(-90deg);
    }
    .circular-meter .label {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 1.2em;
        color: #e0e0e0;
    }
    @keyframes neonGlow {
        from { text-shadow: 0 0 5px #00ddeb, 0 0 10px #00ddeb; }
        to { text-shadow: 0 0 20px #00ddeb, 0 0 30px #00ddeb; }
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: scale(0.95); }
        to { opacity: 1; transform: scale(1); }
    }
    .stButton>button {
        background: linear-gradient(45deg, #00ddeb, #007bff);
        color: white;
        border-radius: 25px;
        padding: 10px 20px;
        border: none;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.1);
        box-shadow: 0 0 20px rgba(0, 221, 235, 0.5);
    }
    .stTextInput>div>input {
        background: rgba(255, 255, 255, 0.1);
        color: #e0e0e0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 10px;
    }
    .stSlider>div>div>div {
        background: #00ddeb !important;
    }
    </style>
    """, unsafe_allow_html=True)

   
    theme_toggle = st.sidebar.checkbox("Light Theme", value=False)
    if theme_toggle:
        st.session_state.theme = "light"
        st.markdown("""
        <style>
        body {
            background: linear-gradient(135deg, #e0e0e0 0%, #f5f5f5 100%);
        }
        .strength-container {
            background: rgba(0, 0, 0, 0.05);
            border: 1px solid rgba(0, 0, 0, 0.1);
        }
        .metric-box {
            background: rgba(0, 0, 0, 0.1);
            border: 1px solid rgba(0, 0, 0, 0.2);
            color: #333;
        }
        .circular-meter .label {
            color: #333;
        }
        </style>
        """, unsafe_allow_html=True)

    st.markdown('<div class="title">CyberShield Password Analyzer</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
      #  st.markdown('<div class="strength-container">', unsafe_allow_html=True)
        password = st.text_input("Enter Your Password", type="password", 
                               help="Enter a password to analyze its strength")

        if password:
            score, feedback = check_password_strength(password)
            strength, color, emoji, percentage = get_strength_info(score)
            entropy = calculate_entropy(password)

            st.markdown(f"""
            <div class="circular-meter">
                <svg width="150" height="150">
                    <circle cx="75" cy="75" r="65" stroke="#444" stroke-width="10" fill="none"/>
                    <circle cx="75" cy="75" r="65" stroke="{color}" stroke-width="10" fill="none"
                        stroke-dasharray="408" stroke-dashoffset="{408 - (408 * percentage / 100)}"
                        style="transition: stroke-dashoffset 0.5s ease-in-out;"/>
                </svg>
                <div class="label">{strength}<br>{score}/10</div>
            </div>
            """, unsafe_allow_html=True)

            
            cols = st.columns(5)
            metrics = [
                ("Length", f"{len(password)} chars"),
                ("Uppercase", f"{sum(1 for c in password if c.isupper())}"),
                ("Numbers", f"{sum(1 for c in password if c.isdigit())}"),
                ("Special", f"{len(re.findall('[!@#$%^&*]', password))}"),
                ("Entropy", f"{entropy:.1f} bits")
            ]
            for i, (label, value) in enumerate(metrics):
                with cols[i]:
                    st.markdown(f"<div class='metric-box'><b>{label}</b><br>{value}</div>", 
                              unsafe_allow_html=True)

           
            if feedback:
                st.warning("Improvement Suggestions:")
                for i, suggestion in enumerate(feedback):
                    st.write(f"{i+1}. {suggestion}")
            else:
                st.success("Perfect! This password meets all security criteria!")

        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
       # st.markdown('<div class="strength-container">', unsafe_allow_html=True)
        st.subheader("Password Tools")

        
        length = st.slider("Password Length", 8, 32, 16, help="Choose the length of the generated password")
        if st.button("Generate Secure Password"):
            with st.spinner("Generating secure password..."):
                time.sleep(0.5)
                new_password = generate_strong_password(length)
                st.code(new_password, language="text")
                st.balloons()

       
        st.markdown("### Password Tips")
        with st.expander("Security Guidelines"):
            st.write("""
            - Use at least 12 characters
            - Mix uppercase and lowercase
            - Include numbers and symbols
            - Avoid personal information
            - Don't reuse passwords
            """)

        with st.expander("What is Entropy?"):
            st.write("""
            Password entropy measures unpredictability in bits.
            Higher entropy = stronger password:
            - < 28 bits: Very Weak
            - 28-35 bits: Weak
            - 36-59 bits: Reasonable
            - 60+ bits: Strong
            """)
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()