import openai
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont  # Add this line
from PyQt5.QtWebEngineWidgets import QWebEngineView

openai.api_key = "API_KEY_YOU"

class EnglishChat(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200, 700)

        self.init_ui()

    def init_ui(self):
        vb = QVBoxLayout(self)  # Pass the parent widget directly to QVBoxLayout

        hb1 = QHBoxLayout()
        vb.addLayout(hb1)

        vb1 = QVBoxLayout()
        hb1.addLayout(vb1)

        self.chat_btn = QPushButton("Chat")
        self.chat_btn.clicked.connect(self.generate_response)
        vb1.addWidget(self.chat_btn)

        self.splitter = QSplitter(Qt.Horizontal)
        hb1.addWidget(self.splitter)

        self.vsplitter1 = QSplitter(Qt.Vertical)
        self.splitter.addWidget(self.vsplitter1)

        self.vsplitter2 = QSplitter(Qt.Vertical)
        self.splitter.addWidget(self.vsplitter2)

        self.prompt_box = QTextEdit()
        self.prompt_box.setFont(QFont("Calibri", 20))
        self.vsplitter1.addWidget(self.prompt_box)

        self.learning_page = QWebEngineView()
        self.learning_page.setFont(QFont("Calibri", 16))
        self.vsplitter1.addWidget(self.learning_page)

        self.response_box = QTextBrowser()
        self.response_box.setFont(QFont("Calibri", 20))
        self.vsplitter2.addWidget(self.response_box)

        # Set initial sizes for the splitters
        self.vsplitter1.setSizes([int(self.height() * 0.30), int(self.height() * 0.70)])
        self.vsplitter2.setSizes([int(self.height() * 0.70), int(self.height() * 0.30)])
    
    def generate_response(self):
        prompt = self.prompt_box.toPlainText()

        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            n=1,  # You missed a comma here
            max_tokens=2048,
            temperature=.5
        )


        response = response.choices[0].text

        self.response_box.setText(response)




def main():
    app = QApplication(sys.argv)
    gui = EnglishChat()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
