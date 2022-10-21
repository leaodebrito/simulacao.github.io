vao = IN[0]
material = IN[1]
intesidade_carga = IN[2]

#Material:
# 1 - Concreto
# 2 - Madeira
if material == 1:
    if intesidade_carga == 1:
        altura_viga = vao * 0.08
    elif intesidade_carga == 2:
        altura_viga = vao * 0.10
elif material == 2:
    if intesidade_carga == 1:
        altura_viga = vao * 0.10
    elif intesidade_carga == 2:
        altura_viga = vao * 0.12

OUT = altura_viga
