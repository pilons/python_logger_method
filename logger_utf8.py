import logging


def configure_logging(log_file='app_utf8.log', log_level=logging.ERROR):
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
    handler.setLevel(log_level)  # ハンドラーのログレベルを設定
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

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


# ログ設定を適用
configure_logging()

# ロガーを取得してログ出力
logger = get_logger('MainApp')
logger.debug('デバッグ: UTF-8で正しく出力されます。')
logger.info('情報: UTF-8エンコーディングのログです。')
logger.warning('警告: 日本語も文字化けしません。')
logger.error('エラー: ログファイルがUTF-8で出力されています。')
logger.critical('致命的: これで文字化けしないはずです。')
