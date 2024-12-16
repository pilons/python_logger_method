from logger_config import configure_logging, get_logger


def main():
    """
    アプリケーションのエントリーポイント。
    """
    # ログ設定を適用
    configure_logging()

    # 名前付きロガーを取得
    logger = get_logger("MainApp")

    # ログの出力例
    logger.debug("アプリケーションがデバッグモードで起動しました")
    logger.info("アプリケーションが正常に起動しました")
    logger.warning("警告: アプリケーションの設定に注意が必要です")
    logger.error("エラー: 予期しないエラーが発生しました")
    logger.critical("致命的なエラー: アプリケーションを終了します")


if __name__ == "__main__":
    main()
