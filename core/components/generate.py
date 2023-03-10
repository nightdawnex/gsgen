import datetime
import os
import os.path as op
import shutil

from ..managers import SettingManager
from ..info import Directories
import logging

def create_output_dir(output_parent_dir: str) -> str:
    if not output_parent_dir:
        raise Exception("No output directory provided")

    output_dir = op.join(output_parent_dir, SettingManager.BaseSettings.project_name)
    if os.path.isdir(output_dir):
        output_dir = output_dir + "-" + datetime.datetime.now().strftime('%Y%m%d-%H-%M-%S')

    logging.critical(f'Files will be produced to: {output_dir}')
    
    return output_dir


def pack_autograder(autograder_dir: str) -> None:
    if not autograder_dir:
        raise Exception("No directory provided to make zip file")
    if not op.isdir(autograder_dir):
        raise NotADirectoryError()
    shutil.make_archive(op.join(autograder_dir,"..","autograder"), 'zip', autograder_dir)

def generate_output(output_parent_dir: str) -> None:
    from ..managers.setting_manager import SettingManager
    SettingManager.save_settings()
    
    output_dir = create_output_dir(output_parent_dir)
    shutil.copytree(Directories.template_dir, output_dir)
    
    output_source_dir = op.join(output_dir, "source")
    shutil.copytree(Directories.core_dir, op.join(output_source_dir, "core"))
    shutil.copytree(Directories.logs_dir, op.join(output_source_dir, "logs"))
    shutil.copy(op.join(Directories.src_path, "main.py"), output_source_dir)
    if SettingManager.BaseSettings.enabled_module:
        enabled_module = SettingManager.BaseSettings.enabled_module
        os.mkdir(op.join(output_source_dir, "modules"))
        shutil.copytree(op.join(Directories.src_path, "modules", enabled_module),
                        op.join(output_source_dir, "modules", enabled_module))
    if len(SettingManager.BaseSettings.enabled_plugins) > 0:
        os.mkdir(op.join(output_source_dir, "plugins"))
        for enabled_plugin in SettingManager.BaseSettings.enabled_plugins:
            shutil.copytree(op.join(Directories.src_path, "plugins", enabled_plugin),
                            op.join(output_source_dir, "plugins", enabled_plugin))
    pack_autograder(output_source_dir)

    from .documentation import generate_documentation
    generate_documentation(op.join(output_dir, "documentation.md"))

    # Open the output directory if on Windows
    try:
        os.startfile(output_dir)
    except AttributeError:
        pass
