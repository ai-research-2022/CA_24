# Importing necessary libraries
import streamlit as st  
import pandas as pd  
import matplotlib.pyplot as plt  

# Set the title of the Streamlit web application
st.title('My First Streamlit App')
# Write some introductory text in the app
st.write('This is a simple Streamlit app.')

# Input Widgets
# Create a text input box and store the user input in a variable
user_input = st.text_input("Enter your name")
# Display the name entered by the user
st.write('Your name is', user_input)

# Create a slider for selecting an age within a specified range
age = st.slider("Choose your age", 1, 100)
# Display the selected age
st.write("You are ", age, " years old")

# Create a button and check if it is clicked
if st.button('Say hello'):
    # If the button is clicked, display this message
    st.write('Hello there!')

# Displaying Data
# Create a DataFrame using pandas
data = pd.DataFrame({
    'first column': [1, 2, 3, 4],  # Data for the first column
    'second column': [10, 20, 30, 40]  # Data for the second column
})
# Use Streamlit to display the DataFrame in a table format
st.dataframe(data)

# Plotting Data
# Create a figure and an axes object for plotting
fig, ax = plt.subplots()
# Plot a histogram of the 'second column' with 5 bins
ax.hist(data['second column'], bins=5)
# Use Streamlit to display the matplotlib figure
st.pyplot(fig)

# Layouts and Containers
# Create two columns for layout
col1, col2 = st.columns(2)
# Content for the first column
with col1:
    st.header("Column 1")  # Set a header for the column
    st.write("Hello")  # Display some text
# Content for the second column
with col2:
    st.header("Column 2")  # Set a header for the column
    st.write("World")  # Display some text

# Create an expander to hide/show detailed explanation
with st.expander("See explanation"):
    # This text can be shown or hidden in the expander
    st.write("Here you could put in some really, really explanatory stuff.")
