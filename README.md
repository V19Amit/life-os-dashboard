# 📱 Life-OS Wellbeing Dashboard

An AI-powered digital wellbeing dashboard that analyzes screen time habits, visualizes app usage patterns, and provides personalized productivity coaching using Google Gemini AI.

---

## 🚀 Project Overview

**Life-OS Wellbeing Dashboard** helps users monitor their digital habits by analyzing daily screen time data. It provides:

- 📊 Screen time analytics
- 📈 Usage trend visualization
- 🎯 Daily goal tracking
- 🤖 AI-powered productivity coaching
- 🎭 Personalized digital wellbeing avatar

The application combines **Data Analytics + Generative AI** to encourage healthier digital habits.

---

## ✨ Features

### 📱 Screen Time Tracking
- Analyze daily mobile application usage.
- Calculate total screen time.
- Identify the most used application.
- Compare usage with daily goals.

### 📊 Interactive Dashboard
- Bar chart for application-wise usage.
- Line chart for screen time trends.
- Date-based filtering.
- Goal-based performance monitoring.

### 🤖 AI Productivity Coach
Powered by **Google Gemini AI**.

Provides:
- Screen time analysis
- Positive habit recognition
- Improvement suggestions
- Real-world activity recommendations

### 🎭 AI Digital Avatar
Generates a personalized avatar based on digital behavior:

- Excessive screen time → Digital addiction awareness avatar
- Healthy usage → Productive lifestyle avatar

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Framework
- Streamlit

### Data Processing
- Pandas

### Generative AI
- Google Gemini API

### Visualization
- Streamlit Charts

### Environment Management
- Python-dotenv

### AI Image Generation
- Pollinations AI

---

## 📂 Project Structure

```
Life-OS-Wellbeing-Dashboard/
│
├── app.py
├── screentime.csv
├── requirements.txt
├── .env
├── README.md
│
└── assets/
    └── screenshots/
```

---

## 📊 Dataset

The project uses `screentime.csv`.

Example format:

| Date | App_Name | Category | Minutes_Used |
|------|----------|----------|--------------|
| 2026-07-01 | YouTube | Entertainment | 120 |
| 2026-07-01 | Chrome | Productivity | 60 |
| 2026-07-01 | WhatsApp | Social | 45 |

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone <repository-url>
cd Life-OS-Wellbeing-Dashboard
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Gemini API Key

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

---

### 5. Run Application

```bash
streamlit run app.py
```

The dashboard will open in your browser.

---

## 🔑 Environment Variables

| Variable | Description |
|----------|-------------|
| GEMINI_API_KEY | Google Gemini API authentication key |

---

## 📸 Application Workflow

```
User Screen Time Data
          |
          ↓
Data Processing using Pandas
          |
          ↓
Dashboard Visualization
          |
          ↓
Gemini AI Analysis
          |
          ↓
Personalized Productivity Advice
          |
          ↓
Digital Wellbeing Avatar
```

---

## 🎯 Future Enhancements

- Mobile application integration
- Real-time screen time tracking
- User authentication
- Database integration
- Weekly wellbeing reports
- AI habit prediction model
- Voice-based productivity assistant

---

## 👨‍💻 Author

**Amit Verma**

B.Tech Computer Science (Data Science)

---

## 📜 License

This project is created for educational and learning purposes.
## 🌐 Live Demo

[Open Life-OS Wellbeing Dashboard](https://life-os-dashboard-bsdbhtnydyosndseprttxx.streamlit.app/)

## 📂 Source Code

[GitHub Repository](https://github.com/V19Amit/life-os-dashboard)
