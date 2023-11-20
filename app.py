import streamlit as st
from streamlit_echarts import st_echarts
import pandas as pd

# Sample data for the table and the bar chart
df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4],
    'Column 2': [10, 20, 30, 40],
    'Column 3': [100, 200, 300, 400]
})

bar_chart_data = {
    'xAxis': {
        'type': 'category',
        'data': ['A', 'B', 'C', 'D']
    },
    'yAxis': {
        'type': 'value'
    },
    'series': [{
        'data': [120, 200, 150, 80],
        'type': 'bar'
    }]
}

# Streamlit layout
st.sidebar.image('path_to_logo.png')  # Replace 'path_to_logo.png' with the path to your company logo image
st.sidebar.button('About Us')
st.sidebar.button('Products')
st.sidebar.button('Pricing')

st.sidebar.checkbox('Option 1')
st.sidebar.selectbox('Dropdown', ['Choice 1', 'Choice 2', 'Choice 3'])

st.title('Page Title')
st.write("This is a placeholder paragraph under the page title. It should contain information about the page content, details or any other relevant text.")

st.table(df)

st_echarts(options=bar_chart_data, height="400px")