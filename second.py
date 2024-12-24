from decorators import with_logger

@with_logger()
def second():
    """
    アプリケーションのエントリーポイント。
    """

    # ログの出力例
    second.logger.debug("アプリケーションがデバッグモードで起動しました")
    second.logger.info("アプリケーションが正常に起動しました")
    second.logger.warning("警告: アプリケーションの設定に注意が必要です")
    second.logger.error("エラー: 予期しないエラーが発生しました")
    second.logger.critical("致命的なエラー: アプリケーションを終了します")
