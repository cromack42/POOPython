def get_joelho(*pedidos):
    yield [f'{pedido} joelho(s)' for pedido in pedidos]
    
    salgado = next(get_joelho(4,6,8))
    print(salgado)
    
    