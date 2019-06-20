from xml.etree import ElementTree as ET
import re


class ElementTreeHelper():
    def __init__(self, xml_file_name):
        xml_file = open(xml_file_name, "rb")
        self.__parse_xml_declaration(xml_file)
        self.element_tree = ET.parse(xml_file)
        xml_file.seek(0)
        root_tag_namespace = self.__root_tag_namespace(self.element_tree)
        self.namespace = None
        if root_tag_namespace is not None:
            self.namespace = '{' + root_tag_namespace + '}'
            ET.register_namespace('', root_tag_namespace)
            self.element_tree = ET.parse(xml_file)

    def find(self, xpath_query):
        return self.element_tree.find(xpath_query)

    def write(self, xml_file_name):
        xml_file = open(xml_file_name, "wb")
        if self.xml_declaration_line is not None:
            xml_file.write(self.xml_declaration_line + '\n')

        return self.element_tree.write(xml_file)

    def __parse_xml_declaration(self, xml_file):
        first_line = xml_file.readline().strip()
        if first_line.startswith('<?xml') and first_line.endswith('?>'):
            self.xml_declaration_line = first_line
        else:
            self.xml_declaration_line = None
        xml_file.seek(0)

    def __root_tag_namespace(self, element_tree):
        namespace_search = re.search('^{(\S+)}', element_tree.getroot().tag)
        if namespace_search is not None:
            return namespace_search.group(1)
        else:
            return None


def __main():
    el_tree_hlp = ElementTreeHelper('myxml.xml')

    for elem in el_tree_hlp.element_tree.iter():
        if elem.text and 'COPY' in elem.text:
            elem.text=None

    el_tree_hlp.write('myxml1.xml')

if __name__ == '__main__':
    __main()