import requests 
from loguru import logger 

from src.setup.config import config 
from src.setup.paths import RAW_DATA_DIR, make_directories


def get_raw_data(url: str = config.data_url):

    make_directories()
    
    response = requests.get(url)
    if response.status_code == 200:
        logger.success("Data found -> Downloading it now.")
        
        try:
            with open(config.raw_data_file_path, mode="wb") as file:
                _ = file.write(response.content)
            logger.success("Downloaded!")
                    
        except Exception as error:
            logger.error(error)
    else:
        logger.error(f"Data not found: Status code: {response.status_code}")

