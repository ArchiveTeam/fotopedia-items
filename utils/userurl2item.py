'''Convert user URLs to items.

Use Python 3.
'''
import urllib.parse
import argparse


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('input_file')
    
    args = arg_parser.parse_args()

    for line in sorted(set(open(args.input_file, 'r'))):
        parse_result = urllib.parse.urlsplit(line.strip())
        
        locale = parse_result.hostname.split('.', 1)[0]
        
        name = parse_result.path.split('/', 2)[2]
        
        print('user:{0}'.format(name))


if __name__ == '__main__':
    main()
