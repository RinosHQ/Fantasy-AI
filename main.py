import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Fantasy AI")
    root.geometry("1080x720")

    label = tk.Label(root, text="Welcome to Fantasy AI", font=("Arial", 24))
    label.pack(pady=20)

    start_button = tk.Button(root, text="Create New Roster", font=("Arial", 18),command=lambda:start_new_roster(root,start_button))
    start_button.pack(pady=10)
    root.mainloop()

def start_new_roster(Tk_window,button):
    button.pack_forget()
    QB_Label = tk.Label(Tk_window,text="Enter number of QBs:",font=("Arial",18))
    QB_Label.pack(pady=5)
    QB_Entry = tk.Entry(Tk_window,font=("Arial",18),width=10)
    QB_Entry.pack(pady=5)

if __name__ == "__main__":
    main()