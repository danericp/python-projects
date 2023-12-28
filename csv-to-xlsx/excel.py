import json
import os
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill


def do_check_file_exists(path_file):
    if os.path.exists(path_file):
        print(f"The file '{path_file}' exists.")
    else:
        print(f"The file '{path_file}' does not exist.")
        exit()


def convert_csv_to_xlsx(file_json, file_csv):
    try:
        with open(file_json, 'r') as file:
            data_json = json.load(file)
        # Read CSV file using pandas
        data = pd.read_csv(file_csv)

        # Create a new Workbook and select the active sheet
        wb = Workbook()
        ws = wb.active
        ws.title = data_json["metadata"]["sheet-name"]  # Set sheet name

        # Set font style
        fill_header = PatternFill(
            start_color=data_json["header"]["background-color"],
            end_color=data_json["header"]["background-color"],
            fill_type="solid",
        )
        fill_data = PatternFill(
            start_color=data_json["data"]["background-color"],
            end_color=data_json["data"]["background-color"],
            fill_type="solid",
        )
        font_header = Font(
            bold=data_json["header"]["font-bold"],
            color=data_json["header"]["font-color"],
            italic=data_json["header"]["font-italic"],
            name=data_json["header"]["font-name"],
            size=data_json["header"]["font-size"]
        )
        font_data = Font(
            bold=data_json["data"]["font-bold"],
            color=data_json["data"]["font-color"],
            italic=data_json["data"]["font-italic"],
            name=data_json["data"]["font-name"],
            size=data_json["data"]["font-size"]
        )

        for cell in ws["1"]:  # Apply font to the header row
            cell.fill = fill_header
            cell.font = font_header

        # Set cell background color
        for row in ws.iter_rows(min_row=2, min_col=1, max_col=len(data.columns), max_row=len(data) + 1):
            for cell in row:
                cell.fill = fill_data
                cell.font = font_data

        # Write the data to the worksheet
        for r_idx, row in enumerate(data.iterrows(), start=1):
            for c_idx, value in enumerate(row[1], start=1):
                ws.cell(row=r_idx, column=c_idx, value=value)

        # Save the workbook as XLSX file
        wb.save(file_csv.split('.')[0] + ".xlsx")

        print(f"CSV file '{file_csv}' successfully converted to XLSX file '{file_csv.split('.')[0] + ".xlsx"}'")
    except Exception as e:
        print("An error occurred:", e)
