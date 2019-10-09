from tkinter import Tk, Frame, BOTH


class Example(Frame):
    """ Place window center """

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.parent.title("Centered window")
        self.pack(fill=BOTH, expand=1)
        self.center_window()

    def center_window(self):
        w = 290
        h = 150

        sw = self.parent.winfo_screenwidth()  # Get screen width
        sh = self.parent.winfo_screenheight()  # Get screen width

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))


def main():
    root = Tk()
    ex = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
