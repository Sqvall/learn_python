import tkinter as tk


class App:
    """"""

    def __init__(self, parent):
        """Constructor"""
        frame = tk.Frame(parent)
        frame.pack()
        self.parent = parent
        self.init_UI()

        btn_22 = tk.Button(
            frame,
            text="22",
            command=lambda: self.print_num(22)
        )
        btn_22.pack(side=tk.LEFT)

        btn_44 = tk.Button(
            frame,
            text="44",
            command=lambda: self.print_num(44)
        )
        btn_44.pack(side=tk.LEFT)

        quit_btn = tk.Button(frame, text="QUIT", fg="red", command=frame.quit)
        quit_btn.pack(side=tk.LEFT)

    @staticmethod
    def print_num(num):
        print(f"You press btn: {num}")

    def init_UI(self):
        self.parent.title("Simple")


if __name__ == "__main__":
    root = tk.Tk(baseName='TEST')
    root.geometry("220x100+550+300")
    app = App(root)
    root.mainloop()
