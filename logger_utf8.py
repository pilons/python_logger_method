import logging


def configure_logging(log_file='app_utf8.log', log_level=logging.DEBUG):
    """
    ログ設定を行う関数。

    Args:
        log_file (str): ログファイルのパス。
        log_level (int): ログレベル（例: logging.DEBUG）。
    """
    # ルートロガーの取得
    logger = logging.getLogger()
    logger.setLevel(log_level)

    # ハンドラーが重複追加されないようにクリア
    if logger.hasHandlers():
        logger.handlers.clear()

    # コンソール用のハンドラーを作成
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # ファイル出力用のハンドラーを作成
    file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
    file_handler.setLevel(logging.ERROR)
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)


def get_logger(name):
    """
    指定した名前のロガーを取得する関数。

    Args:
        name (str): ロガーの名前。

    Returns:
        logging.Logger: 指定された名前のロガー。
    """
    return logging.getLogger(name)


# ログ設定を初期化
configure_logging()
