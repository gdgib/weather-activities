"""Constants for the weather-activities integration."""

from homeassistant.components.binary_sensor import (
    DOMAIN as DOMAIN_BINARY_SENSOR,
)

DOMAIN = "weather-activities"
PLATFORMS = [DOMAIN_BINARY_SENSOR]

CONFID_NAME = "name"
CONFID_WEATHER_ENTITY = "weather_entity"
CONFID_FORECAST_DAYS = "forecast_days"
CONFID_TEMP_MIN = "temp_min"
CONFID_TEMP_MAX = "temp_max"

CONFDF_NAME = DOMAIN
CONFDF_FORECAST_DAYS = 7
CONFDF_TEMP_MIN = None
CONFDF_TEMP_MAX = None

ICON_ON = "mdi:cloud-check-variant"
ICON_OFF = "mdi:cloud-alert"
