# This is a sample Python script.
from PIL import Image, ImageFont, ImageDraw
import math, csv
import pandas as pd


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def get_entity(row):
    entity = {"name": row[0],
              "attack": str(row[1]),
              "hp": str(row[2]),
              "armor": str(row[3]),
              "actions": str(row[4]),
              "str_val": str(row[5]),
              "int_val": str(row[6]),
              "char_val": str(row[7]),
              "agility_val": str(row[8]),
              "condition_val":str(row[9]),
              "to_hit": row[10],
              "img_path": row[11]}
    print(f"ent: {entity}")
    return entity


def draw_card(entity):
    print(entity)
    my_image = Image.open("imgs/Template.jpg")
    image = Image.open(entity['img_path']).resize((453, 323))

    ############

    my_image.paste(image, (110, 128))

    label_font = ImageFont.truetype('fonts/AQS.ttf', 20)
    name_font = ImageFont.truetype('fonts/AQS.ttf', 26)
    statsFont = ImageFont.truetype('fonts/LittleLordFontleroyNF.ttf', 125)
    valFont = ImageFont.truetype('fonts/LittleLordFontleroyNF.ttf', 85)

    image_editable = ImageDraw.Draw(my_image)

    image_editable.text((700, 121), entity['attack'], (0, 0, 0), font=statsFont)

    image_editable.text((700, 345), entity['hp'], (0, 0, 0), font=statsFont)

    image_editable.text((700, 560), entity['armor'], (0, 0, 0), font=statsFont)

    image_editable.text((700, 790), entity['actions'], (0, 0, 0), font=statsFont)

    # image_editable.text((200, 411), str_label, (0, 0, 0), font=label_font)
    #
    # image_editable.text((430, 370), entity['str_val'], (0, 0, 0), font=valFont)

    intelligence_label = "Intelligence "
    image_editable.text((370, 481), intelligence_label, (0, 0, 0), font=label_font)

    image_editable.text((130, 441), entity['int_val'], (0, 0, 0), font=valFont)

    str_label = "Strength "
    image_editable.text((200, 551), str_label, (0, 0, 0), font=label_font)

    image_editable.text((430, 511), entity['str_val'], (0, 0, 0), font=valFont)

    charisma_label = "Charisma "
    image_editable.text((370, 621), charisma_label, (0, 0, 0), font=label_font)

    image_editable.text((130, 581), entity['char_val'], (0, 0, 0), font=valFont)

    agility_label = "Agility "
    image_editable.text((200, 685), agility_label, (0, 0, 0), font=label_font)

    image_editable.text((430, 645), entity['agility_val'], (0, 0, 0), font=valFont)

    w, h = image_editable.textsize(entity['name'])
    print(w)
    image_editable.text(((820 - w * 2) / 2, 50), entity['name'], (0, 0, 0), font=name_font)

    print(entity['to_hit'])
    to_hit = entity['to_hit']
    y_axis_base = 730
    for i in range(to_hit + 1):
        image_editable.text((y_axis_base - i * 69, 1055), "X", (0, 0, 0), font=valFont)

    my_image.save(f"target/characters/{entity['name']}.jpg")
    ##########
def generate():
    with open('db/mobs.csv', newline='') as f:
      reader = pd.read_csv(f)
      for index, row in reader.iterrows():
          entity = get_entity(row)

          draw_card(entity)

