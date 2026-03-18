"""
Fertilizer advice tool.
Provides fertilizer recommendations for common crops, including organic alternatives.
"""


# Crop-specific fertilizer recommendations
FERTILIZER_MAP = {
    "wheat": {
        "primary": "Nitrogen-based fertilizer (e.g. Urea — 46% N)",
        "dosage": "120–150 kg/ha of Urea in split applications",
        "organic": "Well-decomposed farmyard manure (FYM) at 10–15 tonnes/ha, or vermicompost",
        "tip": "Apply nitrogen in 2–3 splits: at sowing, first irrigation, and tillering stage.",
    },
    "rice": {
        "primary": "NPK fertilizer (Nitrogen, Phosphorus, Potassium)",
        "dosage": "120 kg N, 60 kg P₂O₅, 40 kg K₂O per hectare",
        "organic": "Green manure (e.g. Dhaincha/Sesbania) and azolla as biofertilizer",
        "tip": "Use zinc sulphate (25 kg/ha) if zinc deficiency is observed.",
    },
    "cotton": {
        "primary": "Potassium-based fertilizer (Muriate of Potash — MOP)",
        "dosage": "60–80 kg K₂O per hectare along with balanced NPK",
        "organic": "Castor cake or neem cake at 2–3 tonnes/ha",
        "tip": "Potassium improves fibre quality and boll development.",
    },
    "millet": {
        "primary": "DAP (Diammonium Phosphate) + Urea",
        "dosage": "40–60 kg N and 20–30 kg P₂O₅ per hectare",
        "organic": "Compost or FYM at 5–8 tonnes/ha",
        "tip": "Millet requires less fertilizer than most cereals; avoid over-application.",
    },
    "maize": {
        "primary": "Nitrogen-based fertilizer (Urea) + DAP",
        "dosage": "120 kg N, 60 kg P₂O₅, 40 kg K₂O per hectare",
        "organic": "Poultry manure at 5 tonnes/ha or vermicompost",
        "tip": "Side-dress nitrogen at knee-high stage for best results.",
    },
    "soybean": {
        "primary": "Phosphorus-based fertilizer (Single Super Phosphate — SSP)",
        "dosage": "60–80 kg P₂O₅ per hectare; nitrogen fixation reduces N needs",
        "organic": "Rhizobium inoculant + rock phosphate",
        "tip": "Being a legume, soybean fixes its own nitrogen. Focus on phosphorus.",
    },
    "groundnut": {
        "primary": "Gypsum + SSP",
        "dosage": "250 kg Gypsum/ha at flowering + 30 kg P₂O₅/ha",
        "organic": "FYM at 5 tonnes/ha + Rhizobium culture",
        "tip": "Gypsum supplies calcium and sulfur, critical for pod filling.",
    },
}


def fertilizer_advice(crop: str) -> str:
    """
    Provide fertilizer recommendations for a given crop.

    Args:
        crop: Name of the crop (e.g. "wheat", "rice", "cotton").

    Returns:
        Detailed fertilizer advice including organic alternatives.
    """
    crop_lower = crop.strip().lower()
    info = FERTILIZER_MAP.get(crop_lower)

    if info:
        return (
            f"Fertilizer Advice for {crop.title()}:\n"
            f"  • Recommended fertilizer: {info['primary']}\n"
            f"  • Suggested dosage: {info['dosage']}\n"
            f"  • Organic alternative: {info['organic']}\n"
            f"  • Pro tip: {info['tip']}"
        )

    return (
        f"Fertilizer Advice for {crop.title()}:\n"
        f"  • No specific recommendation found in the database.\n"
        f"  • General advice: Use a balanced NPK fertilizer (e.g. 10-26-26 or 20-20-0).\n"
        f"  • Organic alternative: Well-decomposed farmyard manure or vermicompost.\n"
        f"  • Tip: Get a soil test to determine exact nutrient requirements."
    )
