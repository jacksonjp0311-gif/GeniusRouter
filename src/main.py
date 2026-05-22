"""Compatibility entrypoint.

Docker and existing docs may still refer to `src.main:app`.
The real app now lives at `geniusrouter.main:app`.
"""

from geniusrouter.main import app

__all__ = ["app"]