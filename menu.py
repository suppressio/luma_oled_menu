class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Menu:
    def __init__(self, id, name, icon, icon_style, description, command):
        self.id = id
        self.name = name
        self.icon = icon
        self.icon_style = icon_style
        self.description = description
        self.command = command

pri_color = "white"
sec_color = "red"
ter_color = "green"
shadow_color = "black"
shadow_offset = 2
selection_rect = Coords(25, 22)
spacer = Coords(30, 26)
size = Coords(8, 2)
pos = Coords(13, 2)

def draw_lines(draw):
    draw.line((8, 0, 8, 64), fill="red")
    draw.line((0, 25, 256, 25), fill="red")
    #draw.line((128, 0, 128, 64), fill="red")
    draw.line((0, 51, 256, 51), fill="red")
    draw.line((248, 0, 248, 64), fill="red")


def draw_graph_menu_element(draw, position, selected, icon, font):

    if (position < 1) & (position > (size.x * size.y)):
        print("Error: wrong position")
        return

    position = position-1
    x = ( ( ( position %  size.x ) ) * spacer.x ) + pos.x
    y = ( ( ( position // size.x ) ) * spacer.y ) + pos.y
    #print("I:"+str(position)+" - X:"+str(x)+" - Y:"+str(y));

    if selected:
        draw.rectangle((x-4, y-2, x+selection_rect.x, y+selection_rect.y), outline=pri_color, fill=ter_color)
    draw.text((x+shadow_offset, y+shadow_offset), icon, fill=shadow_color, font=font)
    draw.text((x, y), icon, fill=pri_color, font=font)

def draw_descr_command(draw, descr_text, font):
    draw.text((60, 52), descr_text, fill=sec_color, font=font)
    draw.text((59, 50), descr_text, fill=pri_color, font=font)
