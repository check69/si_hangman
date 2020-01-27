from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys

from si_hangman import get_word, make_guess, find_all_elements


def paint_gallows(qp):
    qp.drawLine(75, 60, 75, 20)
    qp.drawLine(150, 20, 75, 20)
    qp.drawLine(150, 20, 150, 200)


class HangManGUI(QWidget):
    alphabet = ['a', 'b', 'c', 'd', 'e',
                'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r',
                's', 't', 'u', 'v', 'w', 'x',
                'y', 'z']

    keyPressed = pyqtSignal(str)
    POSX = 300
    POSY = 300
    WIDTH = 650
    HEIGHT = 450

    def __init__(self):
        self.buttonList = []
        super(HangManGUI, self).__init__()

        self.word = get_word()
        self.lives = 6
        self.gameState = 0
        self.guessed_letters = [""] * len(self.word)
        self.still_playing = True
        self.victory = False

        self.init_ui()

    def init_ui(self):
        self.keyPressed.connect(self.on_key)

        self.setGeometry(self.POSX, self.POSY, self.WIDTH, self.HEIGHT)
        self.setWindowTitle('Sports Interactive HangMan')
        self.show()

    def paint_body(self, qp: QPainter):
        # head
        if self.lives < 6:
            qp.drawEllipse(60, 60, 30, 30)
        # body
        if self.lives < 5:
            qp.drawLine(75, 90, 75, 135)
        # left arm
        if self.lives < 4:
            qp.drawLine(75, 105, 50, 100)
        # right arm
        if self.lives < 3:
            qp.drawLine(75, 105, 100, 100)
        # left leg
        if self.lives < 2:
            qp.drawLine(75, 135, 50, 160)
        # right leg
        if self.lives < 1:
            qp.drawLine(75, 135, 100, 160)

    def paint_hangman(self, qp: QPainter):
        pen = QPen(Qt.black, 3, Qt.SolidLine)
        qp.setPen(pen)

        paint_gallows(qp)
        self.paint_body(qp)

        # Text
        for i in range(len(self.guessed_letters)):
            add = 50 * i
            qp.drawText(40 + add, 240, self.guessed_letters[i])
            qp.drawLine(20 + add, 250, 60 + add, 250)

    def paint_victory(self, qp: QPainter):
        pen = QPen(Qt.red, 50, Qt.SolidLine)
        font = QFont()
        font.setStyleHint(QFont().Monospace)
        font.setFamily('monospace')
        font.setPixelSize(48)
        qp.setPen(pen)
        qp.setFont(font)
        if self.victory:
            qp.drawText(250, 200, "You Win")
        else:
            qp.drawText(250, 200, "You Lose")


    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        self.paint_hangman(qp)
        if not self.still_playing:
            self.paint_victory(qp)

        qp.end()

    def updateGame(self):
        if "".join(self.guessed_letters) == self.word:
            self.finish_game(True)
        elif not self.lives:
            self.finish_game(False)

    def onButtonClick(self, button):
        button.setEnabled(False)

    def keyPressEvent(self, key_event: QKeyEvent) -> None:
        super(HangManGUI, self).keyPressEvent(key_event)
        self.keyPressed.emit(key_event.text())
        if key_event.key() == Qt.Key_Escape:
            sys.exit(None)

    def on_key(self, key):
        if self.still_playing:
            if key in self.alphabet:
                if make_guess(self.word, key):
                    for pos in find_all_elements(self.word, key):
                        self.guessed_letters[pos] = key
                else:
                    self.lives -= 1

                self.updateGame()
                self.update()

    def finish_game(self, win: bool):
        self.still_playing = False
        self.victory = win
        pass


def main():
    app = QApplication(sys.argv)
    gui = HangManGUI()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
