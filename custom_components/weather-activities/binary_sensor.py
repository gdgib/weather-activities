"""Binary sensors for weather-activities."""

import logging

from homeassistant.components.binary_sensor import (
    BinarySensorEntity,
    BinarySensorEntityDescription,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import (
    DOMAIN,
    CONFID_NAME,
    ICON_ON,
    ICON_OFF,
)

LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback):
    """Set up the binary sensor platform."""
    LOGGER.debug("Setup new entry: %s", entry)

class WeatherActivitiesSensor(BinarySensorEntity):
    """Implementation of binary sensor."""

    def __init__(self, entry: ConfigEntry) -> None:
        """Initialize the binary sensor."""
        self._entry = entry
        
        self.entity_description = BinarySensorEntityDescription(
            key=DOMAIN,
            name=self._entry.get(CONFID_NAME) + " Per Day",
            icon=ICON_OFF,
            translation_key=DOMAIN + " perday",
        )

        self._attr_on = None
        self._attr_unique_id = f"{self._entry.entry_id}_{self._entry.domain}_perday"

        LOGGER.debug("Initialized binary sensor from entry data: %s", self._entry.data)

    @property
    def is_on(self) -> bool:
        """Test if the entity is on."""
        return self._attr_on

    @property
    def available(self) -> bool:
        """Test if entity is available."""
        return self._attr_on is not None

    @property
    def icon(self) -> str:
        """Get the icon, based on the current state."""
        return ICON_ON if self.is_on else ICON_OFF

    @property
    def extra_state_attributes(self) -> dict:
        """Get state attributes."""
        return {}

    async def async_update(self) -> None:
        """Update the entity state."""
        self._attr_on = False
