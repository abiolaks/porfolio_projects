import os
from box.exceptions import BoxValueError
import yaml
from src.wine_quality_prediction.logging import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (Path): path like input

    Raises:
        e: raises exception if yaml file is not found

    Returns:
        ConfigBox: ConfigBox type object
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise e
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        verbose (bool, optional): _description_. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")
            
@ensure_annotations
def save_json(path: Path, data: dict):
    """save dict as json file

    Args:
        path (Path): path to json file
        data (dict): data to be saved
    """
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)
        
        
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json file and returns as ConfigBox object

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: ConfigBox type object
    """
    with open(path, "r") as json_file:
        content = json.load(json_file)
        logger.info(f"json file: {path} loaded successfully")
        return ConfigBox(content)
    
    
@ensure_annotations
def get_size(path: Path) -> str:
    """get size in kb

    Args:
        path (Path): path to file

    Returns:
        str: size in kb
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"


def save_bin(file_path: Path, data: Any):
    """save binary file

    Args:
        file_path (Path): path to file
        data (Any): data to be saved
    """
    joblib.dump(value=data, filename=file_path)
    logger.info(f"binary file saved at: {file_path} of size: {get_size(path=file_path)}")
            
            