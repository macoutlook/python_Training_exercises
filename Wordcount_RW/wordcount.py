#!/usr/bin/python
import sys
from operator import itemgetter


def print_count(fname):
    '''
    Prints one per line '<word> <count>' sorted by word for the given file
    '''
    dict_with_words = get_dict_from_file(fname)

    for key, value in dict_with_words.iteritems():
        print key, "liczba wystapien:", value


def print_top(fname):
    '''
    Prints the top count listing for the given file
    '''
    dict_with_words = get_dict_from_file(fname)
    total_count = 20
    top_list = list
    top_tuple = tuple
    for key, value in sorted(dict_with_words.items(), key=itemgetter(1), reverse=True):
        if total_count > 0:
            print key, "Liczba wystapien top:", value
            total_count -= 1


def get_dict_from_file(fname):
    dict_with_words = {}
    with open(fname) as f:
        for line in f:
            tab_with_words = line.split()
            for word in tab_with_words:
                if word.lower() in dict_with_words:
                    dict_with_words[word.lower()] += 1
                else:
                    dict_with_words[word.lower()] = 1
    return dict_with_words


def main():
    if len(sys.argv) != 3:
        print 'Usage: ./wordcount.py {--count | --top} <file name>'
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_count(filename)
    elif option == '--top':
        print_top(filename)
    else:
        print 'unknown option: ' + option
        sys.exit(1)


if __name__ == '__main__':
    main()


