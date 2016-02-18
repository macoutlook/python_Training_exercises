import apachelog


def get_404(log):
    '''
    Find the set of all requests with status 404 in the given `log` sequence
    '''
    # !!!Your code here!!!
    list = []
    for one_dict in log:
        if str(one_dict['status']) == '404':
            list.append(one_dict['request'])
    return list


def main():
    '''Main function'''
    list_with_dict = apachelog.lines_from_dir('access-log', 'www')
    #log = apachelog.apache_log(lines)
    for r in sorted(get_404(list_with_dict)):
        print r


if __name__ == '__main__':
    main()
