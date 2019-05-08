from PIL import Image
import colorsys
import os
import jsonlines
import json

def color_tag_image (image_file):
        red, orange, yellow, green, turquoise, blue, lilac, pink, white, gray, black, brown = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        image = []
#        print ('\n')
        try:
          if os.path.getsize(image_file) > 1000000: #image filesize limit required for servers with limited RAM resources
            raise ValueError('Error: File size is too large.')
          with Image.open(image_file) as image: #debug
            image = image.convert('RGBA').resize((64, 64), Image.ANTIALIAS) #debug
#          image = Image.open(image_file).convert('RGBA').resize((64, 64), Image.ANTIALIAS)
          for px in image.getdata():
                  h, s, l = colorsys.rgb_to_hsv(px[0]/255., px[1]/255., px[2]/255.)
                  h = h * 360
                  s = s * 100
                  l = l * 100

                  if l > 95:
                          white += 1
                  elif l < 8:
                          black += 1
                  elif s < 8:
                          gray += 1
                  elif h < 12 or h > 349:
                          red += 1
                  elif h > 11 and h < 35:
                          if s > 70:
                                  orange += 1
                          else:
                                  brown += 1
                  elif h > 34 and h < 65:
                          yellow += 1
                  elif h > 64 and h < 150:
                          green += 1
                  elif h > 149 and h < 200:
                          turquoise += 1
                  elif h > 195 and h < 240:
                          blue += 1
                  elif h > 235 and h < 275:
                          lilac += 1
                  elif h > 274 and h < 350:
                          pink += 1

        except ValueError as err:
          print(err)
        except:
          print('Error: Cannot open image')

        finally:
          return {
                  'white': white,
                  'black': black,
                  'gray': gray,
                  'red': red,
                  'orange': orange,
                  'brown': brown,
                  'yellow': yellow,
                  'green': green,
                  'turquoise': turquoise,
                  'blue': blue,
                  'lilac': lilac,
                  'pink': pink
                  }




#with open('./output/test.jl', 'r') as jsonfile:
#    data = json.load(jsonfile)

data = []
with jsonlines.open('./output/test.jl') as jsonfile:
    for obj in jsonfile:
        data.append(obj)

for itemset in data:
    for fileinfo in itemset.get('files'):
        print (color_tag_image('./output/' + fileinfo.get('path')))
        fileinfo['color_values'] = color_tag_image('./output/' + fileinfo.get('path'))

with open('./webhost/www/test.json', 'w') as jsonfile:
    json.dump(data, jsonfile)

