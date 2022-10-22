area_de_forma = IN[0]
volume_de_concreto = IN[1]
volume_de_madeira = IN[2]

custo_forma = IN[3]
custo_concreto = IN[4]
custo_madeira = IN[5]

#calculo do custo total
custo_total = (area_de_forma * custo_forma) + (volume_de_concreto * custo_concreto) + (custo_madeira * volume_de_madeira)


#Atribuição a variável de saída
OUT = custo_total