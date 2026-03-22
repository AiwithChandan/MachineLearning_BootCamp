import os
import sys
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

from src.logger import logging
from src.exception import CustomException


@dataclass
class DataIngestionConfig:
    input_data_path: str = os.path.join("data", "data.csv")
    raw_data_path: str = os.path.join("artifacts", "raw.csv")
    train_file_path: str = os.path.join("artifacts", "train.csv")
    test_file_path: str = os.path.join("artifacts", "test.csv")
    test_size: float = 0.3


class DataIngestion:

    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion started")

        try:
            # Check file existence
            if not os.path.exists(self.ingestion_config.input_data_path):
                raise FileNotFoundError(
                    f"File not found at {self.ingestion_config.input_data_path}"
                )

            # Read data
            df = pd.read_csv(self.ingestion_config.input_data_path)
            logging.info(f"Dataset loaded successfully with shape: {df.shape}")

            # Create artifacts directory
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)

            # Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Raw data saved")

            # Train-test split
            train_set, test_set = train_test_split(
                df,
                test_size=self.ingestion_config.test_size,
                random_state=42
            )

            logging.info(f"Train shape: {train_set.shape}, Test shape: {test_set.shape}")

            # Save split data
            train_set.to_csv(self.ingestion_config.train_file_path, index=False)
            test_set.to_csv(self.ingestion_config.test_file_path, index=False)

            logging.info("Train-test split completed and saved")

            return (
                self.ingestion_config.train_file_path,
                self.ingestion_config.test_file_path
            )

        except Exception as e:
            logging.error("Error in Data Ingestion", exc_info=True)
            raise CustomException(e, sys)
        
 
'''        
# Testing

if __name__ == "__main__":
    obj = DataIngestion()
    train_path, test_path = obj.initiate_data_ingestion()

    print("Train file:", train_path)
    print("Test file:", test_path)
    
'''