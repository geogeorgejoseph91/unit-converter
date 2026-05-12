# 🔄 Unit Converter

A multi-category unit converter built with **Python** and **Streamlit**.

## 📖 Description

This project converts values between units across **9 categories**:

| Category | Units Supported |
|---|---|
| 📏 Length | meter, km, cm, mm, mile, yard, foot, inch, nautical mile |
| ⚖️ Weight | kg, g, mg, ton, pound, ounce, stone |
| 🌡️ Temperature | Celsius, Fahrenheit, Kelvin |
| 🧪 Volume | liter, mL, m³, gallon, quart, pint, cup, fl oz |
| ⏱️ Time | second, ms, minute, hour, day, week, month, year |
| 🚀 Speed | m/s, km/h, mph, knot, ft/s |
| 🟦 Area | m², km², cm², hectare, acre, ft², in², mi² |
| ⚡ Energy | joule, kJ, calorie, kcal, Wh, kWh, BTU |
| 💾 Data | byte, KB, MB, GB, TB, bit, KiB, MiB, GiB |

## 📁 Project Structure

```
unit_converter/
├── app.py              # Streamlit web interface
├── conversions.py      # Conversion logic & unit definitions
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## 🚀 How to Run

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app:**
   ```bash
   streamlit run app.py
   ```

3. **Open your browser** — Streamlit will auto-open at `http://localhost:8501`.

## 🧠 How It Works

### Linear Conversions (Length, Weight, Volume, etc.)
Each unit is stored with a factor representing how many **base units** it equals.

```
Step 1:  input_value × source_factor = value in base unit
Step 2:  base_value ÷ target_factor  = final result
```

**Example — Convert 5 km to miles:**
- Step 1: `5 × 1000 = 5000` meters (base unit)
- Step 2: `5000 ÷ 1609.344 ≈ 3.107` miles

### Temperature Conversions (Special Case)
Temperature can't use a simple multiplier because the zero points differ
(0°C ≠ 0°F ≠ 0K). Instead, we always go through **Celsius** as a bridge:

```
°C → °F :  F = C × 9/5 + 32
°F → °C :  C = (F − 32) × 5/9
°C → K  :  K = C + 273.15
K  → °C :  C = K − 273.15
```

## 🎤 Presentation Talking Points

1. **Why Streamlit?** Pure Python, no HTML/CSS/JS needed. Code-to-UI in minutes.
2. **Separation of concerns:** Conversion logic (`conversions.py`) is fully
   independent from the UI (`app.py`) — easy to test and reuse.
3. **Dictionary-based design:** Adding a new unit is just one line in a dict.
4. **Why is temperature special?** It has non-zero offsets, so it needs
   formulas, not factors.
5. **Possible extensions:** currency conversion (with live API), unit history,
   favorites, dark mode toggle.

## 👤 Author

Built as a course project.
