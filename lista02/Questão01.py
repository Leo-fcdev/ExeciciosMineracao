"""
Dessa vez, lhe iludiram e disseram que iam pagar para você fazer um programa, mas no fundo você sabe que não vai receber. Você foi contratado para criar um programa de promoção do dia do consumidor. Basicamente, você vai ler o total da compra de um consumidor e aplicar o desconto conforme abaixo:

	total compra	desconto
	< 50,00		5%
	< 100,00		10%
< 200,00		20%
< 500,00		25%
>= 500, 00		30%

Por fim, você deve imprimir o valor total da compra após o desconto.  

"""
conta = float(input("Qual é o valor da conta?"))
desconto:float = 0 

if (conta <= 0):
    print("Valor inválido, por favor inserir valores positivos")
elif (conta < 50):
    desconto = 0.05
elif (conta < 100):
    desconto = 0.10
elif (conta < 200):
    desconto = 0.20
elif (conta < 500):
    desconto = 0.25
else:
    desconto = 0.30

valor_com_desconto = conta  - (conta * desconto) 

print(f"O valor da conta com o desconto é de: R$ {valor_com_desconto:.2f}")
    

    