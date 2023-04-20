try:
    value = int(input('Entre com um número: '))
    print('0 valor:', value, 'dividido por um é: ', 1/value)
except ValueError:
    print('Erro. Verifique o valor fornecido.')
except ZeroDivisionError:
    print('Não é possível fazer divisão por zero.')
except:
    print('Algo errado aconteceu')
    