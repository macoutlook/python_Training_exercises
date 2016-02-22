import sys
sys.path.insert(0, '../lib')

# Wrapper for ElementTree
# api: http://docs.python.org/2/library/xml.etree.elementtree.html
from CurrentSet_RW.lib import ElementSoup as ES


def parse(fobj):
    '''
    Parse HTML file and extract targets data
    '''
    main_list = []
    root = ES.parse(fobj)
    target_name_list = []
    target_ip_list = []
    hw_type_list = []
    tbllst = root.findall('.//table')

    for elem in tbllst[0][0]:  # iterating over table/tbody/tr elements
        if elem.tag == 'tr':
            target_name_list.append(elem[0].text)
            target_ip_list.append(elem[2].text)
            hw_type_list.append(elem[9].text)

    main_list.append(target_name_list);
    main_list.append(target_ip_list);
    main_list.append(hw_type_list);

    return main_list


def report(targets):
    '''
    Generate targets report to standard output in the form:
    <HW type>

    <Target name> <Target IP>
    <Target name> <Target IP>
    ...
    <Target name> <Target IP>

    <HW type>

    <Target name> <Target IP>
    <Target name> <Target IP>
    ...
    <Target name> <Target IP>
    ...

    '''
    NONE_list = []
    BLADE_list = []
    HP_list = []
    MCP_list = []

    for ind, el in enumerate(targets[2]):
        if el == None:
            my_tuple =  (targets[0][ind], targets[1][ind])
            NONE_list.append(my_tuple)
        elif el == "BLADE":
            my_tuple =  (targets[0][ind], targets[1][ind])
            BLADE_list.append(my_tuple)
        elif el == "HP":
            my_tuple =  (targets[0][ind], targets[1][ind])
            HP_list.append(my_tuple)
        elif el == "MCP-18":
            my_tuple =  (targets[0][ind], targets[1][ind])
            MCP_list.append(my_tuple)

    main_dict = {"NONE":NONE_list, "BLADE":BLADE_list, "HP":HP_list, "MCP-18":MCP_list}

    for key, value in main_dict.iteritems():
        print "======== %s =======" % key
        for tup in value:
            print tup[0], tup[1]


def main():
    try:
        with open('C:\Users\lozoxmac\Documents\Repository_with_exercises\python_Training_exercises\CurrentSet_RW\currentsets.html') as f:
            report(parse(f))
    except IOError as e:
        print e

if __name__ == '__main__':
    main()
