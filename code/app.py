import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Sample Streamlit App")

# Sidebar for user input
st.sidebar.header("User Input")

# Add a slider to the sidebar
slider_value = st.sidebar.slider("Select a value", 0, 100, 50)

# Display the selected slider value
st.write(f"Slider Value: {slider_value}")

# Generate some sample data based on the slider value
data = pd.DataFrame({
    'x': np.arange(1, 101),
    'y': np.arange(1, 101) * slider_value
})

# Display the data
st.write("Generated Data", data)

# Line chart using the generated data
st.line_chart(data)

# File uploader in the sidebar
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded file
    df = pd.read_csv(uploaded_file)

    # Display the contents of the file
    st.write("Uploaded File Data", df)

    # Display a summary of the data
    st.write("Summary Statistics")
    st.write(df.describe())

# Footer
st.write("This is a sample Streamlit app.")
