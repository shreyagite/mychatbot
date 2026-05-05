import streamlit as st
import math

# 1. Setup the Page
st.set_page_config(page_title="Engineering Chatbot", page_icon="🚀")
st.title("🤖 Technical Assistant Bot")
st.write("Welcome! I can chat with you or help you calculate projectile motion.")

# 2. The Chat Interface
user_name = st.text_input("First, what is your name?", "Student")
st.write(f"Hello {user_name}! Type a message or use the calculator below.")

# 3. Physics/Math Section (Equations)
st.divider()
st.header("🚀 Projectile Trajectory Calculator")
st.write("Let's calculate the horizontal range using the formula:")
st.latex(r"R = \frac{v^2 \sin(2\theta)}{g}")

# Input fields for the equation
v = st.number_input("Enter Initial Velocity (v) in m/s:", value=10.0)
angle_deg = st.slider("Select Launch Angle (θ) in degrees:", 0, 90, 45)
g = 9.81  # Acceleration due to gravity

# Calculations
angle_rad = math.radians(angle_deg)
range_r = (v**2 * math.sin(2 * angle_rad)) / g

# 4. Display the Result
st.success(f"The total horizontal range is: *{range_r:.2f} meters*")

# 5. Simple Chat Logic
user_message = st.text_input("Ask me something else:")
if user_message:
    if "hello" in user_message.lower():
        st.write("Hi there! Ready to solve some more equations?")
    elif "physics" in user_message.lower():
        st.write("Physics is great! We can add more formulas like $F = ma$ later.")
    else:
        st.write("That sounds interesting! I am still learning, but I can help with math.")