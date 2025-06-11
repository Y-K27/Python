import turtle
import pandas
from labels import labels

PREFERRED_LANGUAGE = ""
screen = turtle.Screen()
screen.setup(1290, 890)
# Choose the language
while not PREFERRED_LANGUAGE:
    chosen_language = screen.textinput("Choose preferred language:", prompt="Enter 'UA' to play in Ukrainian, or 'EN' to play in English.").lower()
    if chosen_language == "ua" or chosen_language == "en":
        PREFERRED_LANGUAGE = labels[chosen_language]

screen.title(PREFERRED_LANGUAGE["screen_title"])
screen.screensize(1290,890)
screen.bgcolor("black")
image = "clear_images/region_clear.gif"
screen.addshape(image)
turtle.shape(image)

#create new Turtle() object for caption
captures = turtle.Turtle()
captures.hideturtle()
captures.penup()

# Take data from file
states_data = pandas.read_csv("ua_oblasts.csv")
##create the list with  all states
divisions_list = states_data[PREFERRED_LANGUAGE["division_name"]].tolist()
turtle_list = []

guessed_divisions = []

while len(guessed_divisions) < 25:
    answer_state = screen.textinput(f"{len(guessed_divisions)}/{len(divisions_list)} {PREFERRED_LANGUAGE["screen_textinput_title"]}",
                                    prompt=PREFERRED_LANGUAGE["screen_textinput_prompt"]).title()
    if answer_state == PREFERRED_LANGUAGE["phrase_to_finish_the_game"]:
        break
    if answer_state in divisions_list:
        div_image = "clear_images/" + str(divisions_list.index(answer_state)) + ".gif"
        screen.addshape(div_image)
        div_turtle = turtle.Turtle()
        div_turtle.shape(div_image)
        turtle_list.append(div_turtle)
        guessed_divisions.append(answer_state)
        division = states_data[states_data[PREFERRED_LANGUAGE["division_name"]] == answer_state]
        captures.goto(division["X"].item(), division["Y"].item())
        captures.write(answer_state, align="center", font=("Arial", 12, "bold"))

#save didn't guess divisions to learn.csv file
to_learn_states = list(set(divisions_list) - set(guessed_divisions))
dict_to_learn_states = {'states':list(set(divisions_list) - set(guessed_divisions))}
pandas.DataFrame(dict_to_learn_states).to_csv("learn_states.csv")
