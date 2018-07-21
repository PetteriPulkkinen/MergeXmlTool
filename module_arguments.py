import argparse


def get_arguments():
    '''
    Returns:
    '''
    parser = argparse.ArgumentParser(
        description='Tool for merging xml files')
    parser.add_argument('-p', '--parent',
                        default='parent.xml',
                        help='File used as parent in the merge process')
    parser.add_argument('-c', '--child',
                        default='child.xml',
                        help='File used as child in the merge process')
    parser.add_argument('-f', '--folder',
                        action='store_true',
                        help='Child object is handled as folder')
    return parser.parse_args()
