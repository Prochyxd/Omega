import tkinter as tk
from compression import compression
from log_manager import LogManager
from user_interface import UserInterface

def run_compression_gui():
    def read_guide():
        UserInterface.show_guide()

    def start_compression():
        compression()
        LogManager.log_activity("Compression program opened", "Compression")

    root = tk.Tk()
    root.title("Compression GUI")

    label = tk.Label(root, text="Welcome to Text Compression")
    label.pack()

    guide_button = tk.Button(root, text="Read Guide", command=read_guide)
    guide_button.pack()

    compress_button = tk.Button(root, text="Start Compression", command=start_compression)
    compress_button.pack()

    root.mainloop()

if __name__ == "__main__":
    run_compression_gui()
