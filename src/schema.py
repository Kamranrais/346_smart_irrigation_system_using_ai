# Data schema for the smart irrigation project (follows the team Overall Plan)

CROPS = ["wheat", "maize", "potato"]
SOILS = ["sandy", "loamy", "clay"]

# Inputs. No sensors: soil moisture is NOT an input, it is predicted.
NUMERIC_FEATURES = [
    "temperature_c",
    "humidity_pct",
    "rainfall_mm",            # rain in the last 24 hours
    "rain_forecast_mm",       # expected rain in the next 24 hours
    "month",                  # 1 to 12
    "days_since_irrigation",
    "last_irrigation_mm",
]

CATEGORICAL_FEATURES = ["crop_type", "soil_type"]
# "district" will be added after the data check (Stage B) shows which districts have data

FEATURES = NUMERIC_FEATURES + CATEGORICAL_FEATURES

# Stage 1 target: soil moisture predicted by the model
TARGET_MOISTURE = "soil_moisture_pct"

# Stage 2 targets: the decision and the amount
ACTIONS = ["irrigate", "skip_rain_expected", "monitor"]
TARGET_ACTION = "action"
TARGET_AMOUNT = "water_mm"   # water to apply in mm (0 unless action is irrigate)

# Allowed ranges, used to check data and app inputs
RANGES = {
    "temperature_c": (0, 50),
    "humidity_pct": (0, 100),
    "rainfall_mm": (0, 200),
    "rain_forecast_mm": (0, 200),
    "month": (1, 12),
    "days_since_irrigation": (0, 60),
    "last_irrigation_mm": (0, 100),
    "soil_moisture_pct": (0, 100),
}