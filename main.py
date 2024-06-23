from bus_transportation import BusTransportFactory
from  metro_transportation import MetroTransportationFactory

if __name__ == '__main__':
    print("------------------ Transportes OPPORTUNITY -------------------")
    print("Selecione o tipo de transporte")
    print("1 - Ônibus")
    print("2 - Metrô")
    opcao = int(input("Insira uma opção: "))

    if opcao == 1:
        fabrica = BusTransportFactory.criar_fabrica()
        transporte = fabrica.criar_transporte(50, "Dinheiro", "Rio de Janeiro", "Volta Redonda")
    elif opcao == 2:
        fabrica = MetroTransportationFactory.criar_fabrica()
        transporte = fabrica.criar_transporte(200, "Bilhete Único", "Rio de Janeiro", "Niterói")
    else:
        print("Opção Inválida")


    transporte.rota()
    transporte.tarifa()
    transporte.capacidade()
    transporte.embarcar(12)
    transporte.capacidade_atual()
    transporte.desembarcar(10)
    transporte.capacidade_atual()