import config 
import argparse

from utils.data_reader import read_data,read_data_mock


def main(path:str):
    read_data_mock(config.connection_string,config.blob_name,config.container_name,path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path') 
    args = parser.parse_args()
    main(path=args.path)