import os
import sys
import logging

## customized logging template that I have used
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

## at what time at which level you are running which module it is showing the message

log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("cnnClassifierLogger")
