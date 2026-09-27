import yaml 
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).parent
CONFIG_PATH = PROJECT_ROOT / "config.yaml"

def load_config():
    try:
        with open(CONFIG_PATH, "r") as f:
            return yaml.safe_load(f) or {}
    except FileNotFoundError:
        print(f"Warning: Configuration file not found at {CONFIG_PATH}. Using empty defaults.")
        return {}
    except yaml.YAMLError as exc:
        print(f"Error parsing YAML file: {exc}")
        raise 

settings = load_config()
