import tkinter as tk
import ai_call

positions = ["QB","RB","WR","TE","FLEX","DST","K","BENCH"]

def main():
    root = tk.Tk()
    root.title("Fantasy AI")
    root.geometry("1080x720")

    canvas = tk.Canvas(root)
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    canvas.create_window((400, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill='both', expand=True)
    scrollbar.pack(side="right", fill="y")  

    label = tk.Label(scrollable_frame, text="Welcome to Fantasy AI", font=("Arial", 24))
    label.pack(pady=20)

    start_button = tk.Button(scrollable_frame, text="Create New Roster", font=("Arial", 18),command=lambda:start_new_roster(scrollable_frame,start_button,label))
    start_button.pack(pady=10)
    root.mainloop()

def start_new_roster(scroll,button,header):
    header.config(text="Create New Roster")
    button.pack_forget()
    current_fields = []
    for pos in positions:
        pos_label = tk.Label(scroll, text=f"Enter number of {pos}s:", font=("Arial", 18))
        pos_label.pack(pady=10)
        current_fields.append(pos_label)
        pos_entry = tk.Entry(scroll, font=("Arial", 18), width=10)
        pos_entry.pack(pady=5)
        current_fields.append(pos_entry)

    confirm_button = tk.Button(scroll, text="Create New Roster", font=("Arial", 18),command=lambda:input_players(scroll,current_fields,confirm_button))
    confirm_button.pack(pady=10)

def input_players(Window,fields,button):
    button.pack_forget()
    field_size = []
    j = 0
    for j in range(len(fields)):
        if(j%2 != 0):
            field_size.append(fields[j].get())
        fields[j].pack_forget()
    player_fields = []
    player_names = []
    j = 0
    for limit in field_size:
        i = 0
        while (i < int(limit)):
            player_label = tk.Label(Window, text=f"Enter name of {positions[j]} #{i+1}:", font=("Arial", 18))
            player_label.pack(pady=5)
            player_fields.append(player_label)
            player_entry = tk.Entry(Window, font=("Arial", 18), width=20)
            player_entry.pack(pady=5)
            player_fields.append(player_entry)
            i += 1
        j += 1

    submit_button = tk.Button(Window, text="Submit Players", font=("Arial", 18),command=lambda:ai_call.call_ai("Who won the Eagles vs Cowboys game?"))
    submit_button.pack(pady=10)



if __name__ == "__main__":
    main()