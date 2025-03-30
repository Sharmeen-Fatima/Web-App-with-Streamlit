import streamlit as st
from streamlit_lottie import st_lottie
import requests
import matplotlib.pyplot as plt
import numpy as np

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


st.set_page_config(page_title="Growth Mindset Tracker", page_icon=":rocket:", layout="wide")


st.markdown("""
    <style>
        /* Sidebar Styling */
        .css-18e3p6a {
            background: linear-gradient(135deg, #1abc9c, #16a085);
            color: white;
            border-radius: 10px;
            padding: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        }

        .sidebar .sidebar-content {
            padding-top: 20px;
        }

        .sidebar .sidebar-header {
            font-size: 2rem;
            color: white;
            font-weight: bold;
            margin-top: 20px;
        }

        /* Sidebar items */
        .css-1y4ld6u {
            font-size: 1.1rem;
            padding: 10px;
            color: #ffffff;
            border-radius: 5px;
            font-weight: 500;
            transition: background-color 0.3s ease;
        }

        .css-1y4ld6u:hover {
            background-color: #16a085;
            cursor: pointer;
        }

        .css-1y4ld6u:active {
            background-color: #1abc9c;
        }

        /* Hover effect for sidebar items */
        .css-1y4ld6u:hover {
            background-color: #e67e22;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        }

        /* Sidebar icons */
        .sidebar .css-18e3p6a .stIcon {
            margin-right: 10px;
        }

        .title {
            font-size: 3rem;
            color: #ffffff;
            text-align: center;
            margin-top: 20px;
            font-weight: bold;
        }
        
        .subtitle {
            color: #ffffff;
            font-size: 1.5rem;
            font-weight: 400;
        }

        .button {
            background-color: #f39c12;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            font-size: 1rem;
            border: none;
            transition: background-color 0.3s ease;
        }

        .button:hover {
            background-color: #e67e22;
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        }

        .card {
            background-color: #34495e;
            border-radius: 15px;
            padding: 25px;
            color: #ffffff;
            margin-bottom: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        }
    </style>
""", unsafe_allow_html=True)


st.sidebar.markdown('<div class="sidebar-header">Growth Mindset Tracker</div>', unsafe_allow_html=True)

sidebar_option = st.sidebar.radio("", 
                                 ["Introduction", "Set Your Goal", "Track Progress", "Reflect on Your Journey", "Community Support", "Progress Dashboard"],
                                 index=0)


if sidebar_option == "Introduction":
    st.markdown('<p class="title">Growth Mindset Challenge 🚀</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Develop, Learn, and Grow with a Positive Mindset</p>', unsafe_allow_html=True)

    
    animation_url = "https://assets5.lottiefiles.com/packages/lf20_7u95gs.json"  # Sample animation
    lottie_animation = load_lottie_url(animation_url)
    if lottie_animation:
        st_lottie(lottie_animation, speed=1, width=500, height=500, key="intro_animation")

    st.write("""
    A growth mindset is the belief that abilities and intelligence can be developed through hard work, perseverance, and learning from mistakes. 
    Let's embark on this journey together and embrace continuous learning. 🌱
    """)

elif sidebar_option == "Set Your Goal":
    st.markdown('<div class="card"><p class="subtitle">Set Your Growth Goal</p></div>', unsafe_allow_html=True)
    name = st.text_input("Enter Your Name", "")
    goal = st.text_input("What's your current learning goal?", "")
    
    
    progress = st.slider("How much progress have you made?", min_value=0, max_value=100, value=0)
    
    
    if st.button("Save Progress", key="progress_button", help="Save your current goal progress"):
        st.write(f"Great, {name}! You're {progress}% towards your goal. Keep going! 💪")
        
       
        animation_url = "https://assets7.lottiefiles.com/packages/lf20_tzlw3gcn.json"
        lottie_animation = load_lottie_url(animation_url)
        if lottie_animation:
            st_lottie(lottie_animation, speed=1, width=400, height=400, key="progress_animation")

    
    st.markdown('<div class="progress-bar"><div class="progress-bar-inner" style="width:' + str(progress) + '%"></div></div>', unsafe_allow_html=True)

elif sidebar_option == "Track Progress":
    st.markdown('<div class="card"><p class="subtitle">Track Your Growth Progress</p></div>', unsafe_allow_html=True)
    
    progress = st.slider("How much progress have you made?", min_value=0, max_value=100, value=50)
    if st.button("Save Progress"):
        st.write(f"Your current progress is {progress}%")
        
        
        animation_url = "https://assets2.lottiefiles.com/packages/lf20_kpw7d3gl.json"
        lottie_animation = load_lottie_url(animation_url)
        if lottie_animation:
            st_lottie(lottie_animation, speed=1, width=500, height=500, key="track_progress_animation")

    
    animation_url = "https://assets7.lottiefiles.com/packages/lf20_8m7itf6g.json"  # Circular progress animation
    lottie_animation = load_lottie_url(animation_url)
    if lottie_animation:
        st_lottie(lottie_animation, speed=1, width=400, height=400, key="progress_circle_animation")

elif sidebar_option == "Reflect on Your Journey":
    st.markdown('<div class="card"><p class="subtitle">Reflect on Your Journey</p></div>', unsafe_allow_html=True)
    reflection = st.text_area("What did you learn today?", "")
    
    if st.button("Save Reflection"):
        st.write(f"Reflection saved! Keep learning and growing. 🌱")
        
        
        animation_url = "https://assets4.lottiefiles.com/packages/lf20_gnxzzm5h.json"
        lottie_animation = load_lottie_url(animation_url)
        if lottie_animation:
            st_lottie(lottie_animation, speed=1, width=400, height=400, key="reflection_animation")

elif sidebar_option == "Community Support":
    st.markdown('<div class="card"><p class="subtitle">Join Our Community of Learners</p></div>', unsafe_allow_html=True)
    st.write("Engage with others and share your progress!")
    
    
    st.markdown("[Join our WhatsApp Group](https://chat.whatsapp.com/examplelink)")
    st.markdown("[Visit Our Community Forum](https://forum.example.com)")

elif sidebar_option == "Progress Dashboard":
    st.markdown('<div class="card"><p class="subtitle">Your Progress Dashboard</p></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="progress-card"><p><strong>Overall Progress:</strong> 65%</p></div>', unsafe_allow_html=True)
    
    
    progress_data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    days = [f"Day {i+1}" for i in range(len(progress_data))]

    fig, ax = plt.subplots()
    ax.plot(days, progress_data, marker='o', linestyle='-', color='orange')
    ax.set_title("Your Progress Over Time")
    ax.set_xlabel("Days")
    ax.set_ylabel("Progress (%)")
    ax.grid(True)
    st.pyplot(fig)

    st.write("### Achievement Unlocked!")
    st.markdown("<p><strong>You've reached 65% of your learning goal!</strong></p>", unsafe_allow_html=True)
    
    
    st.write("Keep up the great work, you're doing amazing!")


st.sidebar.markdown("### Keep Embracing Growth! 🌱")
st.sidebar.write("Remember, growth is a continuous journey. Embrace every challenge and keep striving for improvement!")


st.markdown("""
    <div class="chatbot">
        <p><strong>Chatbot:</strong> You're doing amazing! Keep pushing yourself to reach your goals, and remember, it's all about progress, not perfection! 💪</p>
    </div>
""", unsafe_allow_html=True)

