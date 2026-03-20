# 🌾 AI Farmer Advisory Agent

An agentic AI system that helps farmers with **crop recommendations**, **weather alerts**, **pest detection**, and **fertilizer advice** — powered by **Google Gemini**.

The agent analyses natural-language questions, dispatches to specialised tools, and uses the Gemini LLM to produce a clear, actionable advisory.

---

## 📁 Project Structure

```
ai-farmer-advisor/
├── app.py              # Streamlit UI
├── agent.py            # Agent orchestration logic
├── gemini_client.py    # Google Gemini client
├── config.py           # Environment variable loader
├── tools/
│   ├── __init__.py
│   ├── weather.py      # OpenWeatherMap integration
│   ├── crop.py         # Rule-based crop recommendation
│   ├── pest.py         # Symptom-based pest detection
│   └── fertilizer.py   # Crop-specific fertilizer advice
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone <repo-url>
cd ai-farmer-advisor
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
# venv\Scripts\activate    # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
```

| Variable | Description |
|---|---|
| `GEMINI_API_KEY` | Your Google Gemini API key |
| `OPENWEATHER_API_KEY` | Free API key from [openweathermap.org](https://openweathermap.org/api) |

---

## 🚀 Run the App

```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`.

---

## 💬 Example Queries

| Query | Tools Used |
|---|---|
| *I have loamy soil and it is winter. What crop should I grow?* | Crop |
| *What is the weather in Nagpur?* | Weather |
| *My wheat leaves have yellow spots. What should I do?* | Pest, Fertilizer |
| *What fertilizer should I use for rice?* | Fertilizer |
| *I have clay soil in monsoon season. My rice crop has white powder on leaves. What fertilizer and treatment should I use?* | Crop, Pest, Fertilizer |

---

## 🛠 Tech Stack

- **Python 3.10+**
- **Streamlit** — interactive web UI
- **Google Gemini** — LLM for advisory generation
- **google-generativeai** — Google GenAI SDK
- **requests** — HTTP client for weather API
- **python-dotenv** — `.env` file loading
- **Pillow** — image handling

---.
