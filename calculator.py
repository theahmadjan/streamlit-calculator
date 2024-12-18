import streamlit as st

st.title("Simple Calculator")

num1 = st.number_input("Enter the first number", value=0.0, step=1.0)
num2 = st.number_input("Enter the second number", value=0.0, step=1.0)

operation = st.selectbox("Select an operation", ["Add", "Subtract", "Multiply", "Divide"])

if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    result = num1 / num2 if num2 != 0 else "Division by zero is not allowed"

st.write("The result is:", result)
