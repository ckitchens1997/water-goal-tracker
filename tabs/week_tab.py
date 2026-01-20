import streamlit as st
from water_data import get_past_week_data, get_week_total, read_log_entries

def render():
    """Render the Past Week Water Intake tab"""
    st.subheader('Past Week Water Intake')
    entries = read_log_entries()
    week_total = get_week_total(entries, days=7)
    
    past_week_data = get_past_week_data()
    if past_week_data:
        st.line_chart(past_week_data)
    else:
        st.info("No data available for the past week.")

    st.write(f'Total water intake for the past week: {week_total} oz')
    st.write(f'Average daily water intake for the past week: {week_total / 7:.2f} oz')