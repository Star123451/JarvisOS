import tkinter as tk
from tkinter import filedialog, messagebox
import sys

class MiniIDE(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mini‑IDE")
        self.geometry("800x600")

        self.text = tk.Text(self, wrap="none")
        self.text.pack(expand=True, fill="both")

        run_btn = tk.Button(self, text="Run ▶️", command=self.run_code)
        run_btn.pack(side="bottom", fill="x")

        menu = tk.Menu(self)
        file_menu = tk.Menu(menu, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        menu.add_cascade(label="File", menu=file_menu)
        self.config(menu=menu)

    def open_file(self):
        path = filedialog.askopenfilename()
        if path:
            with open(path, "r") as f:
                self.text.delete("1.0", tk.END)
                self.text.insert(tk.END, f.read())

    def save_file(self):
        path = filedialog.asksaveasfilename(defaultextension=".py")
        if path:
            with open(path, "w") as f:
                f.write(self.text.get("1.0", tk.END))

    def run_code(self):
        code = self.text.get("1.0", tk.END)

        if hasattr(self, 'console'):
            self.console.delete("1.0", tk.END)
        else:
            self.console = tk.Text(self, height=8, bg="#111", fg="#eee")
            self.console.pack(fill="x")

        sys.stdout = self.console
        sys.stderr = self.console
        try:
            exec(code, {})
        except Exception as e:
            print(f"Error: {e}")
        finally:
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__

if __name__ == "__main__":
    MiniIDE().mainloop()