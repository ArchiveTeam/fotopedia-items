'''Convert discovery items to tracker items.

Use Python 3.
'''
import argparse
import glob
import itertools
import urllib.parse
import gzip


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('directory')
    
    args = arg_parser.parse_args()
    filenames = itertools.chain(
        glob.iglob(args.directory + '/*.gz'),
        glob.iglob(args.directory + '/*/*.gz'),
    )

    for filename in filenames:
        with gzip.GzipFile(filename, mode='rb') as in_file:
            for line in in_file:
                class_, id_ = line.decode('utf8').strip().split('|', 1)
                
                if class_ == 'Album':
                    if id_.startswith('fotopedia'):
                        locale, name = id_.split('-', 2)[1:]
                        name = urllib.parse.quote(name, encoding='utf8', safe='/!$&()*+,:;=@[]~\'')
                        print('wiki:{0}:{1}'.format(locale, name))
                    else:
                        print('album:{0}'.format(id_))
                elif class_ == 'MUser':
                    print('user:{0}'.format(id_))
                elif class_ == 'Story':
                    print('story:{0}'.format(id_))
                elif class_ == 'Picture':
                    print('photo:{0}'.format(id_))
                else:
                    raise Exception('Unknown type {0} {1}'.format(class_, id_))
    
    
if __name__ == '__main__':
    main()
