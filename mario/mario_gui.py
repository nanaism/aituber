import sys

import numpy as np
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget


class MarioWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mario RL Training")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

        # メインウィジェットとレイアウトの設定
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)

        # ステータスラベルの設定
        self.status_label = QLabel("Episode: 0")
        self.status_label.setStyleSheet(
            """
            font-size: 20px;
            color: white;
            padding: 10px;
            background-color: rgba(0, 0, 0, 0.5);
            border-radius: 5px;
        """
        )
        self.status_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        layout.addWidget(self.status_label)

        # ゲーム画面の表示用ラベル
        self.game_label = QLabel()
        self.game_label.setAlignment(Qt.AlignCenter)
        self.game_label.setMinimumSize(640, 480)
        self.game_label.setStyleSheet(
            """
            border: 2px solid #333;
            background-color: black;
        """
        )
        layout.addWidget(self.game_label)

        # 学習中の表示用ラベル
        self.learning_label = QLabel("Learning...")
        self.learning_label.setStyleSheet(
            """
            font-size: 24px;
            color: white;
            padding: 20px;
            background-color: rgba(0, 0, 0, 0.7);
            border-radius: 10px;
        """
        )
        self.learning_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.learning_label)

        # ウィンドウの色設定
        self.setStyleSheet(
            """
            QMainWindow {
                background-color: #1a1a1a;
            }
            QWidget {
                background-color: #1a1a1a;
            }
        """
        )

        # 点滅するタイマーの設定
        self.dots = ""
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_dots)
        self.timer.start(500)

    def update_dots(self):
        """学習中の点滅アニメーション"""
        self.dots = "." * ((len(self.dots) + 1) % 4)
        self.learning_label.setText(f"Learning{self.dots}")

    def show_frame(self, frame):
        """ゲームフレームの表示"""
        self.learning_label.hide()

        if frame is None:
            return

        height, width, channels = frame.shape
        bytes_per_line = channels * width

        # フレームデータをバイト列に変換
        frame_data = frame.tobytes()

        # QImageを作成
        qt_image = QImage(
            frame_data, width, height, bytes_per_line, QImage.Format_RGB888
        )

        # QPixmapに変換してラベルに表示
        pixmap = QPixmap.fromImage(qt_image)
        scaled_pixmap = pixmap.scaled(
            self.game_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        self.game_label.setPixmap(scaled_pixmap)
        self.game_label.show()

    def show_learning(self):
        """学習中表示に切り替え"""
        self.game_label.hide()
        self.learning_label.show()

    def update_episode(self, episode):
        """エピソード番号の更新"""
        self.status_label.setText(f"Episode: {episode}")


def create_gui():
    """GUIを作成して返す"""
    app = QApplication(sys.argv)
    window = MarioWindow()
    window.show()
    return app, window


# 単体テスト用
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MarioWindow()
    window.show()
    sys.exit(app.exec_())
