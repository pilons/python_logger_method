from logger_utf8 import get_logger


def second():
    """
    アプリケーションのエントリーポイント。
    """

    logger = get_logger(second.__name__)

    # ログの出力例
    logger.debug("アプリケーションがデバッグモードで起動しました")
    logger.info("アプリケーションが正常に起動しました")
    logger.warning("警告: アプリケーションの設定に注意が必要です")
    logger.error("エラー: 予期しないエラーが発生しました")
    logger.critical("致命的なエラー: アプリケーションを終了します")
