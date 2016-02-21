import apachelog


def get_downloads_count(log, fpath):
    '''
    Count number of downloads of file `fpath` in the given log sequence
    '''
    counter = 0
    for one_dict in log:
        if one_dict['request'] == fpath:
            counter += 1
    return counter

def main():
    '''Main function'''
    lines = apachelog.lines_from_dir('access-log*', 'www')
    list_with_dicts = apachelog.apache_log(lines)
    print 'Total: %d' % get_downloads_count(list_with_dicts, '/ply/ply-2.3.tar.gz')

if __name__ == '__main__':
    main()
