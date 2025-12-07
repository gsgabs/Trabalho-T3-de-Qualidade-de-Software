from sistema import Cliente, CalculadoraPedidoService


def executar_teste_manual(perfil, estado, valor_compra, esperado):
    service = CalculadoraPedidoService()
    print(f"ENTRADA: Perfil={perfil}, Estado={estado}, Valor={valor_compra}")

    try:
        cliente = Cliente(perfil, estado)
        resultado = service.processar_pedido(cliente, valor_compra)

        esperado = float(esperado)

        print(f"ESPERADO: {esperado}")
        print(f"OBTIDO:   {resultado}")

        if resultado == esperado:
            print("STATUS: ✅ APROVADO")
        else:
            print("STATUS: ❌ REPROVADO")

    except ValueError:
            print("STATUS: ✅ APROVADO (Erro esperado ocorreu)")


    print("-" * 30)
    print()




while 1:
    perfil_level = int(input("Perfil do usuário: "))
    estado = input("Estado do Usuario: ")
    valor_livo = float(input("Valor da compra: "))
    valor_processado = input("Valor esperado após descontos e frete: ")
    print()

    executar_teste_manual(perfil_level, estado, valor_livo, valor_processado)

    print()
    print()
