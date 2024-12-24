import os

import dotenv
import openai

# 環境変数からAPIキーを読み込む
dotenv.load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")


class OpenAIAdapter:
    def __init__(self):
        # システムプロンプトをファイルから読み込む
        with open("system_prompt.txt", "r", encoding="utf-8") as f:
            self.system_prompt = f.read()
        pass

    def _create_message(self, role, message):
        # OpenAI APIに送信するメッセージ形式を作成
        return {"role": role, "content": message}

    def create_chat(self, question):
        # システムメッセージを作成
        system_message = self._create_message("system", self.system_prompt)
        # ユーザーメッセージを作成
        user_message = self._create_message("user", question)
        # メッセージリストを作成
        messages = [system_message, user_message]

        # OpenAI APIを呼び出し
        res = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=messages,
        )

        # APIレスポンスから回答テキストを抽出して返す
        return res["choices"][0]["message"]["content"]
