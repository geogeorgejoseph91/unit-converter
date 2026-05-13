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
# LENGTH
# Base unit: meter
# ---------------------------------------------------------------------------

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

# ---------------------------------------------------------------------------
# WEIGHT
# Base unit: kilogram
# ---------------------------------------------------------------------------

WEIGHT_UNITS = {
    "Kilogram (kg)": 1.0,
    "Gram (g)": 0.001,
    "Milligram (mg)": 0.000001,
    "Metric Ton (t)": 1000.0,
    "Pound (lb)": 0.453592,
    "Ounce (oz)": 0.0283495,
    "Stone (st)": 6.35029,
}

# ---------------------------------------------------------------------------
# VOLUME
# Base unit: liter
# ---------------------------------------------------------------------------

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

# ---------------------------------------------------------------------------
# TIME
# Base unit: second
# ---------------------------------------------------------------------------

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

# ---------------------------------------------------------------------------
# SPEED
# Base unit: meter/second
# ---------------------------------------------------------------------------

SPEED_UNITS = {
    "Meter/Second (m/s)": 1.0,
    "Kilometer/Hour (km/h)": 0.277778,
    "Mile/Hour (mph)": 0.44704,
    "Knot (kn)": 0.514444,
    "Foot/Second (ft/s)": 0.3048,
}

# ---------------------------------------------------------------------------
# AREA
# Base unit: square meter
# ---------------------------------------------------------------------------

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

# ---------------------------------------------------------------------------
# ENERGY
# Base unit: joule
# ---------------------------------------------------------------------------

ENERGY_UNITS = {
    "Joule (J)": 1.0,
    "Kilojoule (kJ)": 1000.0,
    "Calorie (cal)": 4.184,
    "Kilocalorie (kcal)": 4184.0,
    "Watt-hour (Wh)": 3600.0,
    "Kilowatt-hour (kWh)": 3600000.0,
    "BTU": 1055.06,
}

# ---------------------------------------------------------------------------
# DATA
# Base unit: byte
# ---------------------------------------------------------------------------

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

# ---------------------------------------------------------------------------
# PRESSURE
# Base unit: pascal
# ---------------------------------------------------------------------------

PRESSURE_UNITS = {
    "Pascal (Pa)": 1.0,
    "Kilopascal (kPa)": 1000.0,
    "Bar": 100000.0,
    "PSI": 6894.76,
    "Atmosphere (atm)": 101325.0,
}

# ---------------------------------------------------------------------------
# POWER
# Base unit: watt
# ---------------------------------------------------------------------------

POWER_UNITS = {
    "Watt (W)": 1.0,
    "Kilowatt (kW)": 1000.0,
    "Megawatt (MW)": 1000000.0,
    "Horsepower (hp)": 745.7,
}

# ---------------------------------------------------------------------------
# FORCE
# Base unit: newton
# ---------------------------------------------------------------------------

FORCE_UNITS = {
    "Newton (N)": 1.0,
    "Kilonewton (kN)": 1000.0,
    "Pound-force (lbf)": 4.44822,
}

# ---------------------------------------------------------------------------
# ANGLE
# Base unit: radian
# ---------------------------------------------------------------------------

ANGLE_UNITS = {
    "Radian (rad)": 1.0,
    "Degree (°)": 0.0174533,
}

# ---------------------------------------------------------------------------
# FREQUENCY
# Base unit: hertz
# ---------------------------------------------------------------------------

FREQUENCY_UNITS = {
    "Hertz (Hz)": 1.0,
    "Kilohertz (kHz)": 1000.0,
    "Megahertz (MHz)": 1000000.0,
    "Gigahertz (GHz)": 1000000000.0,
}

# ---------------------------------------------------------------------------
# ELECTRIC CURRENT
# Base unit: ampere
# ---------------------------------------------------------------------------

CURRENT_UNITS = {
    "Ampere (A)": 1.0,
    "Milliampere (mA)": 0.001,
}

# ---------------------------------------------------------------------------
# VOLTAGE
# Base unit: volt
# ---------------------------------------------------------------------------

VOLTAGE_UNITS = {
    "Volt (V)": 1.0,
    "Millivolt (mV)": 0.001,
    "Kilovolt (kV)": 1000.0,
}

# ---------------------------------------------------------------------------
# RESISTANCE
# Base unit: ohm
# ---------------------------------------------------------------------------

RESISTANCE_UNITS = {
    "Ohm (Ω)": 1.0,
    "Kiloohm (kΩ)": 1000.0,
    "Megaohm (MΩ)": 1000000.0,
}

# ---------------------------------------------------------------------------
# DENSITY
# Base unit: kg/m³
# ---------------------------------------------------------------------------

DENSITY_UNITS = {
    "Kilogram/m³": 1.0,
    "Gram/cm³": 1000.0,
}

# ---------------------------------------------------------------------------
# ACCELERATION
# Base unit: m/s²
# ---------------------------------------------------------------------------

