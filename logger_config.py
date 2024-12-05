import logging

def configure_logging(log_file='app.log', log_level=logging.DEBUG):
    """
    ログ設定を行う関数。

    Args:
        log_file (str): ログファイルのパス。
        log_level (int): ログレベル（例: logging.DEBUG）。
    """
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename=log_file,
        filemode='w'  # 'w' にすると上書きモード
    )


def get_logger(name):
    """
    指定した名前のロガーを取得する関数。

    Args:
        name (str): ロガーの名前。

    Returns:
        logging.Logger: 指定された名前のロガー。
    """
    return logging.getLogger(name)
