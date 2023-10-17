import inspect
import os
from datetime import datetime
import logging


def ch_cwd():
    current_file_name = inspect.getfile(inspect.currentframe())
    path = os.path.dirname(os.path.abspath(current_file_name))
    os.chdir(path)

def set_seed(seed):
    try:
        import numpy as np
        import random
        import torch
        random.seed(seed)
        np.random.seed(seed)
        torch.manual_seed(seed)
        torch.manual_seed_all(seed)
        torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
    except:
        print("Fails to set seeds.")

def getlogger(logfile = "log.log", log_format = "[%(asctime)s] [%(levelname)s] - %(message)s", logger_name = "my_logger"):
    
    logger = logging.getLogger(logger_name)

    formatter = logging.Formatter(log_format)

    file_handler = logging.FileHandler(logfile)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    logger.setLevel(logging.DEBUG)

    return logger
