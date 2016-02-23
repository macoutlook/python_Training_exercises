import apachelog


def get_404(log):
    '''
    Find the set of all requests with status 404 in the given `log` sequence

    >>> get_404([{'status': '404', 'bytes': '97238', 'host': '140.180.132.213', 'user': '-', 'proto': 'HTTP/1.1', 'referrer': '-', 'request': '/ply/ply.html', 'method': 'GET', 'datetime': '24/Feb/2008:00:08:59 -0600'}, {'status': '200', 'bytes': '4447', 'host': '75.54.118.139', 'user': '-', 'proto': 'HTTP/1.1', 'referrer': '-', 'request': '/', 'method': 'GET', 'datetime': '24/Feb/2008:00:15:40 -0600'}, {'status': '200', 'bytes': '60025', 'host': '75.54.118.139', 'user': '-', 'proto': 'HTTP/1.1', 'referrer': '-', 'request': '/images/Davetubes.jpg', 'method': 'GET', 'datetime': '24/Feb/2008:00:15:41 -0600'}])
    ['/ply/ply.html']

    '''

    return [x['request'] for x in log if x['status'] == '404']


def main():
    '''Main function'''
    lines = apachelog.lines_from_dir('access-log*', 'www')
    list_with_dict = apachelog.apache_log(lines)
    for r in sorted(set(get_404(list_with_dict))):
        print r


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
