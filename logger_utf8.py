import logging


def configure_logging(log_file='app_utf8.log', log_level=logging.DEBUG):
    """
    ログ設定を行う関数。

    Args:
        log_file (str): ログファイルのパス。
        log_level (int): ログレベル（例: logging.DEBUG）。
    """
    # ログハンドラーを作成してエンコーディングを指定
    handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')

    # コンソール用のハンドラーを作成
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)  # ハンドラーのログレベルを設定
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

# ファイル出力用のハンドラー
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.ERROR)
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)

    # ルートロガーにハンドラーを追加
    logger = logging.getLogger()
    logger.setLevel(log_level)
    logger.addHandler(handler)


def get_logger(name):
    """
    指定した名前のロガーを取得する関数。

    Args:
        name (str): ロガーの名前。

    Returns:
        logging.Logger: 指定された名前のロガー。
    """
    return logging.getLogger(name)


configure_logging()
