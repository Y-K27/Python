import turtle
from tkinter import ttk
from regions_class import Regions
from game_captions import GameCaptions
import tkinter

from random import choice

LVL ="easy"
mouse_screen_click_flag = True

captures = GameCaptions()
regions_of_ua = Regions()

screen = turtle.Screen()
screen.setup(1290, 890)

tkinter_canvas = screen.getcanvas()
tkinter_root = tkinter_canvas.winfo_toplevel()
entry_field_variable = tkinter.StringVar()


def load_progress():
    captures.chosen_language = "en"
    captures.change_language(captures.chosen_language)
    screen.title(captures.chosen_language_labels["screen_title"])
    image = "clear_images/region_clear.gif"
    screen.addshape(image)
    turtle.hideturtle()
    turtle.shape(image)

    for file in range(25):
        file_path = "clear_images/" + str(file) + ".gif"
        screen.addshape(file_path)
        progress.step()

    regions_of_ua.create_region_list(captures.dict_of_regions_position)
    progress.step(24)

    progress.place_forget()
    turtle.showturtle()

# the progress bar
progress = ttk.Progressbar(tkinter_root,length = 300,value=60, mode = 'determinate')
progress.place(x=495, y=440)
load_progress()

lbl_to_entry_field_text = tkinter.StringVar()
lbl_to_entry_field_text.set(captures.chosen_language_labels["lbl_to_entry_field_text"])
lbl_to_entry_field = tkinter.Label(tkinter_root,
                                   textvariable=lbl_to_entry_field_text,
                                   bg="#ffffff",
                                   font=("Arial", 16, "bold"))
lbl_to_entry_field.place(x=100, y=570)

lbl_to_choose_difficulty_text = tkinter.StringVar()
lbl_to_choose_difficulty_text.set(captures.chosen_language_labels["lbl_to_choose_difficulty_text"])
lbl_to_choose_difficulty= tkinter.Label(tkinter_root,
                                    textvariable=lbl_to_choose_difficulty_text,
                                    bg="#ffffff",
                                    font=("Arial", 10))
lbl_to_choose_difficulty.place(x=20, y=60)

tkinter_entry_field = tkinter.Entry(tkinter_root,border=3, textvariable=entry_field_variable)
tkinter_entry_field.place(x=100, y=600, width=250, height=30)
tkinter_entry_field.config(state="disabled")

selected_option = tkinter.StringVar(value="en")

def show_selection():
    #print(regions_of_ua.guessed_region_list)
    captures.clear_region_caption()
    #regions_of_ua.clean_all_region()
    captures.change_language(selected_option.get())
    screen.title(captures.chosen_language_labels["screen_title"])
    lbl_to_entry_field_text.set(captures.chosen_language_labels["lbl_to_entry_field_text"])
    lbl_to_choose_difficulty_text.set(captures.chosen_language_labels["lbl_to_choose_difficulty_text"])
    difficult_change_radio_btn_easy.config(text=captures.chosen_language_labels["easy"])
    difficult_change_radio_btn_medium.config(text=captures.chosen_language_labels["medium"])
    difficult_change_radio_btn_hard.config(text=captures.chosen_language_labels["hard"])
    for region in regions_of_ua.guessed_region_list:
        captures.region_capture_writer(captures.regions_names_list[region])


language_radio_btn_ua = tkinter.Radiobutton(tkinter_root,
                                            text="UA",
                                            bg="#ffffff",
                                            variable=selected_option,
                                            value="ua",
                                            command=show_selection)
language_radio_btn_en = tkinter.Radiobutton(tkinter_root,
                                            text="EN",
                                            bg="#ffffff",
                                            variable=selected_option,
                                            value="en",
                                            command=show_selection)

language_radio_btn_ua.place(x=20, y=20)
language_radio_btn_en.place(x=70, y=20)


def lvl_easy_entry_name_of_region(event=None):
    regions_of_ua.player_answer = tkinter_entry_field.get().title()
    entry_field_variable.set('')
    if regions_of_ua.player_answer != "" and regions_of_ua.player_answer == captures.chosen_language_labels["phrase_to_finish_the_game"]:
        print("The game is over")
    if regions_of_ua.player_answer != "" and regions_of_ua.player_answer in captures.regions_names_list:
        if captures.regions_names_list.index(regions_of_ua.player_answer) not in regions_of_ua.guessed_region_list:
            regions_of_ua.show_region(captures.regions_names_list.index(regions_of_ua.player_answer))
            captures.region_capture_writer(regions_of_ua.player_answer)
            regions_of_ua.guessed_region_list.append(captures.regions_names_list.index(regions_of_ua.player_answer))
        else:
            print("the region is already guessed")
    if len(regions_of_ua.guessed_region_list) == 25:
        print("the game is over! You won!")


