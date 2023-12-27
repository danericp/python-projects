import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill


def convert_csv_to_xlsx(csv_file, xlsx_file, sheet_name, font_name, font_size, cell_background):
    try:
        # Read CSV file using pandas
        data = pd.read_csv(csv_file)

        # Create a new Workbook and select the active sheet
        wb = Workbook()
        ws = wb.active
        ws.title = sheet_name  # Set sheet name

        # Set font style
        font = Font(name=font_name, size=font_size)
        for cell in ws["1:1"]:  # Apply font to the header row
            cell.font = font

        # Set cell background color
        if cell_background:
            fill = PatternFill(start_color=cell_background, end_color=cell_background, fill_type="solid")
            for row in ws.iter_rows(min_row=2, min_col=1, max_col=len(data.columns), max_row=len(data) + 1):
                for cell in row:
                    cell.fill = fill

        # Write the data to the worksheet
        for r_idx, row in enumerate(data.iterrows(), start=1):
            for c_idx, value in enumerate(row[1], start=1):
                ws.cell(row=r_idx, column=c_idx, value=value)

        # Save the workbook as XLSX file
        wb.save(xlsx_file)

        print(f"CSV file '{csv_file}' successfully converted to XLSX file '{xlsx_file}'")
    except Exception as e:
        print("An error occurred:", e)
