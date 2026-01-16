import streamlit as st
from datetime import date

LOG_FILE = 'water_log.txt'


# --- Title of program ---
st.title('Water Goal Tracker 💧')

if 'flash_msg' not in st.session_state:
    st.session_state.flash_msg = ''
if 'flash_type' not in st.session_state:
    st.session_state.flash_type = ''

# --- Flashing Confirm or Cancel options ---
if st.session_state.flash_msg:
    if st.session_state.flash_type == "success":
        st.success(st.session_state.flash_msg)
    elif st.session_state.flash_type == "info":
        st.info(st.session_state.flash_msg)
    else:
        st.warning(st.session_state.flash_msg)

    # optional: clear it so it only shows once
    st.session_state.flash_msg = ''
    st.session_state.flash_type = ''

# --- init session state ---
if 'pending_confirm' not in st.session_state:
    st.session_state.pending_confirm = False
if 'pending_oz' not in st.session_state:
    st.session_state.pending_oz = 0

# --- asking user for input ---
oz = st.number_input('How many ounces of water have you drank today?', min_value=0, step=1)

if st.button('Log Water Intake'):
    st.session_state.pending_confirm = True
    st.session_state.pending_oz = int(oz)

if st.session_state.pending_confirm:
    st.warning(f"Confirm logging **{st.session_state.pending_oz} oz** for **{date.today().isoformat()}**?")

    col1, col2 = st.columns(2)

    with col1:
        if st.button('Confirm'):
            with open(LOG_FILE, 'a') as file:
                file.write(f'{date.today()}: {st.session_state.pending_oz} ounces\n')
            
            st.session_state.flash_msg = f'Logged {st.session_state.pending_oz} ounces of water for {date.today().isoformat()}'
            st.session_state.flash_type = 'success'
            
            st.session_state.pending_confirm = False
            st.session_state.pending_oz = 0
            st.rerun()
    
    with col2:
        if st.button('Cancel'):
            st.session_state.flash_msg = 'Log cancelled.'
            st.session_state.flash_type = 'info'

            st.session_state.pending_confirm = False
            st.session_state.pending_oz = 0
            st.rerun()

      