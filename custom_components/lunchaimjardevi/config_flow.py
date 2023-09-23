from __future__ import annotations
from . import common
from typing import Any

from homeassistant import config_entries, exceptions
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession

import asyncio
import voluptuous as vol


DATA_SCHEMA = vol.Schema(
    {
        vol.Required(common.CONF_APIKEY): str
    }
)


class ConfigFlow(config_entries.ConfigFlow, domain=common.DOMAIN):

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""

        errors = {}
        if user_input is not None:
            try:
                return self.async_create_entry(title="Luncha i Mjärdevi", data=user_input)
            except Exception:  # pylint: disable=broad-except
                common._LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"

        return self.async_show_form(
            step_id="user", data_schema=DATA_SCHEMA, errors=errors
        )
        