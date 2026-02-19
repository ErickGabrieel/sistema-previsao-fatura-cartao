from datetime import datetime

def calcular_fatura(data_compra, fechamento, vencimento):
    data = datetime.strptime(data_compra, "%d/%m/%Y")

    if data.day <= fechamento:
        mes_fatura = data.month
        ano_fatura = data.year
    else:
        if data.month == 12:
            mes_fatura = 1
            ano_fatura = data.year + 1
        else:
            mes_fatura = data.month + 1
            ano_fatura = data.year

    data_vencimento = datetime(ano_fatura, mes_fatura, vencimento)

    return data_vencimento.strftime("%d/%m/%Y")

compra = input("Digite a data da compra (dd/mm/aaaa): ")
fechamento = int(input("Digite o dia de fechamento: "))
vencimento = int(input("Digite o dia de vencimento: "))

resultado = calcular_fatura(compra, fechamento, vencimento)

print("Essa compra vencerá em:", resultado)
