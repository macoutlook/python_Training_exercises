import os
import matplotlib.pyplot as plt


# def get_folder_size(folder_path = folder_path_main):
#     global folder_path_main
#     from functools import partial
#     if folder_path_main == None:
#         folder_path_main = folder_path
#
#     #partial let to execute function with one word, basetwo = partial(int, base=2) basetwo('101010')
#     prepend = partial(os.path.join, folder_path)
#     # return sum([(os.path.getsize(f) if os.path.isfile(f) else get_folder_size(folder_path)) for f in map(prepend, os.listdir(get_folder_size(folder_path)))])
#     mapped = map(prepend, os.listdir(get_folder_size()))
#     sum = 0
#     for f in mapped:
#         if os.path.isfile(f):
#             size = os.path.getsize(f)
#             sum += size
#         else:
#             get_folder_size()
#     return sum

# def get_folder_size(folder):
#     total_size = os.path.getsize(folder)
#     for item in os.listdir(folder):
#         itempath = os.path.join(folder, item)
#         if os.path.isfile(itempath):
#             total_size += os.path.getsize(itempath)
#         elif os.path.isdir(itempath):
#             total_size += get_folder_size(itempath)
#     return total_size


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
    print compr_level_lst
    # converting volume of dir in bytes into MB
    folder_size = float(folder_size) / (1024*1024)
    list_for_dir_size = [folder_size]
    for ind, compr_lvl in enumerate(compr_level_lst):
        plt.plot([folder_size], [compr_lvl], 'ro', label = compress_name_level_list[ind], color = list_of_colours[ind])
    max_folder_size = folder_size + 2
    min_folder_size = folder_size - 2
    min_compr_lvl = min(compr_level_lst) - 0.01
    max_compr_lvl = max(compr_level_lst) + 0.01
    plt.ylabel('Compression level')
    plt.xlabel('Size of uncompressed dir')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=1, borderaxespad=0.)
    # min and max values for both dimensions
    plt.axis([min_folder_size, max_folder_size, min_compr_lvl, max_compr_lvl])
    plt.show()
