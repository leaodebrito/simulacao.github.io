#Esse bloco de código também pode ser usado para calculo do volume de madeira desde que seja modificado a condicional

quantidade_elementos = IN[0]
volume_pilar = IN[1]
volume_viga = IN[2]

volume = (volume_viga * quantidade_elementos) + (volume_pilar * quantidade_elementos)

OUT = volume