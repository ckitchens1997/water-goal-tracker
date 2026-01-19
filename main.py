import streamlit as st
from tabs import log_tab, today_tab, week_tab, settings_tab

# --- Title of program ---
st.title('Water Goal Tracker 💧')

tab_log, tab_today, tab_week, tab_settings = st.tabs(['Log', 'Today', 'Past Week', 'Settings'])

with tab_log:
    log_tab.render()

with tab_today:
    today_tab.render()

with tab_week:
    week_tab.render()

with tab_settings:
    settings_tab.render()