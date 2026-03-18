"""
Streamlit UI for the AI Farmer Advisory Agent.
Provides a simple interface for farmers to ask questions and receive AI-powered advice.
"""

import streamlit as st
from agent import farmer_agent

# ---------------------------------------------------------------------------
# Page configuration
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="AI Farmer Advisory Agent",
    page_icon="🌾",
    layout="centered",
)

# ---------------------------------------------------------------------------
# Custom styling
# ---------------------------------------------------------------------------
st.markdown(
    """
    <style>
    .main-header {
        text-align: center;
        padding: 1rem 0;
    }
    .main-header p {
        font-size: 1.1rem;
        opacity: 0.8;
    }
    .advice-box {
        background-color: #f6fff8;
        color: #1a1a1a;
        border-left: 5px solid #4CAF50;
        padding: 1.2rem;
        border-radius: 0.5rem;
        margin-top: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
st.markdown(
    """
    <div class="main-header">
        <h1>🌾 AI Farmer Advisory Agent</h1>
        <p>Ask any farming question — get AI-powered advice backed by real data.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

# ---------------------------------------------------------------------------
# Input section
# ---------------------------------------------------------------------------
st.subheader("🧑‍🌾 Ask Your Question")

query = st.text_area(
    label="Describe your farming query below:",
    placeholder=(
        "Examples:\n"
        "• I have loamy soil and it is winter. What crop should I grow?\n"
        "• What is the weather in Nagpur?\n"
        "• My wheat leaves have yellow spots. What should I do?\n"
        "• What fertilizer should I use for rice?"
    ),
    height=140,
    key="farmer_query",
)

# Optional image uploader
uploaded_image = st.file_uploader(
    "📷 Upload a crop/field image (optional)",
    type=["jpg", "jpeg", "png"],
    help="Upload an image of your crop or field for reference.",
)

if uploaded_image:
    from PIL import Image
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded image", use_container_width=True)

# ---------------------------------------------------------------------------
# Action button
# ---------------------------------------------------------------------------
if st.button("🌿 Get Advice", type="primary", use_container_width=True):
    if not query.strip():
        st.warning("⚠️ Please enter a question before clicking **Get Advice**.")
    else:
        with st.spinner("🔍 Analysing your query and gathering data…"):
            response = farmer_agent(query)

        st.divider()
        st.subheader("📋 Advisory Report")
        st.markdown(
            f'<div class="advice-box">{response}</div>',
            unsafe_allow_html=True,
        )

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.divider()
st.caption(
    "Powered by Amazon Nova via AWS Bedrock · Weather data from OpenWeatherMap · "
    "Built with ❤️ for Indian farmers"
)
