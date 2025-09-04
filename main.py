import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Fantasy AI")
    root.geometry("1080x720")

    label = tk.Label(root, text="Welcome to Fantasy AI", font=("Arial", 24))
    label.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()