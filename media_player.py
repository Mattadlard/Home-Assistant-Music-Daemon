"""Media Player platform for Music Daemon."""
import logging

from homeassistant.components.media_player import MediaPlayerEntity
from homeassistant.components.media_player.const import (
    MEDIA_TYPE_MUSIC,
    SUPPORT_PLAY,
    SUPPORT_STOP,
    SUPPORT_PAUSE,
)
from homeassistant.const import STATE_PLAYING, STATE_IDLE

_LOGGER = logging.getLogger(__name__)

class MusicDaemonMediaPlayer(MediaPlayerEntity):
    """Representation of a Music Daemon Media Player."""

    def __init__(self):
        """Initialize the Music Daemon player."""
        self._state = STATE_IDLE
        self._name = "Music Daemon Player"
        self._media_title = None
        self._media_artist = None

    @property
    def state(self):
        """Return the state of the device."""
        return self._state

    @property
    def name(self):
        """Return the name of the device."""
        return self._name

    @property
    def media_title(self):
        """Return the title of the current media."""
        return self._media_title

    @property
    def media_artist(self):
        """Return the artist of the current media."""
        return self._media_artist

    @property
    def supported_features(self):
        """Flag media player features that are supported."""
        return SUPPORT_PLAY | SUPPORT_STOP | SUPPORT_PAUSE

    def play_media(self, media_type, media_id, **kwargs):
        """Play a piece of media."""
        _LOGGER.info("Playing media: %s", media_id)
        self._state = STATE_PLAYING
        self._media_title = media_id  # Simplified for example purposes
        self.schedule_update_ha_state()

    def stop(self):
        """Stop the player."""
        _LOGGER.info("Stopping media playback")
        self._state = STATE_IDLE
        self.schedule_update_ha_state()

    def pause(self):
        """Pause the player."""
        _LOGGER.info("Pausing media playback")
        self._state = STATE_IDLE
        self.schedule_update_ha_state()
