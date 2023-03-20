import logging
import os, sys
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path)

import config
from constants import INPUT_DATA, LOGS
from helper_functions import read_file, data_to_objects
from build_versions import build_single_process, build_multiprocessing

logging.basicConfig(filename=LOGS,
                    filemode="w",
                    level=logging.DEBUG)


def build_the_wall():
    input_data = read_file(INPUT_DATA)
    profiles = data_to_objects(input_data)

    if config.MULTIPROCESING_MODE:
        profiles = build_multiprocessing(profiles)
    else:
        profiles = build_single_process(profiles)

    logging.debug(f"Finished profiles - {profiles}")
    return profiles
