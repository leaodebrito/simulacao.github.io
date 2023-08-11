area_de_forma = IN[0]
volume_de_concreto = IN[1]
peso_de_aco = IN[2]
volume_de_madeira = IN[3]

custo_forma = IN[4]
custo_concreto = IN[5]
custo_madeira = IN[6]
custo_aco = IN[7]

#calculo do custo total
custo_total = (area_de_forma * custo_forma) + (volume_de_concreto * custo_concreto) + (custo_madeira * volume_de_madeira) + (peso_de_aco * custo_aco)


#Atribuição a variável de saída
OUT = custo_total