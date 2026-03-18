"""
Crop recommendation tool.
Provides rule-based crop suggestions based on soil type and season.
"""


# Mapping of (soil_type, season) -> recommended crop
CROP_RULES = {
    ("loamy", "winter"): "wheat",
    ("loamy", "summer"): "maize",
    ("loamy", "monsoon"): "rice",
    ("black", "winter"): "cotton",
    ("black", "summer"): "cotton",
    ("black", "monsoon"): "soybean",
    ("clay", "winter"): "rice",
    ("clay", "summer"): "rice",
    ("clay", "monsoon"): "rice",
    ("sandy", "winter"): "millet",
    ("sandy", "summer"): "millet",
    ("sandy", "monsoon"): "groundnut",
}

# Default recommendations when no exact rule matches
SOIL_DEFAULTS = {
    "loamy": "wheat or maize",
    "black": "cotton or soybean",
    "clay": "rice",
    "sandy": "millet or groundnut",
}


def crop_recommendation(soil: str, season: str) -> str:
    """
    Recommend a crop based on soil type and season.

    Args:
        soil: Type of soil (e.g. "loamy", "black", "clay", "sandy").
        season: Current season (e.g. "winter", "summer", "monsoon").

    Returns:
        A recommendation string with the suggested crop and brief reasoning.
    """
    soil_lower = soil.strip().lower()
    season_lower = season.strip().lower()

    crop = CROP_RULES.get((soil_lower, season_lower))

    if crop:
        return (
            f"Crop Recommendation:\n"
            f"  • Soil type: {soil.title()}\n"
            f"  • Season: {season.title()}\n"
            f"  • Recommended crop: {crop.title()}\n"
            f"  • Reason: {crop.title()} grows well in {soil_lower} soil during the {season_lower} season."
        )

    # Try a default recommendation based on soil alone
    default_crop = SOIL_DEFAULTS.get(soil_lower)
    if default_crop:
        return (
            f"Crop Recommendation:\n"
            f"  • Soil type: {soil.title()}\n"
            f"  • Season: {season.title()}\n"
            f"  • Suggested crop(s): {default_crop.title()}\n"
            f"  • Note: No specific rule for this soil-season combination. "
            f"These crops generally do well in {soil_lower} soil."
        )

    return (
        f"Crop Recommendation:\n"
        f"  • Soil type: {soil.title()}\n"
        f"  • Season: {season.title()}\n"
        f"  • No specific recommendation available for this combination.\n"
        f"  • Tip: Consult your local agricultural extension office for region-specific advice."
    )
