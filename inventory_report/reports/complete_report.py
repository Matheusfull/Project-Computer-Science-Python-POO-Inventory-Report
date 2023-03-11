from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list):
        dados_simples = SimpleReport.generate(list)
        lista_empresa = ''
        emresas_objetos = Counter(el["nome_da_empresa"] for el in list)
        for key, value in emresas_objetos.items():
            lista_empresa += f"- {key}: {value}\n"

        return (
            f"{dados_simples}\n"
            f"Produtos estocados por empresa:\n"
            f"{lista_empresa}"
        )

# método estátido recebe um parêmetro
# método de classe recebe dois parâmetro, sendo o primeiro cls
