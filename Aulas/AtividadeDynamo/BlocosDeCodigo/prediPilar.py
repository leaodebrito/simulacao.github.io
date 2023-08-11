
import math

raio = IN[0]
lado = IN[1]
carga_do_piso = IN[2]
material = IN[3]


# Equação para definir o valor da apótema. Distancia ortogonal do centro ao lado do polígono
apotema = math.sqrt((raio ** 2) - ((lado ** 2)/4))

#pilares de concreto
area_de_influencia = (lado * apotema)/2
#carga sobre pilar
carga_no_pilar = (area_de_influencia * carga_do_piso)

#condicional de calculo da seção
#considerar unidade de peso em kN/m2
#Material:
# 1 - Concreto
# 2 - Madeira
if material == 1:
    area_da_secao = carga_no_pilar/100
elif material == 1:
    area_da_secao = carga_no_pilar/60


OUT = math.sqrt(area_da_secao)