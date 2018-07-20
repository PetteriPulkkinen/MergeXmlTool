import argparse


def get_arguments():
    '''
    Returns:
    '''
    parser = argparse.ArgumentParser(
        description='Tool for merging xml files')
    parser.add_argument(dest='parent', help='This is the help')
    return parser.parse_args()
