from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
# from inventory_report.data.inventory.json import *

data = [
    {
        "id": "7",
        "nome_do_produto": "Spironolactone",
        "nome_da_empresa": "REMEDYREPACK",
        "data_de_fabricacao": "2021-07-17",
        "data_de_validade": "2023-11-18",
        "numero_de_serie": "SM28 B981 5118 903W JY0C 5KVO 3QD",
        "instrucoes_de_armazenamento": "instrucao 7"
  }
]


def test_decorar_relatorio():
    objeto_simples = ColoredReport(SimpleReport)
    rel = objeto_simples.generate(data)

    assert rel == (
        "\033[32mData de fabricação mais antiga:\033[0m"
        " \033[36m2021-07-17\033[0m\n"
        "\033[32mData de validade mais próxima:\033[0m"
        " \033[36m2023-11-18\033[0m\n"
        "\033[32mEmpresa com mais produtos:\033[0m"
        " \033[31mREMEDYREPACK\033[0m"
    )
    assert "\033[32mData de fabricação mais antiga:\033[0m" in rel
    assert "\033[32mData de validade mais próxima:\033[0m" in rel
    assert "\033[32mEmpresa com mais produtos:\033[0m" in rel
    assert "\033[36m2021-07-17\033[0m" in rel
    assert "\033[36m2023-11-18\33[0m" in rel
    assert "\033[31mREMEDYREPACK\033[0m" in rel
