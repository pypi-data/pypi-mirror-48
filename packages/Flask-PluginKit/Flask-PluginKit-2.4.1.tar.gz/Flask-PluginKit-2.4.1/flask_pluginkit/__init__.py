# -*- coding: utf-8 -*-

from .exceptions import PluginError, TarError, ZipError, InstallError, CSSLoadError, DCPError, VersionError, DFPError, NotCallableError
from .flask_pluginkit import PluginManager, push_dcp, emit_config
from .installer import PluginInstaller
from .web import blueprint
from .fixflask import Flask
from .utils import BaseStorage, LocalStorage, RedisStorage, PY2, string_types, isValidSemver, sortedSemver

__author__ = "staugur <staugur@saintic.com>"

__version__ = "2.4.1"

__all__ = ["Flask", "PluginManager", "PluginInstaller", "blueprint", "push_dcp", "emit_config",
           "PluginError", "TarError", "ZipError", "InstallError", "CSSLoadError", "DCPError", "VersionError", "DFPError", "NotCallableError",
           "BaseStorage", "LocalStorage", "RedisStorage", "PY2", "string_types", "isValidSemver", "sortedSemver"]
