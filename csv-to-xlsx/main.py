import argparse
import excel


def get_arguments():
    obj_parser = argparse.ArgumentParser(
        prog='CSV to XLSX',
        description='Convert your CSV file into a customized XLSX.',
        epilog="Tested with Python 3.8"
    )
    obj_parser.add_argument("-f", "--file", dest="csv", help="CSV file", required=True)
    obj_parser.add_argument("-c", "--config", dest="config", help="JSON Configuration file", required=False)
    options = obj_parser.parse_args()
    return options


obj_options = get_arguments()
str_csv = obj_options.csv
str_json = obj_options.config

print(excel.test_function())
