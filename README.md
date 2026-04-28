# 🌾 AgroSage AI — Farmer Advisory Agent

AgroSage AI is an agriculture-focused assistant that helps farmers with practical, local-style guidance using a mix of:

- **LLM reasoning (Google Gemini)**
- **Rule-based agronomy tools**
- **Live weather lookups (OpenWeatherMap)**

It accepts natural-language questions (for example: crop planning, disease symptoms, fertilizer choices), runs the relevant tools, and returns one clear advisory response.

## ✨ What it does

- Recommends crops from **soil type + season**
- Detects likely pest/disease issues from **symptom text**
- Suggests crop-specific fertilizer plans with **organic alternatives**
- Pulls current city weather and incorporates it into advice
- Combines tool outputs into a single farmer-friendly response via Gemini

## 🧠 How it works

1. User enters a farming question in the Streamlit app.
2. `agent.py` extracts intent signals (city, soil, season, crop, symptoms).
3. Relevant tools are called from `tools/`:
   - `weather.py`
   - `crop.py`
   - `pest.py`
   - `fertilizer.py`
4. Tool results + original query are sent to Gemini (`gemini_client.py`).
5. Final actionable advisory is shown in the UI.

## 📁 Project structure

```text
AgroSage-Ai/
├── app.py               # Streamlit frontend
├── agent.py             # Query parsing + tool orchestration
├── gemini_client.py     # Gemini API integration
├── config.py            # Environment/config loading
├── requirements.txt
├── README.md
├── LICENSE
└── tools/
    ├── __init__.py
    ├── crop.py          # Soil+season crop recommendation
    ├── fertilizer.py    # Crop fertilizer advice
    ├── pest.py          # Symptom-based pest detection
    └── weather.py       # OpenWeatherMap weather fetch
```

## ✅ Prerequisites

- Python **3.10+**
- A **Google Gemini API key**
- An **OpenWeatherMap API key** (free tier works)

## ⚙️ Setup

1. Clone the repository:

```bash
git clone https://github.com/adityamoghaa/AgroSage-Ai.git
cd AgroSage-Ai
```

2. Create and activate virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
# .venv\Scripts\activate         # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create `.env` in project root:

```env
GEMINI_API_KEY=your_gemini_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
```

| Variable | Required | Purpose |
|---|---|---|
| `GEMINI_API_KEY` | Yes | Generates final advisory response |
| `OPENWEATHER_API_KEY` | Yes (for weather queries) | Fetches live weather by city |

## ▶️ Run

```bash
streamlit run app.py
```

Open: `http://localhost:8501`

## 💬 Sample queries

- `I have loamy soil and it is winter. What crop should I grow?`
- `What is the weather in Nagpur?`
- `My wheat leaves have yellow spots. What should I do?`
- `What fertilizer should I use for rice?`
- `I have clay soil in monsoon season. My rice crop has white powder on leaves. What treatment and fertilizer should I use?`

## ⚠️ Current limitations

- Image upload is currently for reference display in UI; image content is not yet analyzed by a vision model.
- Pest and crop recommendations are rule-based and should be validated with local agronomy experts for field-critical decisions.

## 🛠 Tech stack

- Python
- Streamlit
- Google Gemini (`google-generativeai`)
- OpenWeatherMap API
- `requests`
- `python-dotenv`
- `Pillow`

## 📜 License

This project is licensed under the **MIT License**. See [`LICENSE`](LICENSE).
