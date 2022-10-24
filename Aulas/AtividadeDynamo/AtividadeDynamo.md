# Simulações de projeto com Dynamo/Revit

## Programação e algoritmos (um resumo)
A programação informática é o ato de compor os elementos da linguagem de programação selecionada pela ordem que provocará o efeito desejado. O efeito pode ser diferente em cada caso específico - depende da imaginação, conhecimento e experiência do programador.
É claro que tal composição tem de ser correta em muitos sentidos:

- **alfabeticamente** - um programa precisa de ser escrito num guião reconhecível, tal como romano, cirílico, etc.
- **lexicamente** - cada linguagem de programação tem o seu dicionário e é preciso dominá-lo; felizmente, é muito mais simples e menor do que o dicionário de qualquer língua natural;
- **sintaticamente** - cada linguagem tem as suas regras, e estas devem ser obedecidas;
- **semanticamente** - o programa tem de fazer sentido.

_____
## O Dynamo

O Dynamo é uma ferramenta de código aberto, portanto gratuita, desenvolvida para estender as funcionalidades do Autodesk Revit. Nas versões mais recentes do Revit a instalação do Dynamo é automática, mas também está disponível para download em DynamoBIM.org.

**Essencialmente, o Dynamo é uma ferramenta de programação que usa uma estrutura chamada de “programação visual”. Com a programação visual, o usuário pode “montar” suas próprias aplicações, mesmo sem possuir conhecimento em linguagens de programação.**

Com isso, o Dynamo pode ser utilizado em diversas aplicações sejam automatização de tarefas repetitivas, interações com o modelo do Revit, ou para criação de modelos a partir de regras complexas ou de dados externos.

Criar uma aplicação em Dynamo, também chamada de rotina, é basicamente a montagem de uma sequência de tarefas a serem executadas.

**Cada tarefa pode ser entendida como um comando do próprio Revit, mas também pode ser uma operação matemática ou qualquer outro recurso pré-programado, nativo ou não**. Ou seja, uma tarefa pode ser alterar o valor de um parâmetro de um elemento, selecionar objetos, comparar valores, ler e escrever planilhas de Excel, criar e apagar objetos no modelo, etc.

**Cada tarefa individual recebe o nome de “nó”. Ao conectar os nós necessários, o usuário cria uma sequência lógica que pode ser executada automaticamente enquanto o usuário trabalha no Revit ou através de um clique.**


Abaixo segue alguns links de referência sobre o Dynamo
- [Dynamobim.org](https://dynamobim.org)
- [Biblioteca de nós](https://dictionary.dynamobim.com/#/Analyze)
- [Vídeos tutoriais](https://dynamobim.org/#videoTut)

_____

## Lógica do experimento

No link abaixo esta anexo a construção mental feita no nosso primeiro encontro que irá guiar nossas proximas atividades
- [Mapa Mental](https://github.com/leaodebrito/simulacao.github.io/blob/main/Aulas/AtividadeDynamo/Ferramentas%20e%20simulações.pdf)

_____

## A Edificação 
A tipologia de edificação que iremos desenvolver e simular é a seguinte:

- Quiosque de planta regular com pilares distribuídos perimetralmente;
- Fundação em concreto armado
- Estrutura em concreto armado ou madeira
- Cobertura em concreto armado ou madeira

![Quiosque](https://github.com/leaodebrito/simulacao.github.io/blob/main/Aulas/AtividadeDynamo/imagem/Quiosque.png?raw=true)

_____
## O código para simulação

### Nosso código
Para desenvolver nossa simulação, vamos dividir nosso código em dois tipos de linguagem diferentes. A programação visual Dynamo e a linguaguem script Python.
Essa divisão será da seguinte maneira:


**[Programação visual](https://github.com/leaodebrito/simulacao.github.io/blob/main/Aulas/AtividadeDynamo/imagem/algoritmoDynamo.png?raw=true)**
1. Estrutura de linhas para modelagem
2. Atribuição das famílias paramétricas
3. Inserção de valores em parâmetros
4. Levantamentos de parãmetros


**[Python](https://github.com/leaodebrito/simulacao.github.io/tree/main/Aulas/AtividadeDynamo/BlocosDeCodigo)**

1. **Cálculo de pré-dimensionamento dos elementos estruturais**

a.Terças e vigas
```
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
```

```
#Base da Viga

altura_viga = IN[0]

OUT = altura_viga * (2/3)
```

b.Pilares
```
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
```

_
2. **Cálculo dos insumos para orçamento**


a.Quantificação da área de forma
```
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
```

b.Quantificação de volume de concreto
```
#Esse bloco de código também pode ser usado para calculo do volume de madeira desde que seja modificado a condicional

quantidade_elementos = IN[0]
volume_pilar = IN[1]
volume_viga = IN[2]

volume = (volume_viga * quantidade_elementos) + (volume_pilar * quantidade_elementos)

OUT = volume
```
_
3. **Cálculo dos valores de custos**


```
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
```

Para baixar os arquivos .py basta clicar no link: [Código python no GitHub](https://github.com/leaodebrito/simulacao.github.io/blob/54bc2bc20d2881c5ac7cbd03c1a450e41b247216/Aulas/AtividadeDynamo/BlocosDeCodigo)

___
### Extração de dados
Após a modelagem começa a etapa de extração de dados. Essa atividade também é feita através do Dynamo. Para isso, vamos usar o código composto pelos Nós apresentados na imagem abaixo

![Código para extração de informações](https://github.com/leaodebrito/simulacao.github.io/blob/b6759b7b9ade7bf48cbd7d9472d87135ba7a9769/Aulas/AtividadeDynamo/imagem/extrairDados.png)

Após levantamento dos dados, é feito a quantificação dos elementos para que seja feita a estimativa de custo. Os código para essa parte estão na seção anterior.

Depois da extração dos dados e da realização dos cálculos necessários, os dados deve ser escritos em uma planilha para que possamos analisa-los e consequentemente tomar uma decisão a cerca do projeto.
O código para escrita dos dados no é apresentado na imagem abaixo.

![Código para escrita de dados no excel](https://github.com/leaodebrito/simulacao.github.io/blob/b6759b7b9ade7bf48cbd7d9472d87135ba7a9769/Aulas/AtividadeDynamo/imagem/escreverExvel.png)

As informações que serão extraídas (na ordem que aparecem na imagem) são:
- Raio - IN[0]
- Quantidade de lados - IN[1]
- Altura da cobertura - IN[2]
- Profundidade da fundação - IN[3]
- Inclinação - IN[4]
- Área do Quiosque - IN[5]
- Intensidade da carga - IN[6]
- Carregamento do pilar - IN[7]
- Material da fundação - IN[8]
- Material da estrutura - IN[9]
- Material das terças da cobertura - IN[10]
- Volume de concreto - IN[11]
- Área de forma - IN[12]
- Peso de aço - IN[13]
- Volume de madeira - IN[14]
- Custo total - IN[15]






*_aos poucos eu irei alimentando com os códigos e algumas cositas mais..._
