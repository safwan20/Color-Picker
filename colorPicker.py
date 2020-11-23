import cv2
import numpy as np
from collections import Counter

def prepareIntensities(filename) :
  '''
    Returns : the tuples having count of colors intensities, height and width of an image

    Args : filename
  
  '''

  img = cv2.imread(filename)
  width, height, channel = img.shape

  intensities = {}
  for y in range(0, height):
    for x in range(0, width):
      RGB = (img[x, y, 2], img[x, y, 1], img[x, y, 0])
      if RGB in intensities:
        intensities[RGB] += 1
      else:
        intensities[RGB] = 1
        
  return (intensities, width, height)

def topMostIntensity(intensities) :
  '''
    Returns : the 20 topmost color intensities of the image 

    Args : intensities

  '''

  number_counter = Counter(intensities).most_common(20)

  return number_counter


def average(number_counter) :
  '''
      Returns : the average color tuple of (red, green , blue). 

      Args : number_counter
  '''

  red = 0
  green = 0
  blue = 0
  sample = 10

  for top in range(0, sample):
    red += number_counter[top][0][0]
    green += number_counter[top][0][1]
    blue += number_counter[top][0][2]

  average_red = int(red / sample)
  average_green = int(green / sample)
  average_blue = int(blue / sample)

  average_colors = (average_red, average_green, average_blue)

  return average_colors

def rgb2hex(r,g,b):
  '''
    Return : the hexcode.

    Args : the RBG value of the dominant color.
    
  '''
  return "#{:02x}{:02x}{:02x}".format(r,g,b)



def pickColor(filename) :
  '''
    Returns : the response having the logo and dominant color.

    Args : filename

  '''

  color_picker = {}

  intensities, width, height = prepareIntensities(filename)
  number_counter = topMostIntensity(intensities)
  total_pixels = width * height

  percentage_of_first = float(number_counter[0][1])/total_pixels

  if percentage_of_first > 0.5:
    color_picker['logo_border'] = rgb2hex(number_counter[0][0][0], number_counter[0][0][1], number_counter[0][0][2])
    color_picker['dominant_color'] = rgb2hex(number_counter[0][0][0], number_counter[0][0][1], number_counter[0][0][2])

  else:
    average_colors = average(number_counter)
    color_picker['logo_border'] = rgb2hex(average_colors[0], average_colors[1], average_colors[2])
    color_picker['dominant_color'] = rgb2hex(number_counter[0][0][0], number_counter[0][0][1], number_counter[0][0][2])

  return color_picker