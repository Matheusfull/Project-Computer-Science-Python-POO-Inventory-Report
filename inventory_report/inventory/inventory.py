import csv
import json
from pathlib import Path
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(caminho, tipo):
        extensao = Path(caminho).suffix
        info = None
        if extensao == ".csv":
            with open(caminho, "r") as file_csv:
                info = list(csv.DictReader(file_csv))
        elif extensao == ".json":
            with open(caminho, "r") as file_json:
                info = json.load(file_json)

        if tipo == "simples":
            return SimpleReport().generate(info)
        else:
            return CompleteReport().generate(info)
