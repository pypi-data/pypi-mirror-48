"""Define endpoints for interacting with systems (accounts)."""
from typing import Callable


class System:  # pylint: disable=too-few-public-methods
    """Define an object to interact with all endpoints."""

    def __init__(self, request: Callable) -> None:
        """Initialize."""
        self._request = request

    async def async_all(self) -> list:
        """Get all systems."""
        resp = await self._request("get", "systems")
        return resp["systems"]

    async def async_create(self, attributes: dict) -> dict:
        """Create a system with a specific attribute payload."""
        resp = await self._request("post", "systems", json={"systems": attributes})
        return resp["systems"]

    async def async_delete(self, system_id: int) -> None:
        """Delete a system by ID."""
        await self._request("delete", "systems/{0}".format(system_id))

    async def async_get(self, system_id: int) -> dict:
        """Get a system by ID."""
        resp = await self._request("get", "systems/{0}".format(system_id))
        return resp["systems"]

    async def async_update(self, system_id: int, new_attributes: dict) -> dict:
        """Update a system with a specific attribute payload."""
        resp = await self._request(
            "put", "systems/{0}".format(system_id), json={"systems": new_attributes}
        )
        return resp["systems"]
