from PIL import Image
from pylab import *


img = Image.open('data/paths0.png')
imshow(img)


def draw_lines(*args,multipul = True):
    
    for i,tuple in enumerate(args):
        if multipul or i==0:
            plt.figure(i+1)
            fig, ax = plt.subplots()
            ax.imshow(img, extent=[0, 400, 0, 300])
        plot(*tuple, '-', 'color',rand(1,3))
    show()

draw_lines(([30,100,150,200,250],[30,40,60,90,150]),([350,300],[30,50]),([400,300],[30,100]),([250,150],[30,50]),([100,250],[30,50]), multipul=True)




