"""Constants used throughout this module"""
from lib2to3.pgen2.token import OP
import os
import platform
import subprocess
from typing import Optional

from pyparsing import Opt
from webdriver_manager.chrome import ChromeDriverManager

# Methods for getting the constants needed


def is_tool_present(name) -> bool:
    """determines if an executable is present on the current device"""
    try:
        devnull = open(os.devnull)
        subprocess.Popen([name], stdout=devnull, stderr=devnull).communicate()
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            return False
    return True


def find_prog_path(prog) -> Optional[str]:
    """returns the path of a tool if present"""
    if is_tool_present(prog):
        cmd = "where" if platform.system() == "Windows" else "which"
        return subprocess.call([cmd, prog])


COLONIST_URL = "https://colonist.io/?#"
CHROMEDRIVER_PATH = ChromeDriverManager().install()
