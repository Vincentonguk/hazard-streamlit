import os
import time
import hashlib
import random
import datetime as dt
import pandas as pd
import streamlit as st

# ---------- PAGE & THEME ----------
st.set_page_config(page_title="🚨 Hazard Security Dashboard", page_icon="🛡️", layout="wide")

# CSS para “cara de produto”
st.markdown("""
    <style>
    .main {
        background-color: #0e1a2b;
        color: #f0f0f0;
    }
    .stMetric {
        background: #142b47;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.4);
    }
    </style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.title("🛡️ Hazard Security Dashboard")
st.markdown("Real-time monitoring and security alerts for companies & communities.")

# ---------- METRICS ----------
col1, col2, col3, col4 = st.columns(4)
col1.metric("Active Monitors", 142, "+12")
col2.metric("Security Alerts", 7, "-3")
col3.metric("Community Members", 1247, "+89")
col4.metric("Detection Rate", "97.8%", "+0.5%")

# ---------- RECENT ALERTS ----------
st.subheader("⚠️ Recent Alerts (Simulation)")
alerts = pd.DataFrame({
    "Level": ["Medium", "Low", "Info", "High"],
    "Description": [
        "Unusual Activity – King’s Road, Chelsea",
        "New Device – Victoria Street, Westminster",
        "Package Delivery – Fulham Broadway",
        "Unauthorized Access – Sloane Square"
    ],
    "Time": ["2 min ago", "5 min ago", "12 min ago", "25 min ago"]
})
st.table(alerts)

# ---------- SYSTEM STATUS ----------
st.subheader("📡 System Status")
status_cols = st.columns(2)
with status_cols[0]:
    st.success("Network Health: Excellent")
    st.info("Data Processing: Normal")
with status_cols[1]:
    st.success("GDPR Compliance: Verified")
    st.write("Community Trust Score: **9.2/10**")

# ---------- EMERGENCY BUTTON ----------
st.subheader("🚨 Emergency Action")
if st.button("Trigger Emergency Alert 🚨"):
    with st.spinner("🔔 Notifying authorities..."):
        time.sleep(2)
    st.error("✅ Authorities have been notified!")
