# This is a sample Python script.
from PIL import Image, ImageFont, ImageDraw
import math, csv
import pandas as pd


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def get_entity(row):
    entity = {"name": row[0],
              "ap_cost": str(row[1]),
              "cooldown": str(row[2]),
              "type": str(row[3]),
              "text": str(row[4])}
    print(f"ent: {entity}")
    return entity

def draw_card(entity):
    my_image = Image.open(f"imgs/backgrounds/{entity['type']}.jpg").resize((900,1000))
    image = Image.open("imgs/backgrounds/Scroll.jpg").resize((835, 350))
    overhowl = Image.open("imgs/backgrounds/overhoul.jpg")
    image_editable = ImageDraw.Draw(overhowl)


    overhowl = overhowl.convert("RGBA")
    ############
    datas = overhowl.getdata()

    label_font = ImageFont.truetype('fonts/AQS.ttf', 20)
    name_font = ImageFont.truetype('fonts/AQS.ttf', 16)
    statsFont = ImageFont.truetype('fonts/LittleLordFontleroyNF.ttf', 100)
    valFont = ImageFont.truetype('fonts/LittleLordFontleroyNF.ttf', 85)

    my_image = my_image.convert("RGBA")




    my_image=my_image.resize((900, 1000))
    overhowl=overhowl.resize((900, 1000))


    datas = overhowl.getdata()

    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    overhowl.putdata(newData)

    a=Image.alpha_composite(my_image, overhowl)
    a=a.convert("RGB")
    a.paste(image, (30, 630))

    datas2 = a.getdata()
    newData2 = []

    ##for red cards
    if entity['type'] == 'fire':
        for item in datas2:
            if item[0] > 240 and item[1] > 240 and item[2] > 240:
                newData2.append((0, 0, 0, 0))
            else:
                newData2.append(item)
        a.putdata(newData2)

    ##for red cards
    if entity['type'] == 'nature':
        for item in datas2:
            if item[0] > 240 and item[1] > 240 and item[2] > 240:
                newData2.append((155, 244, 133, 0))
            else:
                newData2.append(item)
        a.putdata(newData2)

    ##for red cards
    if entity['type'] == 'hunt':
        for item in datas2:
            if item[0] > 240 and item[1] > 240 and item[2] > 240:
                newData2.append((100, 155, 77, 0))
            else:
                newData2.append(item)
        a.putdata(newData2)

    skill_img = Image.open(f"imgs/spells/{entity['name']}.jpg")
    skill_img = skill_img.resize((623, 465))
    a.paste(skill_img, (130, 150))
    a = a.resize((238, 333))

    a.save(f"target/{entity['name']}.jpg")
        ##########

    add = Image.open(f"target/{entity['name']}.jpg")
    edit = ImageDraw.Draw(add)
    print(str(edit))
    print(entity['ap_cost'])
    edit.text((0, -35), entity['ap_cost'], (0, 0, 133), font=statsFont)
    edit.text((70, 5), entity['name'], (0, 0, 0), font=name_font)
    edit.text((195, -35), entity['cooldown'], (0, 0, 0), font=statsFont)
    add.save(f"target/{entity['name']}.jpg")


with open('db/spells.csv', newline='') as f:
  reader = pd.read_csv(f)
  for index, row in reader.iterrows():
      entity = get_entity(row)

      draw_card(entity)
