from data_recollect.utils.utils import get_env


class Config:
    DEBUG = get_env('DEBUG', True)
