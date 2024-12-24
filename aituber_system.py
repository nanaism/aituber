import random

from dotenv import load_dotenv

from obs_adapter import OBSAdapter
from openai_adapter import OpenAIAdapter
from play_sound import PlaySound
from voicevox_adapter import VoicevoxAdapter
from youtube_comment_adapter import YoutubeCommentAdapter

load_dotenv()
import os


class AITuberSystem:
    def __init__(self) -> None:
        video_id = os.getenv("YOUTUBE_VIDEO_ID")
        self.youtube_comment_adapter = YoutubeCommentAdapter(video_id)
        self.openai_adapter = OpenAIAdapter()
        self.voice_adapter = VoicevoxAdapter()
        self.obs_adapter = OBSAdapter()
        self.play_sound = PlaySound(output_device_name="CABLE Input")
        self.conversation_history = []
        self.topics = [
            # テクノロジー関連
            "最近のAI技術の発展について",
            "未来の技術はどうなると思う？",
            "好きなガジェットについて",
            "面白いアプリや便利なツールについて",
            "プログラミングの楽しさについて",
            "バーチャルYouTuberの魅力について",
            "最近のスマートフォンの進化について",
            "ロボット工学の未来について",
            "Web3やブロックチェーンについて",
            "メタバースの可能性について",
            # エンターテイメント
            "最近見た面白い動画について",
            "好きなアニメや漫画について",
            "印象に残ったゲームについて",
            "おすすめの映画やドラマについて",
            "好きな音楽やアーティストについて",
            "面白かったライブ配信について",
            "最近ハマっているゲームについて",
            "好きなバーチャルYouTuberについて",
            "印象に残った動画作品について",
            "おもしろかった実況プレイ動画について",
            # 趣味・文化
            "最近始めた新しい趣味について",
            "おすすめの本や小説について",
            "好きな料理や食べ物について",
            "休日の過ごし方について",
            "旅行で行ってみたい場所について",
            "インターネットでの発見について",
            "創作活動の楽しさについて",
            "コレクションしているものについて",
            "最近のトレンドについて",
            "面白いSNSの使い方について",
            # 日常生活
            "今日あった面白い出来事について",
            "最近の天気や季節の変化について",
            "好きな時間の過ごし方について",
            "リラックスする方法について",
            "おすすめのカフェや店について",
            "便利な生活のハックについて",
            "楽しい思い出について",
            "明日やってみたいことについて",
            "休日の予定について",
            "お気に入りの場所について",
            # 学び・教養
            "最近学んだ面白い知識について",
            "気になる科学の話題について",
            "不思議な自然現象について",
            "宇宙や天体について",
            "歴史の中の面白い出来事について",
            "言語や言葉の面白さについて",
            "心理学の興味深い話題について",
            "動物や生き物の不思議について",
            "芸術や文化について",
            "哲学的な考察について",
            # 創造的な話題
            "面白いアイデアについて",
            "未来の夢や目標について",
            "想像上の世界について",
            "タイムトラベルしたら何をする？",
            "スーパーパワーがあったら何がしたい？",
            "理想の休暇について",
            "宝くじが当たったら何をする？",
            "異世界に行ったら何をしてみたい？",
            "理想の未来について",
            "空を飛べるようになったら行きたい場所は？",
            # コミュニティ・交流
            "オンラインでの出会いについて",
            "コミュニティの面白さについて",
            "思い出に残る会話について",
            "インターネットの良いところについて",
            "友達との楽しい思い出について",
            "オンラインイベントの魅力について",
            "配信を通じた交流について",
            "共有して嬉しかった経験について",
            "一緒に遊んで楽しかった思い出について",
            "応援してくれる人への感謝について",
            # 感情・内面
            "最近嬉しかったことについて",
            "笑顔になれる瞬間について",
            "心が温まる出来事について",
            "がんばろうと思えること",
            "わくわくする未来のことについて",
            "癒されること・モノについて",
            "元気をもらえる言葉について",
            "心に響いた言葉について",
            "自分の成長を感じる瞬間について",
            "大切にしている価値観について",
            # 季節・イベント
            "この季節ならではの楽しみについて",
            "好きな季節の風景について",
            "思い出の行事やイベントについて",
            "季節の食べ物について",
            "祭りや伝統行事について",
            "花火や夜景について",
            "お正月の過ごし方について",
            "クリスマスの思い出について",
            "春夏秋冬の好きなところについて",
            "季節の変わり目の楽しみについて",
            # ポップカルチャー
            "最近のミームについて",
            "面白いインターネットスラングについて",
            "トレンドの動画について",
            "人気のコンテンツについて",
            "面白いチャレンジについて",
            "人気のハッシュタグについて",
            "話題のショート動画について",
            "インターネットの流行について",
            "面白い都市伝説について",
            # 創作・表現
            "好きな創作活動について",
            "描きたいイラストについて",
            "作ってみたい動画について",
            "挑戦したい配信について",
            "書いてみたい物語について",
            "作ってみたい音楽について",
            "編集のコツについて",
            "クリエイティブな表現について",
            "アート作品の解釈について",
            "創作の源泉について",
        ]
        self.current_topic = None

    def generate_autonomous_message(self) -> str:
        if not self.current_topic or len(self.conversation_history) >= 3:
            # 新しいトピックを選択
            self.current_topic = random.choice(self.topics)
            self.conversation_history = []
            return f"新しい話題について話そうかな。{self.current_topic}どう思う？"

        # 会話履歴を使って次のメッセージを生成
        context = "これまでの会話:\n" + "\n".join(self.conversation_history)
        prompt = f"{context}\n\n{self.current_topic}についての会話を続けてください。"
        return self.openai_adapter.create_chat(prompt)

    def talk_with_comment(self) -> bool:
        # コメントの確認
        comment = self.youtube_comment_adapter.get_comment()

        if comment:
            # コメントがある場合はそれに応答
            print("コメントを受信しました:", comment)
            response_text = self.openai_adapter.create_chat(comment)
            self.obs_adapter.set_question(comment)
            self.conversation_history = []  # コメント対応後は自律会話をリセット
        else:
            # コメントがない場合は自律的に会話を生成
            print("自律会話を生成します...")
            response_text = self.generate_autonomous_message()
            self.obs_adapter.set_question("自律会話中...")

        # 応答の処理
        self.conversation_history.append(response_text)
        self.obs_adapter.set_answer(response_text)
        data, rate = self.voice_adapter.get_voice(response_text)
        self.play_sound.play_sound(data, rate)
        return True
