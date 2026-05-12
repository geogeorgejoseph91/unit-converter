"""
Unit Converter - Conversion Logic Module
=========================================
This module contains all unit definitions and conversion functions.

Strategy:
  - For LINEAR units (length, weight, etc.): each unit stores how many
    base units it equals. To convert: value -> base unit -> target unit.
  - For TEMPERATURE: needs special handling because it has non-zero
    offsets (0°C is NOT 0°F), so we can't use a simple multiplier.
"""

# ---------------------------------------------------------------------------
# LINEAR UNIT DEFINITIONS
# Each dictionary maps "Unit Name" -> "how many base units = 1 of this unit"
# ---------------------------------------------------------------------------

# Base unit: meter
LENGTH_UNITS = {
    "Meter (m)": 1.0,
    "Kilometer (km)": 1000.0,
    "Centimeter (cm)": 0.01,
    "Millimeter (mm)": 0.001,
    "Mile (mi)": 1609.344,
    "Yard (yd)": 0.9144,
    "Foot (ft)": 0.3048,
    "Inch (in)": 0.0254,
    "Nautical Mile (nmi)": 1852.0,
}

# Base unit: kilogram
WEIGHT_UNITS = {
    "Kilogram (kg)": 1.0,
    "Gram (g)": 0.001,
    "Milligram (mg)": 0.000001,
    "Metric Ton (t)": 1000.0,
    "Pound (lb)": 0.453592,
    "Ounce (oz)": 0.0283495,
    "Stone (st)": 6.35029,
}

# Base unit: liter
VOLUME_UNITS = {
    "Liter (L)": 1.0,
    "Milliliter (mL)": 0.001,
    "Cubic Meter (m³)": 1000.0,
    "Gallon US (gal)": 3.78541,
    "Quart US (qt)": 0.946353,
    "Pint US (pt)": 0.473176,
    "Cup US": 0.24,
    "Fluid Ounce US (fl oz)": 0.0295735,
}

# Base unit: second
TIME_UNITS = {
    "Second (s)": 1.0,
    "Millisecond (ms)": 0.001,
    "Minute (min)": 60.0,
    "Hour (h)": 3600.0,
    "Day": 86400.0,
    "Week": 604800.0,
    "Month (30 days)": 2592000.0,
    "Year (365 days)": 31536000.0,
}

# Base unit: meter/second
SPEED_UNITS = {
    "Meter/Second (m/s)": 1.0,
    "Kilometer/Hour (km/h)": 0.277778,
    "Mile/Hour (mph)": 0.44704,
    "Knot (kn)": 0.514444,
    "Foot/Second (ft/s)": 0.3048,
}

# Base unit: square meter
AREA_UNITS = {
    "Square Meter (m²)": 1.0,
    "Square Kilometer (km²)": 1000000.0,
    "Square Centimeter (cm²)": 0.0001,
    "Hectare (ha)": 10000.0,
    "Acre": 4046.86,
    "Square Foot (ft²)": 0.092903,
    "Square Inch (in²)": 0.00064516,
    "Square Mile (mi²)": 2589988.11,
}

# Base unit: joule
ENERGY_UNITS = {
    "Joule (J)": 1.0,
    "Kilojoule (kJ)": 1000.0,
    "Calorie (cal)": 4.184,
    "Kilocalorie (kcal)": 4184.0,
    "Watt-hour (Wh)": 3600.0,
    "Kilowatt-hour (kWh)": 3600000.0,
    "BTU": 1055.06,
}

# Base unit: byte
DATA_UNITS = {
    "Byte (B)": 1.0,
    "Kilobyte (KB)": 1000.0,
    "Megabyte (MB)": 1000000.0,
    "Gigabyte (GB)": 1000000000.0,
    "Terabyte (TB)": 1000000000000.0,
    "Bit (b)": 0.125,
    "Kibibyte (KiB)": 1024.0,
    "Mebibyte (MiB)": 1048576.0,
    "Gibibyte (GiB)": 1073741824.0,
}

# All linear categories grouped together (Temperature is handled separately)
LINEAR_CATEGORIES = {
    "Length": LENGTH_UNITS,
    "Weight": WEIGHT_UNITS,
    "Volume": VOLUME_UNITS,
    "Time": TIME_UNITS,
    "Speed": SPEED_UNITS,
    "Area": AREA_UNITS,
    "Energy": ENERGY_UNITS,
    "Data": DATA_UNITS,
}

# Temperature has its own list because conversions are non-linear
TEMPERATURE_UNITS = ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"]

# All categories shown in the UI (in display order)
ALL_CATEGORIES = [
    "Length", "Weight", "Temperature", "Volume",
    "Time", "Speed", "Area", "Energy", "Data",
]


# ---------------------------------------------------------------------------
# CONVERSION FUNCTIONS
# ---------------------------------------------------------------------------

def convert_linear(value, from_unit, to_unit, units_dict):
    """
    Convert between two units that have a linear relationship.

    Step 1: convert input value to the base unit
    Step 2: convert base unit value to the target unit
    """
    base_value = value * units_dict[from_unit]
    return base_value / units_dict[to_unit]


def convert_temperature(value, from_unit, to_unit):
    """
    Convert between temperature units. Uses Celsius as the intermediate.
    """
    # Step 1: convert input to Celsius
    if from_unit == "Celsius (°C)":
        celsius = value
    elif from_unit == "Fahrenheit (°F)":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "Kelvin (K)":
        celsius = value - 273.15
    else:
        raise ValueError(f"Unknown temperature unit: {from_unit}")

    # Step 2: convert Celsius to target unit
    if to_unit == "Celsius (°C)":
        return celsius
    elif to_unit == "Fahrenheit (°F)":
        return celsius * 9 / 5 + 32
    elif to_unit == "Kelvin (K)":
        return celsius + 273.15
    else:
        raise ValueError(f"Unknown temperature unit: {to_unit}")


def get_units_for_category(category):
    """Return the list of available units for the given category."""
    if category == "Temperature":
        return TEMPERATURE_UNITS
    return list(LINEAR_CATEGORIES[category].keys())


def convert(value, from_unit, to_unit, category):
    """
    Main conversion entry point. Picks the right conversion strategy
    based on the category.
    """
    if category == "Temperature":
        return convert_temperature(value, from_unit, to_unit)
    return convert_linear(value, from_unit, to_unit, LINEAR_CATEGORIES[category])