def lvl_medium_entered_answer(event):
    global mouse_screen_click_flag
    regions_of_ua.player_answer = tkinter_entry_field.get().title()
    if regions_of_ua.player_answer  and regions_of_ua.player_answer in captures.regions_names_list:
        regions_of_ua.guessed_region_list.append(captures.regions_names_list.index(regions_of_ua.player_answer))
        captures.region_capture_writer(regions_of_ua.player_answer)
        mouse_screen_click_flag = True
        entry_field_variable.set('')
        tkinter_entry_field.config(state="disabled")
    else:
        print("Wrong answer")
        entry_field_variable.set('')

def lvl_medium_entry_name_of_chosen_region(x,y):
    global mouse_screen_click_flag
    if mouse_screen_click_flag and len(regions_of_ua.guessed_region_list)<=24:
        if regions_of_ua.count_distans_from_click_to_center_of_region(x,y):
            tkinter_entry_field.config(state="normal")
            tkinter_entry_field.focus()
            mouse_screen_click_flag = False



def lvl_hard_show_ramdom_chosen_region():
    print(regions_of_ua.guessed_region_list)
    if regions_of_ua.lvl_hard_random_chosen_region == '' or regions_of_ua.player_answer == regions_of_ua.lvl_hard_random_chosen_region:
        if len(regions_of_ua.guessed_region_list) <=24:
            regions_of_ua.lvl_hard_random_chosen_region = choice(captures.regions_names_list)
            while captures.regions_names_list.index(regions_of_ua.lvl_hard_random_chosen_region) in regions_of_ua.guessed_region_list:
                regions_of_ua.lvl_hard_random_chosen_region = choice(captures.regions_names_list)
        regions_of_ua.show_region(captures.regions_names_list.index(regions_of_ua.lvl_hard_random_chosen_region))

def lvl_hard_check_answer(event=None):
    regions_of_ua.player_answer= tkinter_entry_field.get().title()
    if len(regions_of_ua.guessed_region_list) <= 24:
        if regions_of_ua.player_answer and regions_of_ua.player_answer == regions_of_ua.lvl_hard_random_chosen_region:
            captures.region_capture_writer(regions_of_ua.lvl_hard_random_chosen_region)
            regions_of_ua.guessed_region_list.append(captures.regions_names_list.index(regions_of_ua.player_answer))
            lvl_hard_show_ramdom_chosen_region()
        else:
            print("wrong answer")
    else:
        print("You won!")
        tkinter_entry_field.config(state="disabled")
    entry_field_variable.set('')

def lvl_easy():
    tkinter_entry_field.bind("<Return>", lvl_easy_entry_name_of_region)
    tkinter_entry_field.config(state="normal")
    tkinter_entry_field.focus()


def lvl_medium():
    tkinter_entry_field.bind("<Return>", lvl_medium_entered_answer)
    screen.onclick(lvl_medium_entry_name_of_chosen_region, btn=1)


def lvl_hard():
    tkinter_entry_field.bind("<Return>", lvl_hard_check_answer)
    tkinter_entry_field.config(state="normal")
    tkinter_entry_field.focus()
    lvl_hard_show_ramdom_chosen_region()

def set_lvl_for_game():
    global LVL
    LVL = selected_difficult.get()
    tkinter_entry_field.config(state="disabled")
    captures.clear_region_caption()
    regions_of_ua.clean_all_region()

    #print(LVL)
    if LVL == "easy":
        lvl_easy()
    if LVL == "medium":
        lvl_medium()
    elif LVL == "hard":
        lvl_hard()

selected_difficult = tkinter.StringVar(value="easy")
difficult_change_radio_btn_easy = tkinter.Radiobutton(tkinter_root,
                                                        text=captures.chosen_language_labels["easy"],
                                                        bg="#ffffff", variable=selected_difficult,
                                                        value="easy",
                                                        command=set_lvl_for_game)
difficult_change_radio_btn_medium = tkinter.Radiobutton(tkinter_root,
                                                        text=captures.chosen_language_labels["medium"],
                                                        bg="#ffffff",variable=selected_difficult,
                                                        value="medium",
                                                        command=set_lvl_for_game)
difficult_change_radio_btn_hard = tkinter.Radiobutton(tkinter_root,
                                                        text= captures.chosen_language_labels["hard"],
                                                        bg="#ffffff",
                                                        variable=selected_difficult,
                                                        value="hard",
                                                        command=set_lvl_for_game)

difficult_change_radio_btn_easy.place(x=20, y=80)
difficult_change_radio_btn_medium.place(x=20, y=100)
difficult_change_radio_btn_hard.place(x=20, y=120)


if LVL == "easy":
    lvl_easy()
if LVL == "medium":
    lvl_medium()
elif LVL == "hard":
    lvl_hard()
    
turtle.mainloop()