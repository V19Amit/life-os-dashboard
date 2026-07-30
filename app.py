import streamlit as st
import pandas as pd
import os
import requests
from dotenv import load_dotenv
from google import genai

load_dotenv()

st.set_page_config(
    page_title="Life-OS Wellbeing Dashboard",
    page_icon="📱",
    layout="wide"
)

@st.cache_resource
def get_client():
    return genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

client = get_client()

st.title("📱 Life-OS Wellbeing Dashboard")
st.write("Track your digital wellbeing and receive AI-powered productivity coaching.")

# Load CSV
df = pd.read_csv("screentime.csv")


# Sidebar
st.sidebar.header("Dashboard Controls")

dates = sorted(df["Date"].unique())

selected_date = st.sidebar.selectbox(
    "Select Date",
    dates
)

daily_goal = st.sidebar.slider(
    "Daily Goal (Minutes)",
    60,
    600,
    300,
    30
)

# Filter data
day_df = df[df["Date"] == selected_date]
total_minutes = day_df["Minutes_Used"].sum()

most_used_app = day_df.loc[
    day_df["Minutes_Used"].idxmax(),
    "App_Name"
]

delta = total_minutes - daily_goal

col1, col2, col3 = st.columns(3)

col1.metric(
    "📱 Total Screen Time",
    f"{total_minutes} min",
    delta=f"{delta} min",
    delta_color="inverse"
)

col2.metric(
    "🔥 Most Used App",
    most_used_app
)

col3.metric(
    "🎯 Daily Goal",
    f"{daily_goal} min"
)
st.divider()

st.subheader("📊 Daily App Usage")

st.bar_chart(
    day_df.set_index("App_Name")["Minutes_Used"]
)

trend = df.groupby("Date")["Minutes_Used"].sum()

st.subheader("📈 14-Day Screen Time Trend")

st.line_chart(trend)
st.divider()

st.header("🤖 AI Productivity Coach")

summary = day_df.groupby("Category")["Minutes_Used"].sum().to_string()

prompt = f"""
You are an expert productivity and wellness coach.

Today's screen time:

{summary}

Give:
1. Short analysis.
2. What the user did well.
3. What the user should improve.
4. Suggest real-world activities instead of excessive screen time.

Keep response under 200 words.
"""

if st.button("Get AI Advice"):

    with st.spinner("Analyzing your digital habits..."):

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        if total_minutes > daily_goal:
            st.warning(response.text)
        else:
            st.info(response.text)
st.divider()

st.header("🎭 Today's Digital Avatar")

from urllib.parse import quote

if total_minutes > daily_goal:
    avatar_prompt = "lazy zombie staring at a glowing phone, digital addiction, cinematic"
else:
    avatar_prompt = "focused warrior studying peacefully, productive, cinematic"

image_url = f"https://image.pollinations.ai/prompt/{quote(avatar_prompt)}"

st.image(image_url, use_container_width=True)

try:
    response = requests.get(image_url, timeout=10)
    response.raise_for_status()

    st.download_button(
        "⬇️ Download Avatar",
        response.content,
        file_name="life_os_avatar.png",
        mime="image/png"
    )

except Exception as e:
    st.warning(f"Image download unavailable: {e}")