ACCELERATION_UNITS = {
    "Meter/s²": 1.0,
    "Foot/s²": 0.3048,
}

# ---------------------------------------------------------------------------
# TEMPERATURE (special handling)
# ---------------------------------------------------------------------------

TEMPERATURE_UNITS = [
    "Celsius (°C)",
    "Fahrenheit (°F)",
    "Kelvin (K)"
]

# ---------------------------------------------------------------------------
# ALL LINEAR CATEGORIES
# ---------------------------------------------------------------------------

LINEAR_CATEGORIES = {
    "Length": LENGTH_UNITS,
    "Weight": WEIGHT_UNITS,
    "Volume": VOLUME_UNITS,
    "Time": TIME_UNITS,
    "Speed": SPEED_UNITS,
    "Area": AREA_UNITS,
    "Energy": ENERGY_UNITS,
    "Data": DATA_UNITS,
    "Pressure": PRESSURE_UNITS,
    "Power": POWER_UNITS,
    "Force": FORCE_UNITS,
    "Angle": ANGLE_UNITS,
    "Frequency": FREQUENCY_UNITS,
    "Electric Current": CURRENT_UNITS,
    "Voltage": VOLTAGE_UNITS,
    "Resistance": RESISTANCE_UNITS,
    "Density": DENSITY_UNITS,
    "Acceleration": ACCELERATION_UNITS,
}

# ---------------------------------------------------------------------------
# ALL CATEGORIES
# ---------------------------------------------------------------------------

ALL_CATEGORIES = [
    "Length",
    "Weight",
    "Temperature",
    "Volume",
    "Time",
    "Speed",
    "Area",
    "Energy",
    "Data",
    "Pressure",
    "Power",
    "Force",
    "Angle",
    "Frequency",
    "Electric Current",
    "Voltage",
    "Resistance",
    "Density",
    "Acceleration",
]
ALL_CATEGORIES = sorted(ALL_CATEGORIES)
# ---------------------------------------------------------------------------
# CONVERSION FUNCTIONS
# ---------------------------------------------------------------------------

def convert_linear(value, from_unit, to_unit, units_dict):
    """
    Convert between two units that have a linear relationship.
    """
    base_value = value * units_dict[from_unit]
    return base_value / units_dict[to_unit]


def convert_temperature(value, from_unit, to_unit):
    """
    Convert between temperature units.
    Uses Celsius as the intermediate.
    """

    # Convert to Celsius
    if from_unit == "Celsius (°C)":
        celsius = value

    elif from_unit == "Fahrenheit (°F)":
        celsius = (value - 32) * 5 / 9

    elif from_unit == "Kelvin (K)":
        celsius = value - 273.15

    else:
        raise ValueError(f"Unknown temperature unit: {from_unit}")

    # Convert from Celsius to target
    if to_unit == "Celsius (°C)":
        return celsius

    elif to_unit == "Fahrenheit (°F)":
        return celsius * 9 / 5 + 32

    elif to_unit == "Kelvin (K)":
        return celsius + 273.15

    else:
        raise ValueError(f"Unknown temperature unit: {to_unit}")


def get_units_for_category(category):
    """
    Return list of units for the given category.
    """

    if category == "Temperature":
        return TEMPERATURE_UNITS

    return list(LINEAR_CATEGORIES[category].keys())


def convert(value, from_unit, to_unit, category):
    """
    Main conversion entry point.
    """

    if category == "Temperature":
        return convert_temperature(value, from_unit, to_unit)

    return convert_linear(
        value,
        from_unit,
        to_unit,
        LINEAR_CATEGORIES[category]
    )

def get_conversion_equation(from_unit, to_unit, category):
  """
  Return conversion equation/formula for selected units.
  """

  # Temperature formulas
  if category == "Temperature":

      if from_unit == "Celsius (°C)" and to_unit == "Fahrenheit (°F)":
          return "°F = (°C × 9/5) + 32"

      elif from_unit == "Fahrenheit (°F)" and to_unit == "Celsius (°C)":
          return "°C = (°F - 32) × 5/9"

      elif from_unit == "Celsius (°C)" and to_unit == "Kelvin (K)":
          return "K = °C + 273.15"

      elif from_unit == "Kelvin (K)" and to_unit == "Celsius (°C)":
          return "°C = K - 273.15"

      elif from_unit == "Fahrenheit (°F)" and to_unit == "Kelvin (K)":
          return "K = (°F - 32) × 5/9 + 273.15"

      elif from_unit == "Kelvin (K)" and to_unit == "Fahrenheit (°F)":
          return "°F = (K - 273.15) × 9/5 + 32"

      else:
          return "Same Unit"

  # Linear unit equations
  units_dict = LINEAR_CATEGORIES[category]

  from_factor = units_dict[from_unit]
  to_factor = units_dict[to_unit]

  factor = from_factor / to_factor

  return f"1 {from_unit} = {factor:g} {to_unit}"