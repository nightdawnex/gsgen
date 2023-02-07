from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class BaseSettings:
    
    project_name: str = "foo"
    project_desc: str = ""
    output_dir: str = ""
    enabled_module: str = field(default_factory=str, metadata={"excluded_from_ui": True})
    enabled_plugins: List[str] = field(default_factory=set, metadata={"excluded_from_ui": True})
    submission_files: List[str] = field(default_factory=list)
    