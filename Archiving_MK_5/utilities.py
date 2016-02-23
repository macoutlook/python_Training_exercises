import os
import numpy as np
import matplotlib.pyplot as plt


def get_folder_size(folder):
    """
    with os.walk dir is penetrated and size of dir is calculated
    :param folder:
    :return:
    """
    folder_size = 0
    for (path, dirs, files) in os.walk(folder):
      for file in files:
        filename = os.path.join(path, file)
        folder_size += os.path.getsize(filename)
    return folder_size


def calculate_compression(folder_size, zipped_folder_size):
    """
    Compressien level is calculated here
    :param folder_size:
    :param zipped_folder_size:
    :return:
    """
    return float(folder_size) / float(zipped_folder_size)


def create_plot(folder_size, compr_level_lst, compress_name_level_list):
    """
    creating a plot for folder size and compression levels
    :param folder_size:
    :param compr_level_lst:
    :return:
    """
    list_of_colours = ["red", "blue", "green", "yellow", "lime"]
    print "Calculated compression levels: %s" % compr_level_lst
    # converting volume of dir in bytes into MB
    folder_size = float(folder_size) / (1024*1024)
    for ind, compr_lvl in enumerate(compr_level_lst):
        plt.plot([folder_size], [compr_lvl], 'ro', label = compress_name_level_list[ind], color = list_of_colours[ind])

    min_folder_size, max_folder_size= evaluate_axis(folder_size, folder_size)
    min_compr_lvl, max_compr_lvl = evaluate_axis(min(compr_level_lst), max(compr_level_lst))
    plt.ylabel('Compression level')
    plt.xlabel('Size of uncompressed dir')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=1, borderaxespad=0.)
    # min and max values for both dimensions
    plt.axis([min_folder_size, max_folder_size, min_compr_lvl, max_compr_lvl])
    plt.show()


def create_bar_plot(folder_size, compr_level_lst, compress_name_level_list):
    N = len(compr_level_lst)
    folder_size = float(folder_size) / (1024*1024)
    folder_size = [folder_size]*3
    print tuple(folder_size)
    folder_size_bar = tuple(folder_size)
    ind = np.arange(N)  # the x locations for the groups
    width = 0.15       # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, folder_size_bar, width, color='r')

    compr_lvl_bar = tuple(compr_level_lst)
    rects2 = ax.bar(ind + width, compr_lvl_bar, width, color='y')

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Size')
    ax.set_title('Scores by zip method', y=1.05)
    ax.set_xticks(ind + width)
    ax.set_xticklabels(tuple(compress_name_level_list))

    ax.legend((rects1[0], rects2[0]), ('Size of folder', 'Size of compressed files'))

    autolabel(rects1, ax)
    autolabel(rects2, ax)

    plt.show()


def autolabel(rects, ax):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
            '%f' % float(height),
             ha='center', va='bottom')



def evaluate_axis(min, max):
    """
    Helper method which evaluates min and max values for axis
    :param min:
    :param max:
    :return:
    """
    int_size = int(min)
    len_of_value = len(str(int_size))
    mylist = list(xrange(len_of_value))
    x = 0.01

    for el in mylist:
        x = x * 10

    min = min - x
    max = max + x

    return min, max
