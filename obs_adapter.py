import os

import obsws_python as obs
from dotenv import load_dotenv


class OBSAdapter:
    def __init__(self) -> None:
        load_dotenv()

        # OBS WebSocket接続に必要な情報を環境変数から取得
        password = os.environ.get("OBS_WS_PASSWORD")
        host = os.environ.get("OBS_WS_HOST")
        port = os.environ.get("OBS_WS_PORT")

        # 必要な設定が全て存在するか確認
        if password == None or host == None or port == None:
            raise Exception("OBSの設定がされていません")

        # OBS WebSocketクライアントを初期化
        self.ws = obs.ReqClient(host=host, port=port, password=password)

    def set_question(self, text: str):
        # 質問テキストをOBSの"Question"入力ソースに設定
        self.ws.set_input_settings(
            name="Question",
            settings={"text": text},
            overlay=True,
        )

    def set_answer(self, text: str):
        # 回答テキストをOBSの"Answer"入力ソースに設定
        self.ws.set_input_settings(
            name="Answer",
            settings={"text": text},
            overlay=True,
        )
