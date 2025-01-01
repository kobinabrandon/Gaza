from dotenv import load_dotenv, find_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


_ = load_dotenv(
    find_dotenv(filename=".env")
)


class GeneralConfig(BaseSettings):
    _ = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    data_url: str = "https://data.humdata.org/dataset/7915bad5-6ea5-45b7-b035-f7a6f2438bd3/resource/1ddd1531-bf23-4c09-8538-f4e7b4c7e5ec/download/commodities-received-4.xlsx" 


config = GeneralConfig()

