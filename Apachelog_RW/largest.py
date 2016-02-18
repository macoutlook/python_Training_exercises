import apachelog


def get_largest(log):
    '''
    Find the largest data transfer in the given `log` sequence

    >>> get_largest([{'status': '200', 'bytes': '97238', 'host': '140.180.132.213', 'user': '-', 'proto': 'HTTP/1.1', 'referrer': '-', 'request': '/ply/ply.html', 'method': 'GET', 'datetime': '24/Feb/2008:00:08:59 -0600'}, {'status': '200', 'bytes': '4447', 'host': '75.54.118.139', 'user': '-', 'proto': 'HTTP/1.1', 'referrer': '-', 'request': '/', 'method': 'GET', 'datetime': '24/Feb/2008:00:15:40 -0600'}, {'status': '200', 'bytes': '60025', 'host': '75.54.118.139', 'user': '-', 'proto': 'HTTP/1.1', 'referrer': '-', 'request': '/images/Davetubes.jpg', 'method': 'GET', 'datetime': '24/Feb/2008:00:15:41 -0600'}])
    (97238, '/ply/ply.html')
    '''
    # !!!Your code here!!!
    biggest_bytes = 0
    request = ''
    for one_dict in log:
        if str(one_dict['bytes']) != '-':
            if int(one_dict['bytes']) > biggest_bytes:
                biggest_bytes = int(one_dict['bytes'])
                request = one_dict['request']
    returned_dict = {'bytes' : biggest_bytes, 'request' : request}
    # list = (biggest_bytes, request)

    return (biggest_bytes, request)

def main():
    '''Main function'''
    list_with_dict = apachelog.lines_from_dir('access-log', 'www')
    #log = apachelog.apache_log(list_with_dict)
    print '%d %s' % get_largest(list_with_dict)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    #main()
