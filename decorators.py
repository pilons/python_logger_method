import logging
from functools import wraps

from logger_utf8 import get_logger


def with_logger():
    """
    ロガーを関数に注入するデコレーター。
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            program_name = func.__name__  # 実行中のスクリプト名を取得
            logger = get_logger(program_name)  # logger を関数の属性として保存
            wrapper.logger = logger  # ラッパー関数に logger を設定
            return func(*args, **kwargs)
        return wrapper
    return decorator
