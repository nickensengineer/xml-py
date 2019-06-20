import xml.etree.ElementTree as ET
context = ET.iterparse('file.xml', events=('end', ))
for event, elem in context:
    if elem.tag == 'row':
        title = elem.find('NAME').text
        filename = format(title + ".xml")
        with open(filename, 'wb') as f:
            f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
            f.write(ET.tostring(elem))