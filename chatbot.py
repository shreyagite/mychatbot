import streamlit as st

# 1. Page Styling
st.set_page_config(page_title="Simple Math & Joke Bot")
st.title("🤖 My Friendly Helper Bot")

# 2. The Chatbot's Opening Line
st.write("### Hello! How can I help you today?")

# 3. Choose your path: Math, Jokes, or Chat
option = st.selectbox("What would you like to do?", ["Choose an option", "Solve Math", "Tell me a Joke", "Just Chat"])

# 4. Simple If-Else Logic
if option == "Solve Math":
    st.subheader("Basic Calculator")
    num1 = st.number_input("Enter first number:", value=0.0)
    num2 = st.number_input("Enter second number:", value=0.0)
    operation = st.radio("Choose operation:", ["Add", "Subtract", "Multiply", "Divide"])

    if st.button("Calculate"):
        if operation == "Add":
            st.success(f"Result: {num1 + num2}")
        elif operation == "Subtract":
            st.success(f"Result: {num1 - num2}")
        elif operation == "Multiply":
            st.success(f"Result: {num1 * num2}")
        elif operation == "Divide":
            if num2 != 0:
                st.success(f"Result: {num1 / num2}")
            else:
                st.error("You cannot divide by zero!")

elif option == "Tell me a Joke":
    st.subheader("Time for a Laugh! 😂")
    if st.button("Click for a Joke"):
        # Simple if-else for random-ish jokes
        import random
        jokes = [
            "Why did the student throw his clock out the window? He wanted to see time fly!",
            "Why don't scientists trust atoms? Because they make up everything!",
            "Parallel lines have so much in common. It’s a shame they’ll never meet.",
            "What do you call a fake noodle? An Impasta!"
        ]
        st.info(random.choice(jokes))

elif option == "Just Chat":
    user_msg = st.text_input("Type your message here:")
    if user_msg:
        if "hello" in user_msg.lower():
            st.write("Hi there! I'm your AI assistant.")
        elif "how are you" in user_msg.lower():
            st.write("I'm running smoothly on the cloud! How are you?")
        else:
            st.write("That's interesting! I'm still a simple bot, but I'm learning.")

elif option == "Choose an option":
    st.write("Please select an activity from the dropdown menu above.")