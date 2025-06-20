
###
### The Configuration Class should hold most of the configuration this globals.py are for configuration 
### before the Configuration class is loaded
###

from pathlib import Path

CURRENT_FILE_PATH    = Path(__file__).resolve()
WORKING_DIR_PATH     = Path(CURRENT_FILE_PATH.parents[1])
DATA_CONFIG_PATH     = WORKING_DIR_PATH / "data" / "config.yaml"
DATA_CONFIG_ENCODING = "utf-8"
