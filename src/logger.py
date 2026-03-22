import os
import sys
import logging
from datetime import datetime 

# Define Path
log_path = 'logs/app.log'
os.makedirs("logs", exist_ok=True)

# Write Log Config
logging.basicConfig(
    level=logging.INFO,
    filename=log_path,
    format='%(asctime)s - %(levelname)s - %(message)s - %(funcName)s'
)