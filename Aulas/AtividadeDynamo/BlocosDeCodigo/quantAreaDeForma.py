comprimento_viga = IN[0]
base_viga = IN[1]
altura_viga = IN[2]

comprimento_pilar = IN[3]
lado_pilar = IN[4]

quantidade_de_pilares = IN[5]
quantidade_de_vigas = IN[6]

material_pilares = IN[7]
material_viga = IN[8]

#área de

#Calculo de forma das vigas
if material_viga == 1:
    forma_viga = ((base_viga + (altura_viga * 2)) * comprimento_viga) * quantidade_de_vigas
else:
    forma_viga = 0

#calculo de forma dos pilares
if material_pilares == 1:
    forma_pilar = ((lado_pilar * 4) * comprimento_pilar) * quantidade_de_pilares
else:
    forma_pilar = 0

#quantidade total de formas
total_forma = forma_pilar + forma_viga






OUT = total_forma