from datetime import datetime
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(info):
        fabricacao_velha = min([el["data_de_fabricacao"] for el in info])

        # list_validade = [el["data_de_validade"] for el in list]
        validade_perto = min([
            el["data_de_validade"] for el in info
            if el["data_de_validade"] > datetime.now().isoformat()
        ])

        moda_empresa = Counter(
            el["nome_da_empresa"] for el in info
            ).most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {fabricacao_velha}\n"
            f"Data de validade mais próxima: {validade_perto}\n"
            f"Empresa com mais produtos: {moda_empresa}"
        )
