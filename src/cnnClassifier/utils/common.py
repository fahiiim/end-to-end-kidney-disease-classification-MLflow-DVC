import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import joblib
from ensure import ensure_annotations
from pathlib import Path  
from box import ConfigBox
from typing import Any
import base64
import json


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a yaml file and returns a ConfigBox object.
    Args:
        path_to_yaml (Path): Path to the yaml file.
    Returns:
        ConfigBox: ConfigBox object containing the yaml file data.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise BoxValueError(f"Error while parsing yaml file")
    except Exception as e:
        raise e

