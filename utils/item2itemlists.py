'''Convert items list to split lists based on type.

Use Python 3.
'''
import argparse


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('input_file')
    arg_parser.add_argument('output_file_prefix')
    
    args = arg_parser.parse_args()
    
    files = {}

    for line in sorted(set(open(args.input_file, 'r'))):
        type_, value = line.strip().split(':', 1)
        
        if type_ not in files:
            files[type_] = open('{0}-{1}.txt'.format(args.output_file_prefix, type_), 'w')
        
        files[type_].write(line)
    
    for file_ in files.values():
        file_.close()


if __name__ == '__main__':
    main()
