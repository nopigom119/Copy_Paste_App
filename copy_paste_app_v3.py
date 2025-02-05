import tkinter as tk
import pyperclip
from tkinter import scrolledtext, messagebox

class TextArea:
    def __init__(self, master, index):
        self.index = index
        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, height=10)
        self.text_area.grid(row=index, column=0, sticky="nsew", padx=10, pady=5)
        self.copy_button = tk.Button(master, text="복사", command=self.copy_text)
        self.copy_button.grid(row=index, column=1, sticky="n", pady=5)
        self.x_button = tk.Button(master, text="X", command=self.remove_text_area)
        self.x_button.grid(row=index, column=2, sticky="ne", padx=5, pady=5)

    def copy_text(self):
        try:
            text_to_copy = self.text_area.get("1.0", tk.END).rstrip()
            pyperclip.copy(text_to_copy)
        except pyperclip.PyperclipException as e:
            messagebox.showerror("오류 발생", f"클립보드 복사 중 오류 발생: {e}")
        except Exception as e:
            messagebox.showerror("오류 발생", f"예상치 못한 오류 발생: {e}")

    def remove_text_area(self):
        self.text_area.grid_forget()
        self.copy_button.grid_forget()
        self.x_button.grid_forget()
        text_areas.remove(self)
        for i, area in enumerate(text_areas):
            area.text_area.grid(row=i, column=0)
            area.copy_button.grid(row=i, column=1)
            area.x_button.grid(row=i, column=2)
        root.update()
        window_height = root.winfo_reqheight()
        root.geometry(f"400x{window_height}")

root = tk.Tk()
root.title("텍스트 복사 앱")
root.columnconfigure(0, weight=1)

text_areas = []

def add_text_area():
    text_area = TextArea(root, len(text_areas))
    text_areas.append(text_area)
    root.update()
    window_height = root.winfo_reqheight()
    root.geometry(f"400x{window_height}")

add_button = tk.Button(root, text="+", command=add_text_area)
add_button.grid(row=0, column=3, sticky="n", padx=10, pady=10)

add_text_area()

root.mainloop()