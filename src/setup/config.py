from pathlib import Path 
from dotenv import load_dotenv, find_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

from src.setup.paths import RAW_DATA_DIR

_ = load_dotenv(
    find_dotenv(filename=".env")
)


class DataConfig(BaseSettings):

    data_url: str = "https://data.humdata.org/dataset/7915bad5-6ea5-45b7-b035-f7a6f2438bd3/resource/1ddd1531-bf23-4c09-8538-f4e7b4c7e5ec/download/commodities-received-4.xlsx" 
    raw_data_file_name: str = "commodities_received_2024.xlsx"
    raw_data_file_path: Path = RAW_DATA_DIR/raw_data_file_name

config = DataConfig()

