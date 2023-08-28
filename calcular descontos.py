"""
Calcular descontos no salário:
Informe o salário,desconto inss,horas extras e salário líquido

"""
#Valores de Entrada
print('#' * 40)

salario = int(input('Informe seu salário R$:\n'))
extras = int(input('Quantas horas extras alcançadas?\n'))

print( '#' * 40)
#Base de cáĺculos
valor_hora = float(salario / 220)

valor_extras = float(extras * (valor_hora * 2 ))

inss = float(salario * (11 / 100))

fgts = float(salario * (9 /100))

sal_des = float(salario + valor_extras - fgts - inss)

#Condições sobre cálculo de imposto de renda
if sal_des < 1903:
    ir = sal_des - sal_des
    print('Não atingiu o minimo de IR\n')
    
elif sal_des > 1904 and sal_des< 2826:
    ir = sal_des * 7.5 / 100
    print('Atingiu o valor de 7,5% de IR\n')

elif sal_des > 2827 and sal_des< 3751:
    ir = sal_des * 15 / 100
    print('Atingiu 15% de IR\n')

elif sal_des > 3752 and sal_des < 4664:
    ir = sal_des * 22.5 / 100
    print('Atingiu 22,5% de IR\n')

elif sal_des > 4665:
    ir = sal_des * 27.5 / 100
    print('Atingiu 27,5 de IR\n')
else:
    print('Não especificado')

#Base de descontos
desconto_total = fgts + inss + ir
salario_liquido = sal_des - ir

#Espaçamentos para melhor vizualização
print('Desconto Inss foi de R$:{:.2f}\n'.format(inss))

print('Desconto de Fgts foi de R$:{:.2f}\n'.format(fgts))

print('Desconto de IR foi de R$:{:.2f}\n'.format(ir))

print('Total de descontos foi de: {:.2f}\n'.format(desconto_total))

print('Valor de horas Extras foi de R$:{:.2f}\n'.format(valor_extras))

print('Seu salário líquido é R$:{:.2f}\n'.format(salario_liquido))

print('Qualquer dúvida entrar em contato com o Rh. Obrigado')

