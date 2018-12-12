import pandas as pd
from pylab import *
from plot_graph import draw_lines
import datetime

df = pd.read_pickle('data/paths.pkl.xz')
objs = df.groupby(["filename","obj"]).size().sort_values(ascending=False)
df_by_obj = df.set_index(['filename', 'obj']).sort_index()
var_in_class = df_by_obj
img = imread("data/paths0.png")


def plot_objs(data):
    top10 = data.groupby(["filename","obj"]).size().sort_values(ascending=False).head(10)
    df_by_obj = df.set_index(['filename', 'obj']).sort_index()
    main_info = []
    for t in top10.index:
        oo = df_by_obj.loc[t]
        main_info.append((oo.x,oo.y))
    draw_lines(main_info,multipul = False)

def filter_by_date(date):
    global var_in_class
    var_in_class = var_in_class[var_in_class.time.dt.date == date]
    #return specific_date

# d = datetime.date(2017, 8, 20)
# filter_by_date(d)

def filter_by_time(time1,time2):
    global var_in_class
    var_in_claas = var_in_class[var_in_class.time.dt.time.between(time1, time2)]
    #return specific_time

# time1 = datetime.time(1, 24, 9)
# time2 = datetime.time(1, 27, 9)
# filter_by_time(time1,time2)

def filter_by_area(t_l, b_r):
    global var_in_class
    var_in_claas = var_in_class[(var_in_class.x.between(t_l[0], b_r[0])) & (var_in_class.y.between(t_l[1], b_r[1]))]
    #return table[['x', 'y']]

# t_l = (0, 0)
# b_r = (600, 300)
# filter_by_area(t_l,b_r)


def filter_by_definitioned_area(num_square, num_of_squares):
    y=img.shape[0]
    x=img.shape[1]
    x_size=x//num_of_squares[0]
    y_size=y//num_of_squares[1]
    p1=(x_size*num_square[0],y_size*(num_square[1]))
    p2=(x_size*(num_square[0]+1),y_size*(num_square[1]+1))
    filter_by_area(p1,p2)

# num_square=(7,9)
# num_of_squares=(10,10)
# filter_by_definitioned_area(num_square, num_of_squares)

def filter(*args):
    global var_in_class
    #args is a tuples of name of filter, and his args in tuple
    #call the suit filter
    #get the data
    for filter in args:
        filter[0](*filter[1])
    plot_objs(var_in_class[['x','y']])
    var_in_class = df_by_obj



tuple1 = (filter_by_area,((0, 0),(100, 100)))
tuple2 = (filter_by_definitioned_area,((7,9),(10,10)))
filter(tuple1,tuple2)
