from tkinter import *
from chatbot import get_response, bot_name

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 14 bold"


class ChatApplication:

    def __int__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.main.loop()

    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=BG_COLOR)

if __name__ == "__main__":
    app = ChatApplication
    app.run()
