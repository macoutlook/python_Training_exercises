import apachelog


def get_downloads_count(log, fpath):
    '''
    Count number of downloads of file `fpath` in the given log sequence

    >>> get_downloads_count([{'status': '200', 'bytes': '97238', 'host': '140.180.132.213', 'user': '-', 'proto': 'HTTP/1.1', 'referrer': '-', 'request':'/ply/ply-2.3.tar.gz', 'method': 'GET', 'datetime': '24/Feb/2008:00:08:59 -0600'}, {'status': '200', 'bytes': '4447', 'host': '75.54.118.139', 'user': '-', 'proto': 'HTTP/1.1', 'referrer': '-', 'request': '/', 'method': 'GET', 'datetime': '24/Feb/2008:00:15:40 -0600'}, {'status': '200', 'bytes': '60025', 'host': '75.54.118.139', 'user': '-', 'proto': 'HTTP/1.1', 'referrer': '-', 'request': '/images/Davetubes.jpg', 'method': 'GET', 'datetime': '24/Feb/2008:00:15:41 -0600'}], '/ply/ply-2.3.tar.gz')
    1
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
    import doctest
    doctest.testmod()
    main()
