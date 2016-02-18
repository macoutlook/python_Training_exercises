import apachelog


def get_downloads_count(log, fpath):
    '''
    Count number of downloads of file `fpath` in the given log sequence
    '''
    # !!!Your code here!!!
    counter = 0
    for one_dict in log:
        if one_dict['request'] == fpath:
            counter += 1
    return counter

def main():
    '''Main function'''
    # lines = apachelog.lines_from_dir('access-log*', 'www')
    # log = apachelog.apache_log(lines)
    list_with_dicts = apachelog.lines_from_dir('access-log', 'www')
    #print list_with_dicts[0]
    # get_downloads_count()
    print 'Total: %d' % get_downloads_count(list_with_dicts, '/ply/ply-2.3.tar.gz')

if __name__ == '__main__':
    main()
