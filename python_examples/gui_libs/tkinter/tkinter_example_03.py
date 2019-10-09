from tkinter import Tk, BOTH, Frame, Button


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.init_UI()

    def init_UI(self):
        self.parent.title("Quit button")  # Set title window
        self.parent.geometry("250x150+300+300")  # Set geometry manager
        # self.style = Style()  # This not work, in example need from ttk import Frame, Button, Style
        # self.style.theme_use("default")

        self.pack(fill=BOTH, expand=1)  # Set geometry manager

        quit_button = Button(self, text="Quit",
                             command=self.quit)  # Create button, self.quit it is ready method in class Misc
        quit_button.place(x=50, y=50)  # Place button on top/left


def main():
    root = Tk()
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
