from decorators import with_logger
from second import second


@with_logger()
def without_arguments():
    """
    アプリケーションのエントリーポイント。
    """
    # ログの出力例
    without_arguments.logger.debug("アプリケーションがデバッグモードで起動しました")
    without_arguments.logger.info("アプリケーションが正常に起動しました")
    without_arguments.logger.warning("警告: アプリケーションの設定に注意が必要です")
    without_arguments.logger.error("エラー: 予期しないエラーが発生しました")
    without_arguments.logger.critical("致命的なエラー: アプリケーションを終了します")

    second()


if __name__ == "__main__":
    without_arguments()
