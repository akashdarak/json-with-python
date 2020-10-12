import sys
import xml.etree.ElementTree as etree

def get_attr_number(root):
    # your code goes here
    num = 0
    for child in root.iter():
        #print child.attrib
        num += len(child.attrib)
    return num
     

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print get_attr_number(root)
