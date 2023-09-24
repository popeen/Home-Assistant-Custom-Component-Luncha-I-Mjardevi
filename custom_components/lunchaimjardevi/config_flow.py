from __future__ import annotations
from . import common
from typing import Any

from homeassistant import config_entries, exceptions
from homeassistant.helpers.aiohttp_client import async_get_clientsession

import voluptuous as vol

DATA_SCHEMA = vol.Schema(
    {
        vol.Required(common.CONF_APIKEY): str
    }
)

async def validate_input(hass: HomeAssistant, data: dict) -> dict[str, Any]:
    """Validate the user input."""
    session = async_get_clientsession(hass)  
    key = data[common.CONF_APIKEY]      
    try:
        url = "https://lunchaimjardevi.com/api/v4/validateKey?key=" + key
        async with session.get(url) as resp:
            json = await resp.json()
            if False == json['valid']:
                raise Exception("the key is invalid")
    except Exception:
        raise InvalidAPIKey

class ConfigFlow(config_entries.ConfigFlow, domain=common.DOMAIN):

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""

        errors = {}
        if user_input is not None:
            try:
                await validate_input(self.hass, user_input)
                return self.async_create_entry(title="Luncha i Mjärdevi", data=user_input)
            except InvalidAPIKey:
                errors["base"] = "invalid_api_key"
            except Exception:  # pylint: disable=broad-except
                common._LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"

        return self.async_show_form(
            step_id="user", data_schema=DATA_SCHEMA, errors=errors
        )
        
class InvalidAPIKey(exceptions.HomeAssistantError):
    """Error to indicate there is no data available for the ID."""