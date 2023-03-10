name = "NetworkProjectEngine"
version = "1.0.0"
author = "Tim"
author_email = ""
description = "Network Project Engine"

from core.managers.setting_manager import SettingManager
from .config import Config as _Config

config = SettingManager.register(_Config)
from .grader import grade
from .gen_doc import generate_documentation