# Life Compass

Life Compass is a **FastAPI-based backend project** that generates an explainable **purpose and development profile** using precise astronomical calculations of lunar nodes.

The goal of the project is **not astrology as belief**, but an engineering-style experiment:
translating **astronomical node positions** into structured life-direction logic — with all calculations deterministic, transparent, and defensible at interview level.

---

## ✨ Key Features

* **FastAPI backend** with clean, modular architecture
* **Swiss Ephemeris (pyswisseph)** as the single source of astronomical truth
* Deterministic calculations (no randomization, no tables by date)
* Explainable business logic layered on top of raw astronomical data
* Portfolio-level backend project

---

## 🧠 What the API Calculates

Based on **date, time, and place of birth**, the service computes:

* ☋ **South Node** – habitual patterns and comfort zone
* ☊ **North Node** – development vector and growth direction
* ♈ **Node sign axis** – qualitative direction of growth
* 🏠 **Node house axis** – life areas where purpose is lived

Only lunar nodes are used.
No aspects. No additional planets.
All calculations are performed via **Swiss Ephemeris**, not simplified tables.

---

## 🧩 Purpose Model

The purpose profile is built as a clear axis:

1. **South Node sign** → default strategies and familiar behavior
2. **South Node house** → where these patterns usually play out
3. **North Node sign** → qualities to consciously develop
4. **North Node house** → life domain where growth happens

The result focuses on:

* transition logic (from → to)
* growth recommendations
* risks of staying in autopilot
* human-readable explanation

---

## 🚀 Getting Started

### Requirements

* Python **3.12.x** (required)
* Windows OS

### Installation

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### Run the Server

```bash
python -m uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## 📥 API Example

### Request

```json
{
  "birth_date": "1995-11-18",
  "birth_time": "14:30",
  "birth_place": "Minsk, Belarus"
}
```

### Response (example)

```json
{
  "title": "Sagittarius South Node (9th House) → Gemini North Node (3rd House)",
  "bridge": "From absolute truth → to dialogue.",
  "sections": [
    {
      "focus": "☋ South Node in Sagittarius",
      "meaning": "A tendency toward certainty, teaching others, and abstract worldview thinking."
    },
    {
      "focus": "☋ South Node in the 9th House",
      "meaning": "Living through beliefs, ideologies, and theoretical frameworks.",
      "direction": "from certainty → to curiosity"
    },
    {
      "focus": "☊ North Node in Gemini",
      "meaning": "Growth through listening, asking questions, and exchanging perspectives."
    },
    {
      "focus": "☊ North Node in the 3rd House",
      "meaning": "Development unfolds through communication, learning, and everyday dialogue.",
      "direction": "from monologue → to conversation"
    }
  ],
  "recommendations": [
    "Practice curiosity instead of certainty.",
    "Develop growth through communication and learning.",
    "Notice when abstract beliefs replace real dialogue.",
    "Keep the core transition in mind."
  ],
  "motto": "Truth is born in dialogue."
}
```

---

## 🏗 Architecture Overview

```
LifeCompass/
├─ app/
│  ├─ api/            # FastAPI routes
│  ├─ services/       # Astronomical calculations & purpose logic
│  ├─ schemas/        # Pydantic models
│  └─ main.py
├─ data/              # Places and coordinates
└─ requirements.txt
```

---

## 📄 License

MIT
