name = "NetworkProjectEngine"
version = "1.0.0"
author = "Tim"
author_email = ""
description = "Network Project Engine"

from .config import Config as _Config
from core.managers.setting_manager import SettingManager
config = SettingManager.register(_Config)
from . import custom_gui as CustomGUI
