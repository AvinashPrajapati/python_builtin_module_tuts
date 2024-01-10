import random

def get_light_color():
    r = random.randint(150, 240)
    g = random.randint(150, 240)
    b = random.randint(150, 240)
    #often 0-100 dark
    #150-255 -> light

    color = "#{:02x}{:02x}{:02x}".format(r,g,b)
    return color



def generate_matching_dark_color(color:str):
    color = color.lstrip("#")

    r, g,b = int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16)
    # print(r,g,b)
    dark_r, dark_g, drak_b = 255-r, 255-g, 255-b
    light_color_matching = "#{:02x}{:02x}{:02x}".format(dark_r,dark_g,drak_b)
    return light_color_matching


new_color= get_light_color()
print(new_color)

matching_light_color = generate_matching_dark_color(new_color)
print(matching_light_color)