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
    current_fields = []
    QB_Label = tk.Label(Tk_window,text="Enter number of QBs:",font=("Arial",18))
    QB_Label.pack(pady=5)
    current_fields.append(QB_Label)
    QB_Entry = tk.Entry(Tk_window,font=("Arial",18),width=10)
    QB_Entry.pack(pady=5)
    current_fields.append(QB_Entry)

    RB_Label = tk.Label(Tk_window,text="Enter number of RBs:",font=("Arial",18))
    RB_Label.pack(pady=5)
    current_fields.append(RB_Label)
    RB_Entry = tk.Entry(Tk_window,font=("Arial",18),width=10)
    RB_Entry.pack(pady=5)
    current_fields.append(RB_Entry)

    WR_Label = tk.Label(Tk_window,text="Enter number of WRs:",font=("Arial",18))
    WR_Label.pack(pady=5)
    current_fields.append(WR_Label)
    WR_Entry = tk.Entry(Tk_window,font=("Arial",18),width=10)
    WR_Entry.pack(pady=5)
    current_fields.append(WR_Entry)

    FLEX_Label = tk.Label(Tk_window,text="Enter number of FLEXs:",font=("Arial",18))
    FLEX_Label.pack(pady=5)
    current_fields.append(FLEX_Label)
    FLEX_Entry = tk.Entry(Tk_window,font=("Arial",18),width=10)
    FLEX_Entry.pack(pady=5)
    current_fields.append(FLEX_Entry)

    DST_Label = tk.Label(Tk_window,text="Enter number of D/STs:",font=("Arial",18))
    DST_Label.pack(pady=5)
    current_fields.append(DST_Label)
    DST_Entry = tk.Entry(Tk_window,font=("Arial",18),width=10)
    DST_Entry.pack(pady=5)
    current_fields.append(DST_Entry)

    K_Label = tk.Label(Tk_window,text="Enter number of Ks:",font=("Arial",18))
    K_Label.pack(pady=5)
    current_fields.append(K_Label)
    K_Entry = tk.Entry(Tk_window,font=("Arial",18),width=10)
    K_Entry.pack(pady=5)
    current_fields.append(K_Entry)

    B_Label = tk.Label(Tk_window,text="Enter number of BENCHs:",font=("Arial",18))
    B_Label.pack(pady=5)
    current_fields.append(B_Label)
    B_Entry = tk.Entry(Tk_window,font=("Arial",18),width=10)
    B_Entry.pack(pady=5)
    current_fields.append(B_Entry)

    confirm_button = tk.Button(Tk_window, text="Create New Roster", font=("Arial", 18),command=lambda:input_players(Tk_window,current_fields,confirm_button))
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
    for limit in field_size:
        i = 0
        while (i < int(limit)):
            player_label = tk.Label(Window, text=f"Enter name of Player {i+1}:", font=("Arial", 18))
            player_label.pack(pady=5)
            player_fields.append(player_label)
            player_entry = tk.Entry(Window, font=("Arial", 18), width=20)
            player_entry.pack(pady=5)
            player_fields.append(player_entry)
            i += 1
    submit_button = tk.Button(Window, text="Submit Players", font=("Arial", 18))
    submit_button.pack(pady=10)

if __name__ == "__main__":
    main()