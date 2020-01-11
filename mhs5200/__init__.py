from . import enums
from .mhs5200 import MHS5200

__all__ = ["MHS5200", "enums"]

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions
