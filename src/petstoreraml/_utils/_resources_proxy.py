from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `petstoreraml.resources` module.

    This is used so that we can lazily import `petstoreraml.resources` only when
    needed *and* so that users can just import `petstoreraml` and reference `petstoreraml.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("petstoreraml.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
