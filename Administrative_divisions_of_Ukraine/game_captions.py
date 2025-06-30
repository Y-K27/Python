import pandas
from turtle import Turtle
from labels import labels

class GameCaptions(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.regions_df = pandas.read_csv("ua_oblasts.csv")
        self.chosen_language = ""
        self.chosen_language_labels = {}
        self.regions_names_list = []
        self.dict_of_regions_position = {}

    def clear_region_caption(self):
        self.clear()

    def change_language(self, language_code:str):
        self.chosen_language_labels = labels[language_code]
        self.regions_names_list = self.regions_df[self.chosen_language_labels["division_name"]].tolist()
        self.dict_of_regions_position = {"X" : self.regions_df["position_x"].tolist(),
                                         "Y" : self.regions_df["position_y"].tolist()}

    def region_capture_writer(self, entered_name_of_region):
        division = self.regions_df[self.regions_df[self.chosen_language_labels["division_name"]] == entered_name_of_region]
        self.goto(division["X"].item(), division["Y"].item())
        self.write(division[self.chosen_language_labels["division_name"]].item(), align="center", font=("Arial", 12, "bold"))

