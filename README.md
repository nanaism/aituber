# AI Tuber Plays Mario: Reinforcement Learning & LLM Live Stream

[![Watch the Live Stream Archive on YouTube](https://img.shields.io/badge/Watch%20Live%20Stream-YouTube-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/live/Qxjp4Emuyj8)

これは、**AIが自身でゲーム（スーパーマリオブラザーズ）の攻略法を学びながら、視聴者とリアルタイムで対話する**、全自動のAITuber（AI VTuber）ゲーム配信プロジェクトです。

**👇 実際の配信アーカイブはこちら！**
### [https://www.youtube.com/live/Qxjp4Emuyj8](https://www.youtube.com/live/Qxjp4Emuyj8)
![スクリーンショット 2025-06-23 123137](https://github.com/user-attachments/assets/4bf4d942-6b87-4bde-9a3d-3fe2608a1cf9)

---

## 🌟 プロジェクトの概要 (Project Overview)

このプロジェクトは、単にゲームをプレイするAIではありません。以下の2つのAIが連携して、一つのキャラクターとして振る舞います。

1.  **プレイヤーAI (強化学習)**
    -   **Deep Q-Network (DQN)** アルゴリズムを用いて、試行錯誤を繰り返しながらリアルタイムでマリオの操作を学習します。最初はジャンプすらおぼつかない状態から、徐々にステージを攻略していきます。

2.  **コメンテーターAI (大規模言語モデル)**
    -   **OpenAI API (GPTシリーズ)** を活用し、YouTubeのコメント欄に寄せられる視聴者からのコメントを理解し、人間らしい自然な対話を行います。
    -   ゲームの状況（成功、失敗など）に応じて、感情豊かなコメントを生成することも可能です。

これら2つのAIが、**VRM**フォーマットの3Dアバターと連動し、あたかも一人のAITuberが思考し、プレイし、会話しているかのような配信を全自動で実現します。

## 💡 プロジェクトの核心と挑戦 (Core Concept & Challenges)

このプロジェクトの最大の挑戦は、**性質の異なる2つのAI（強化学習エージェントと大規模言語モデル）を一つのシステムに統合し、一貫したキャラクターとして機能させること**です。

-   **ゲームプレイと実況の連携**: プレイヤーAIの行動（例：クリア、ミス）をトリガーとして、コメンテーターAIが適切な実況や感想を述べます。
-   **視聴者とのインタラクション**: 視聴者の応援やアドバイスが、コメンテーターAIの応答を通じてプレイヤーAIの行動に（間接的に）影響を与えるようなインタラクティブな体験を目指します。
-   **リアルタイム処理**: ゲームプレイ、コメント取得、応答生成、音声合成、アバター制御など、すべてを低遅延で処理し、ライブ配信として成立させる必要があります。

## 🛠️ システム構成と使用技術 (System Architecture & Tech Stack)

このプロジェクトは、主に以下の技術要素から構成されるPythonアプリケーションです。

-   **メイン言語**: `Python`
-   **ゲームプレイ (強化学習)**:
    -   `Deep Q-Network (DQN)`
    -   `gym-super-mario-bros` (OpenAI Gym互換のマリオ環境)
    -   `PyTorch` / `TensorFlow`
-   **視聴者との対話 (LLM)**:
    -   `OpenAI API (gpt-4)`
    -   `YouTube Data API` (コメント取得)
    -   `VOICEVOX`
-   **アバター制御**:
    -   `VRM` (3Dアバターフォーマット)
    -   `Vmagic Mirror`
-   **カテゴリ**: `AITuber` / `VTuber`


## 🚀 ローカルでの実行方法 (Getting Started)

このプロジェクトをご自身の環境で動かすには、いくつかの設定が必要です。

1.  **リポジトリをクローン**
    ```sh
    git clone https://github.com/your-username/your-repository.git
    ```
2.  **ディレクトリに移動**
    ```sh
    cd your-repository
    ```
3.  **依存関係をインストール**
    ```sh
    pip install -r requirements.txt
    ```
4.  **環境変数を設定**
    `.env.example` を参考に `.env` ファイルを作成し、以下のキーを設定してください。
    -   `OPENAI_API_KEY`: OpenAIのAPIキー
    -   `YOUTUBE_API_KEY`: YouTube Data APIのキー
    -   `YOUTUBE_LIVE_ID`: 対象となるYouTubeライブ配信のID

5.  **アプリケーションを実行**
    ```sh
    python main.py
    ```
