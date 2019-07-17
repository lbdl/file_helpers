import argparse
from  changes_helper import helper

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A helper program for change files in a project')
    
    parser.add_argument('base_file', nargs='?', default='change.base',
                        help=('The base change file to be used, generaly'
                        'this is going to be a previous versions change file'
                        'but you might optionally wish to use a blank.'))
   
    parser.add_argument('-t', nargs='?', default='md', 
                        help=('The file type of the change file to use'
                        'defaults to.md'))
    
    parser.add_argument('-js', type=Boolean, default=false, 
                        help=('When set to true will produce a json changes'
                              'file alongside the base markdown file'))
