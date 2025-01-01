import pandas as pd 
from pathlib import Path 
from loguru import logger 

from src.setup.config import config 
from src.feature_pipeline.data_sourcing import get_raw_data


def load_raw_data() -> pd.DataFrame:
    
    logger.info("Checking for the the presence of the raw data")
    
    if not Path(config.raw_data_file_path).exists():
        logger.warning("Data not available locally -> Need to download it")
        get_raw_data()
    
    return pd.read_excel(config.raw_data_file_path)


data = load_raw_data()
breakpoint()
