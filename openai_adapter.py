import os

import dotenv
import openai

# APIキーの設定
dotenv.load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")


class OpenAIAdapter:
    def __init__(self):
        # system_promptはsystem_prompt.txtから読み込む
        with open("system_prompt.txt", "r", encoding="utf-8") as f:
            self.system_prompt = f.read()
        pass

    def _create_message(self, role, message):
        return {"role": role, "content": message}

    def create_chat(self, question):
        system_message = self._create_message("system", self.system_prompt)
        user_message = self._create_message("user", question)
        messages = [system_message, user_message]
        res = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=messages,
        )
        return res["choices"][0]["message"]["content"]


if __name__ == "__main__":
    adapter = OpenAIAdapter()
    question = "自然言語処理のアルゴリズムとその特徴を教えてください。"
    answer = adapter.create_chat(question)
    print(answer)
