import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

class SimpleEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Mini Editor for Compiler")
        self.master.geometry("800x600")

        # Create Text Area
        self.text_area = tk.Text(self.master, wrap="word", undo=True)
        self.text_area.pack(expand=True, fill="both")

        # Create Menu
        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)

        # File Menu
        file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)

        # Edit Menu
        edit_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=lambda: self.text_area.event_generate('<<Cut>>'))
        edit_menu.add_command(label="Copy", command=lambda: self.text_area.event_generate('<<Copy>>'))
        edit_menu.add_command(label="Paste", command=lambda: self.text_area.event_generate('<<Paste>>'))

        # Run Menu (placeholder for compiler)
        run_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Run", menu=run_menu)
        run_menu.add_command(label="Run Code", command=self.run_code)

        # Help Menu
        help_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(self.text_area.get(1.0, tk.END))

    def run_code(self):
        # Placeholder: save and run code using system Python
        code = self.text_area.get(1.0, tk.END).strip()
        if not code:
            messagebox.showwarning("Run", "No code to run!")
            return

        with open("temp_code.py", "w", encoding="utf-8") as f:
            f.write(code)

        try:
            output = subprocess.check_output(["python", "temp_code.py"], stderr=subprocess.STDOUT, text=True)
            messagebox.showinfo("Output", output)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", e.output)

    @staticmethod
    def show_about():
        messagebox.showinfo("About", "Simple Editor for Compiler\nCreated with Tkinter")


if __name__ == "__main__":
    root = tk.Tk()
    editor = SimpleEditor(root)
    root.mainloop()