from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(
        id=1,
        nome_da_empresa="Matheus",
        nome_do_produto="resiliencia",
        data_de_fabricacao="25/07/1996",
        data_de_validade="25/07/2076",
        numero_de_serie="10",
        instrucoes_de_armazenamento="deixar ao ar livre"
    )

    assert produto.id == 1
    assert produto.nome_da_empresa == "Matheus"
    assert produto.nome_do_produto == "resiliencia"
    assert produto.data_de_fabricacao == "25/07/1996"
    assert produto.data_de_validade == "25/07/2076"
    assert produto.numero_de_serie == "10"
    assert produto.instrucoes_de_armazenamento == "deixar ao ar livre"
