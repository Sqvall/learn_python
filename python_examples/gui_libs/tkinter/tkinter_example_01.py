from tkinter import Tk, Frame, BOTH


class Example(Frame):
    """ Simple example window """
    def __init__(self, parent):
        super().__init__(background="black")  # Set background
        # Frame.__init__(self, parent, background="white")
        self.parent = parent  # Save link parent widget
        self.init_UI()  # Delegate create UI another method

    def init_UI(self):
        self.parent.title("Simple")  # Set title window
        self.pack(fill=BOTH, expand=1)  # Set geometry manager


def main():
    root = Tk()  # Create main(root) window
    root.geometry("250x150+300+300")  # Set replace geometry
    app = Example(root)  # Create instance app
    root.mainloop()  # Run event handling


if __name__ == '__main__':
    main()
