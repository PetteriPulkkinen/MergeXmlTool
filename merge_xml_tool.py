import xml.etree.ElementTree as ET
import module_arguments
import os

place_holder = r'@PLACE_HOLDER'
config = r'config.xml'


def _get_parent(element, tree):
    return tree.find()


def _make_tree(parent_file, child_file):
    parent_xml = os.path.abspath(parent_file)
    parent_tree = ET.parse(parent_xml)
    child_xml = os.path.abspath(child_file)
    child_tree = ET.parse(child_xml)
    for element in parent_tree.iter():
        generator = filter(lambda _, v: v == place_holder, element.items())
        for k, _ in generator:
            f = child_tree.find('.//{}'.format(element.tag))
            element.set(k, f.get(k))
        if element.text == place_holder:
            f = child_tree.find('.//{}'.format(element.tag))
            element.text = f.text
    parent_tree.write(child_file)


def _get_config_files(directory):
    for dirpath, _, filenames in os.walk(directory):
        generator = filter(lambda file: file == config, filenames)
        for file in generator:
            yield os.path.abspath(os.path.join(dirpath, file))


if __name__ == '__main__':
    args = module_arguments.get_arguments()
    parent_xml = os.path.abspath(args.parent)
    if args.folder:
        child_folder = os.path.abspath(args.child)
        for child_xml in _get_config_files(child_folder):
            _make_tree(parent_xml, child_xml)
    else:
        child_xml = os.path.abspath(args.child)
        _make_tree(parent_xml, child_xml)
