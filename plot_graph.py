from PIL import Image
from pylab import *

img = Image.open('data/paths0.png')
imshow(img)


def draw_lines(*args,multipul = True):

    if list == []:
        fig, ax = plt.subplots()
        ax.imshow(img)
        return

    for i,tuple in enumerate(args):
        if multipul or i==0:
            plt.figure(i+1)
            fig, ax = plt.subplots()
            ax.imshow(img)
        plot(*tuple, '-', 'color',rand(1,3))
    show()





