from pathlib import Path


class BaseConfig:
    BASE_DIR = Path(__file__).resolve().parent.parent.parent

class DevelopmentConfig(BaseConfig):
    pass

class ProductionConfig(BaseConfig):
    pass