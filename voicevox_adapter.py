import io
import json

import requests
import soundfile


class VoicevoxAdapter:
    # VOICEVOXサーバーのURL
    URL = "http://127.0.0.1:50021/"

    def __init__(self) -> None:
        pass

    def __create_audio_query(self, text: str, speaker_id: int) -> json:
        # 音声合成のためのクエリを生成
        item_data = {
            "text": text,
            "speaker": speaker_id,
        }
        # audio_queryエンドポイントにPOSTリクエストを送信
        response = requests.post(self.URL + "audio_query", params=item_data)
        # レスポンスをJSON形式で返す
        return response.json()

    def __create_request_audio(self, query_data, speaker_id: int) -> bytes:
        # 音声合成リクエストのパラメータを設定
        a_params = {
            "speaker": speaker_id,
        }
        # リクエストヘッダーを設定
        headers = {"accept": "audio/wav", "Content-Type": "application/json"}
        # synthesisエンドポイントにPOSTリクエストを送信
        res = requests.post(
            self.URL + "synthesis",
            params=a_params,
            data=json.dumps(query_data),
            headers=headers,
        )
        # レスポンスのステータスコードを表示
        print(res.status_code)
        # 音声データ（バイト列）を返す
        return res.content

    def get_voice(self, text: str):
        # 話者IDを設定（ここでは春日部つむぎを使用）
        speaker_id = 8
        # テキストから音声クエリを生成
        query_data: json = self.__create_audio_query(text, speaker_id=speaker_id)
        # 音声クエリから音声データ（バイト列）を生成
        audio_bytes = self.__create_request_audio(query_data, speaker_id=speaker_id)
        # バイト列をバイトストリームに変換
        audio_stream = io.BytesIO(audio_bytes)
        # 音声データを読み込み、データとサンプルレートを取得
        data, sample_rate = soundfile.read(audio_stream)
        # 音声データとサンプルレートを返す
        return data, sample_rate
