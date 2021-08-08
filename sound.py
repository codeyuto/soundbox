import tkinter as tk

from tkinter import ttk
from pygame import mixer

import inspect
# Define
BUTTON = [
    ['1', '2', '3', '4'],
    ['5', '6', '7', '8'],
    ['9', '10', '11', '12']
]
 


 
# サウンドボックス
class SoundGui(object):
    def __init__(self, app=None):
        # Window Setting
        app.title('my sound box') # Window のタイトル
        app.geometry('300x200') # Window のサイズ

        # Frame Setting
        button_frame = ttk.Frame(app, width=300, height=400) # ボタンFrame
        button_frame.propagate(False) # サイズが固定される
        button_frame.pack(side=tk.BOTTOM) # 余白の設定
 
        # Parts Setting
        for y, row in enumerate(BUTTON, 1): # Buttonの配置
            for x, num in enumerate(row):
                button = tk.Button(button_frame, text=num, font=('', 15), width=5, height=2)
                button.grid(row=y, column=x) # 列や行を指定して配置
                button.bind('<Button-1>', self.click_button) # Buttonが押された場合
    
    def click_button(self, event):
        check = event.widget['text'] # 押したボタンのCheck
        mixer.music.load("test.mp3")
        mixer.music.play(1)
 
        if check == '1':
            mixer.music.load("test2.mp3")

        elif check == '2':
            mixer.music.load("test3.mp3")

        elif check == '3':

            mixer.music.load("test.mp3")
        else:
            mixer.music.load("test.mp3")

        mixer.music.play(1)
    
 
 
 
def main():
    app = tk.Tk()
    mixer.init()
    app.resizable(width=False, height=False)
    SoundGui(app)
    app.mainloop()
 
if __name__ == '__main__':
    main()