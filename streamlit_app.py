import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Initialize the Streamlit app
st.title('My First Streamlit App')

# Add introductory text explaining the purpose of the app
st.write('This is a simple Streamlit app to demonstrate basic functionalities including user input, data display, and interactive controls.')

# 2. User Input Controls
name = st.text_input("Enter your name", "")
if name:
    st.write(f"Hello {name}!")

age = st.slider("Select your age", 1, 100)
st.write("You've selected:", age)

# 3. Button Interaction
if st.button('Say hello'):
    st.write('Hello there!')

# 4. Data Manipulation and Display
data = pd.DataFrame({
    "Numbers": range(100),
    "Squares": [i**2 for i in range(100)]
})
st.dataframe(data)  # Display the DataFrame

# 5. Data Visualization
fig, ax = plt.subplots()
ax.hist(data['Squares'], bins=10, color='blue')
ax.set_title('Histogram of Squares')
ax.set_xlabel('Squares')
ax.set_ylabel('Frequency')
st.pyplot(fig)

# 6. Advanced Layouts
col1, col2 = st.columns(2)
with col1:
    st.header("Hello")
with col2:
    st.header("World")

expander = st.expander("More Information")
expander.write("This is an expander widget to show or hide additional information. Toggle it to see more or less information.")
