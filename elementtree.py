import sys

#Most common APIs are available on the ElementTree class

#from elementtree.ElementTree import ElementTree
import xml.etree.ElementTree as ET
tree = ET.parse("C:\\Users\\nickens\\Downloads\\XML311SCHEMA\\XML311SCHEMA.XML")
root = tree.getroot()
#write out XML from the ElementTree instance

tree.write("C:\\Users\\nickens\\Downloads\\XML311SCHEMA\\XML311SCHEMAROOT.XML")
