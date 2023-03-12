from inventory_report.inventory.product import Product


def test_relatorio_produto():
    produto = Product(
        id=1,
        nome_da_empresa="Matheus",
        nome_do_produto="resiliencia",
        data_de_fabricacao="25/07/1996",
        data_de_validade="25/07/2076",
        numero_de_serie="10",
        instrucoes_de_armazenamento="deixar ao ar livre"
    )

    assert (produto.__repr__()) == (
        "O produto resiliencia"
        " fabricado em 25/07/1996"
        " por Matheus com validade"
        " até 25/07/2076"
        " precisa ser armazenado deixar ao ar livre."
    )
