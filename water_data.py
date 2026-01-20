from datetime import date, timedelta
import streamlit as st

LOG_FILE = 'water_log.txt'
DAILY_GOAL_OZ = 64

@st.cache_data
def read_log_entries():
    entries = []
    try:
        with open(LOG_FILE, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(': ')
                if len(parts) != 2:
                    continue

                date_text = parts[0].strip()
                rest = parts[1].strip()
                tokens = rest.split()

                if not tokens:
                    continue

                try:
                    ounces = int(tokens[0])
                except ValueError:
                    continue

                entries.append({"date": date_text, "ounces": ounces})
    except FileNotFoundError:
        return []
    return entries

def get_last_n_days_strings(n=7):
    today = date.today()
    return {(today - timedelta(days=i)).isoformat() for i in range(n)}

def get_week_total(entries, days=7):
    valid_days = get_last_n_days_strings(days)
    return sum(e["ounces"] for e in entries if e["date"] in valid_days)

def get_todays_logs(entries, today_str=None):
    if today_str is None:
        today_str = date.today().isoformat()
    return [e for e in entries if e["date"] == today_str]

def get_todays_total(entries, today_str=None):
    todays = get_todays_logs(entries, today_str)
    return sum(e["ounces"] for e in todays)

def get_past_week_data():
    entries = read_log_entries()
    past_week_data = []
    for i in range(7):
        day = (date.today() - timedelta(days=i)).isoformat()
        day_total = sum(e["ounces"] for e in entries if e["date"] == day)
        past_week_data.append(day_total)
    return past_week_data[::-1]

def check_streak(today=None, goal_oz=DAILY_GOAL_OZ):
    if today is None:
        today = date.today()

    entries = read_log_entries()

    totals_by_date = {}
    for entry in entries:
        totals_by_date[entry["date"]] = totals_by_date.get(entry["date"], 0) + entry["ounces"]

    streak = 0
    cursor = today
    while totals_by_date.get(cursor.isoformat(), 0) >= goal_oz:
        streak += 1
        cursor -= timedelta(days=1)

    return streak
        