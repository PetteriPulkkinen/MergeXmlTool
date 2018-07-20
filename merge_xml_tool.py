import xml.etree.ElementTree as ET
import os

place_holder = r'@PLACE_HOLDER'


def _make_tree(parent_file, child_file):
    parent_xml = os.path.abspath(parent_file)
    parent_tree = ET.parse(parent_xml)
    child_xml = os.path.abspath(child_file)
    child_tree = ET.parse(child_xml)
    for element in parent_tree.iter():
        for key, value in element.items():
            if value == place_holder:
                f = child_tree.find('.//{}'.format(element.tag))
                element.set(key, f.get(key))
        if element.text == place_holder:
            f = child_tree.find('.//{}'.format(element.tag))
            element.text = f.text
    parent_tree.write(child_file)


def _get_config_files(directory):
    config = 'config.xml'
    for dirpath, _, filenames in os.walk(directory):
        for file in filenames:
            if config == file:
                yield os.path.abspath(os.path.join(dirpath, file))


if __name__ == '__main__':
    parent_file = 'parent.xml'
    for child_file in _get_config_files(os.path.abspath('Jenkins')):
        _make_tree(parent_file, child_file)
