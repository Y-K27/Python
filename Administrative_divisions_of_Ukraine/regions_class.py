from turtle import Turtle

class Regions(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.region_list= []
        self.guessed_region_list = []
        self.lvl_hard_random_chosen_region = ''
        self.player_answer  = ""


    def create_region_list(self,dict_regions_position):
        for i in range(25):
            div_image = "clear_images/"+str(i)+".gif"
            div_turtle = Turtle()
            div_turtle.hideturtle()
            div_turtle.speed(0)
            div_turtle.penup()
            div_turtle.goto(dict_regions_position["X"][i], dict_regions_position["Y"][i])
            div_turtle.shape(div_image)
            self.region_list.append(div_turtle)

    def show_region(self, index):
        self.region_list[index].showturtle()

    def clean_all_region(self):
        for item in self.region_list:
            item.hideturtle()
        self.guessed_region_list = []
        self.lvl_hard_random_chosen_region = ''
        self.player_answer = ""

    def count_distans_from_click_to_center_of_region(self, x,y):
        min_distance = 50
        the_region_index = ''
        for region in self.region_list:
            if region.distance(x,y) < min_distance:
                min_distance = region.distance(x,y)
                the_region_index = self.region_list.index(region)
        if min_distance < 50  and the_region_index != "":
            if the_region_index not in self.guessed_region_list:
                self.region_list[the_region_index].showturtle()
            else:
                print("the region is already guessed")
            return True
        else:
            return False

