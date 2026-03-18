"""
Pest detection tool.
Identifies common pests/diseases from symptom descriptions and suggests treatments.
"""


# Symptom keywords mapped to (pest/disease name, treatment suggestion)
PEST_DATABASE = [
    {
        "keywords": ["yellow spots", "yellow", "yellowing", "rust"],
        "pest": "Leaf Rust",
        "description": "A fungal disease that appears as yellow-orange pustules on leaves.",
        "treatment": (
            "  • Apply fungicides such as Propiconazole or Tebuconazole.\n"
            "  • Remove and destroy infected leaves.\n"
            "  • Use resistant crop varieties when available.\n"
            "  • Organic option: Neem oil spray (2-3 ml per litre of water)."
        ),
    },
    {
        "keywords": ["holes", "eaten", "caterpillar", "chewed"],
        "pest": "Caterpillars (Lepidoptera larvae)",
        "description": "Larvae that chew through leaves, creating holes and ragged edges.",
        "treatment": (
            "  • Apply Bacillus thuringiensis (Bt) based biopesticide.\n"
            "  • Handpick caterpillars in small-scale farming.\n"
            "  • Use pheromone traps to monitor and reduce adult moth populations.\n"
            "  • Organic option: Neem-based insecticide spray."
        ),
    },
    {
        "keywords": ["white powder", "powdery", "white coating", "mildew"],
        "pest": "Powdery Mildew",
        "description": "A fungal infection that coats leaves with a white, powdery substance.",
        "treatment": (
            "  • Apply sulfur-based fungicide or Potassium bicarbonate spray.\n"
            "  • Ensure proper spacing between plants for air circulation.\n"
            "  • Avoid overhead watering.\n"
            "  • Organic option: Milk spray (1 part milk to 9 parts water)."
        ),
    },
    {
        "keywords": ["wilting", "wilt", "drooping"],
        "pest": "Fusarium Wilt",
        "description": "A soil-borne fungal disease causing wilting and yellowing of plants.",
        "treatment": (
            "  • Use disease-free seeds and resistant varieties.\n"
            "  • Practice crop rotation.\n"
            "  • Solarize soil before planting.\n"
            "  • Organic option: Apply Trichoderma-based biocontrol agents."
        ),
    },
    {
        "keywords": ["black spots", "dark spots", "blight"],
        "pest": "Blight",
        "description": "A bacterial or fungal disease causing dark, water-soaked lesions on leaves.",
        "treatment": (
            "  • Apply copper-based fungicides.\n"
            "  • Remove affected plant parts immediately.\n"
            "  • Ensure good drainage and air circulation.\n"
            "  • Organic option: Bordeaux mixture spray."
        ),
    },
]


def detect_pest(symptoms: str) -> str:
    """
    Detect potential pests or diseases from a symptom description.

    Args:
        symptoms: A description of observed symptoms (e.g. "yellow spots on leaves").

    Returns:
        A diagnosis with treatment suggestions, or a fallback message if no match.
    """
    symptoms_lower = symptoms.strip().lower()
    matches = []

    for entry in PEST_DATABASE:
        for keyword in entry["keywords"]:
            if keyword in symptoms_lower:
                matches.append(entry)
                break  # Avoid duplicate matches from the same entry

    if not matches:
        return (
            f"Pest Detection:\n"
            f"  • Symptoms: {symptoms}\n"
            f"  • No matching pest or disease found in the database.\n"
            f"  • Tip: Take a clear photo of the affected plant and consult your "
            f"local agricultural extension officer for accurate diagnosis."
        )

    result_parts = [f"Pest Detection (based on symptoms: \"{symptoms}\"):\n"]
    for match in matches:
        result_parts.append(
            f"  🔍 {match['pest']}\n"
            f"     {match['description']}\n"
            f"     Recommended treatment:\n"
            f"{match['treatment']}\n"
        )

    return "\n".join(result_parts)
