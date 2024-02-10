import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math as m
def unpack(file_path):

    x = []
    x_title = ""
    y = []
    y_title = ""

    with open(file_path, 'r', encoding='iso-8859-1') as file:
        for line in file:
            # Process each line here
            line = line.strip()
            if line == "":
                continue
            line = line.split()
            if ord(line[0][-1]) > 57:
                x_title += line[0] + " "
                y_title += line[1] + " "
                continue
            line[0] = line[0].replace(",", ".")
            line[1] = line[1].replace(",", ".")
            x.append(float(line[0]))
            y.append(float(line[1]))
    
    return x, x_title, y, y_title
