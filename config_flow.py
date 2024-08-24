"""Config flow for Music Daemon integration."""
from homeassistant import config_entries
import voluptuous as vol

from .const import DOMAIN

class MusicDaemonConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Music Daemon."""

    VERSION = 1

    def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        if user_input is not None:
            # Validate user input here
            return self.async_create_entry(title="Music Daemon", data=user_input)

        data_schema = vol.Schema({
            vol.Required("host", default="localhost"): str,
            vol.Required("port", default=5000): int,
        })

        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors
        )
