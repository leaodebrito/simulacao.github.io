#TODO: Inserir código na explicação da atividade

comprimento_viga = IN[0]
base_viga = IN[1]
altura_viga = IN[2]

comprimento_pilar = IN[3]
lado_pilar = IN[4]

#Calculo de forma das vigas
forma_viga = (base_viga + (altura_viga * 2)) * comprimento_viga

#calculo de forma dos pilares
forma_pilar = (lado_pilar * 4) * comprimento_pilar

#quantidade total de formas
total_forma = forma_pilar + forma_viga


OUT = total_forma