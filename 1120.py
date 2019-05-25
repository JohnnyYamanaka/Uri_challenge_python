def calcula_valor_registrado():


    while True:
        dig_falhaado, valor_negociado = list(input().split(" "))
        if dig_falhaado == '0' and valor_negociado == '0':
            return False

        else:
            valor_negociado_digit = list(valor_negociado)

            while dig_falhaado in valor_negociado_digit:
                valor_negociado_digit.remove(dig_falhaado)

            if not valor_negociado_digit:
                valor_negociado_digit.append("0")

            novo_valor = int("".join(valor_negociado_digit))
            print(novo_valor)


def main():
    calcula_valor_registrado()


if __name__ == '__main__':
    main()