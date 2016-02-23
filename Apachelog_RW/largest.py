import apachelog


def get_largest(log):
    '''
    Find the largest data transfer in the given `log` sequence

    >>> get_largest([{'status': '200', 'bytes': '97238', 'host': '140.180.132.213', 'user': '-', 'proto': 'HTTP/1.1', 'referrer': '-', 'request': '/ply/ply.html', 'method': 'GET', 'datetime': '24/Feb/2008:00:08:59 -0600'}, {'status': '200', 'bytes': '4447', 'host': '75.54.118.139', 'user': '-', 'proto': 'HTTP/1.1', 'referrer': '-', 'request': '/', 'method': 'GET', 'datetime': '24/Feb/2008:00:15:40 -0600'}, {'status': '200', 'bytes': '60025', 'host': '75.54.118.139', 'user': '-', 'proto': 'HTTP/1.1', 'referrer': '-', 'request': '/images/Davetubes.jpg', 'method': 'GET', 'datetime': '24/Feb/2008:00:15:41 -0600'}])
    (97238, '/ply/ply.html')
    '''
    largest = (0, None)
    for one_dict in log:
        if str(one_dict['bytes']) != '-' and int(one_dict['bytes']) > largest[0]:
            largest = (int(one_dict['bytes']), one_dict['request'])

    return largest

def main():
    '''Main function'''
    lines = apachelog.lines_from_dir('access-log*', 'www')
    list_with_dict = apachelog.apache_log(lines)
    print '%d %s' % get_largest(list_with_dict)


if __name__ == '__main__':
    # doctest in get_largest method is implemented
    import doctest
    doctest.testmod()
    main()
