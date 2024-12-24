from logger_utf8 import get_logger
from second_without_argument import second


def without_arguments():
    """
    アプリケーションのエントリーポイント。
    """

    logger = get_logger(without_arguments.__name__)

    # ログの出力例
    logger.debug("アプリケーションがデバッグモードで起動しました")
    logger.info("アプリケーションが正常に起動しました")
    logger.warning("警告: アプリケーションの設定に注意が必要です")
    logger.error("エラー: 予期しないエラーが発生しました")
    logger.critical("致命的なエラー: アプリケーションを終了します")

    second()

    # ログの出力例
    logger.debug("アプリケーションがデバッグモードで起動しました")
    logger.info("アプリケーションが正常に起動しました")
    logger.warning("警告: アプリケーションの設定に注意が必要です")
    logger.error("エラー: 予期しないエラーが発生しました")
    logger.critical("致命的なエラー: アプリケーションを終了します")

    second()


if __name__ == "__main__":
    without_arguments()
