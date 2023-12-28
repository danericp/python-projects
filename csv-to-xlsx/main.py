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


if __name__ == "__main__":
    obj_options = get_arguments()
    path_csv = obj_options.csv
    path_json = obj_options.config
    excel.do_check_file_exists(path_json)
    excel.convert_csv_to_xlsx(path_json, path_csv)
