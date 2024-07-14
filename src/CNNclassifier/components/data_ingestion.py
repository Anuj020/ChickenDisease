import os
import urllib.request as request
import zipfile
from CNNclassifier import logger
from CNNclassifier.utils.common import get_size
from CNNclassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URl,
                filename= self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}" )
        else:
            logger.info(f"File alredy exists of size:{get_size(Path(self.config.local_data_file))}")
    
    def extract_zip_file(self):
        '''
        Zip_file_path: str
        Extracts the zip file into the dat directory
        Function returns None
        '''
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)