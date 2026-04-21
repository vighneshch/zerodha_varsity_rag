# Loading the required libraries
import yaml
import os

def load_config(path = "config/config.yaml"):
    
    base_dir = os.path.dirname(os.path.dirname(__file__))  # Project_1
    path = os.path.join(base_dir, "config", "config.yaml")

    with open(path,"r") as f:
        return yaml.safe_load(f)

config = load_config()