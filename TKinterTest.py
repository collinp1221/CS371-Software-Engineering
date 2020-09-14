import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.hello_2 = tk.Button(self, command=self.say_hi_2, text="Hello World 2!", bg="#F00", anchor="sw")
        self.hello_2.pack(side="left")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    def say_hi_2(self):
        print("Hello again!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
