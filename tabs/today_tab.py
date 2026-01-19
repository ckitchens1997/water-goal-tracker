import streamlit as st
from water_data import (
    DAILY_GOAL_OZ,
    read_log_entries,
    get_todays_logs,
    get_todays_total
)

def render():
    """Render the Today's Water Intake tab"""
    entries = read_log_entries()
    total = get_todays_total(entries)
    todays_logs = get_todays_logs(entries)
    remaining = max(DAILY_GOAL_OZ - total, 0)
    progress = 0 if DAILY_GOAL_OZ == 0 else min(total / DAILY_GOAL_OZ, 1.0)
    
    st.subheader(f"Today's Water Intake - Daily Goal: {DAILY_GOAL_OZ} oz")
    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        st.progress(progress)
        st.write(f"Percent of Goal Achieved: {progress * 100:.2f}%")

    with col2:
        st.write(f'Total Ounces Remaining: {remaining}/{DAILY_GOAL_OZ} oz\n')
        st.write(f'Logs for Today:\n\n{todays_logs}')

    st.divider()

    if total >= DAILY_GOAL_OZ:
        st.success('Congratulations! You have met your daily water intake goal! 🎉')
    
    if total < DAILY_GOAL_OZ:
        st.info('Keep going! You have not yet reached your daily water intake goal.')