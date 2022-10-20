# Simulações de projeto com Dynamo/Revit


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



## Lógica do experimento

No link abaixo esta anexo a construção mental feita no nosso primeiro encontro que irá guiar nossas proximas atividades
- [Mapa Mental](/Aulas/Atividade%20Dynamo/Ferramentas%20e%20simulações.pdf)


## A Edificação 
A tipologia de edificação que iremos desenvolver e simular é a seguinte:

![Quiosque](https://github.com/leaodebrito/simulacao.github.io/blob/main/Aulas/AtividadeDynamo/imagem/Quiosque.png?raw=true)


## O código para simulação

### programação e algoritmos (um resumo)
A programação informática é o ato de compor os elementos da linguagem de programação selecionada pela ordem que provocará o efeito desejado. O efeito pode ser diferente em cada caso específico - depende da imaginação, conhecimento e experiência do programador.
É claro que tal composição tem de ser correta em muitos sentidos:

- **alfabeticamente** - um programa precisa de ser escrito num guião reconhecível, tal como romano, cirílico, etc.
- **lexicamente** - cada linguagem de programação tem o seu dicionário e é preciso dominá-lo; felizmente, é muito mais simples e menor do que o dicionário de qualquer língua natural;
- **sintaticamente** - cada linguagem tem as suas regras, e estas devem ser obedecidas;
- **semanticamente** - o programa tem de fazer sentido.

### Nosso código
Para desenvolver nossa simulação, vamos dividir nosso código em dois tipos de linguagem diferentes. A programação visual Dynamo e a linguaguem script Python.
Essa divisão será da seguinte maneira:

**[Programação visual](https://github.com/leaodebrito/simulacao.github.io/blob/main/Aulas/AtividadeDynamo/imagem/algoritmoDynamo.png?raw=true)**
1. Estrutura de linhas para modelagem
2. Atribuição das famílias paramétricas
3. Inserção de valores em parâmetros
4. Levantamentos de parãmetros


**Python**
1. Cálculo de pré-dimensionamento dos elementos estruturais

**Terças e vigas; e**
```
#Altura da viga

vao = IN[0]
material = IN[1]
intesidade_carga = IN[2]

if material == "concreto":
    if intesidade_carga == 1:
        altura_viga = vao * 0.08
    elif intesidade_carga == 2:
        altura_viga = vao * 0.10
elif material == "madeira":
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

**Pilares**
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
#considerar unidade de peso em kgf/cm²
if material == "concreto":
    area_da_secao = carga_no_pilar/100
elif material == "madeira":
    area_da_secao = carga_no_pilar/60


OUT = math.sqrt(area_da_secao)
```


2. Cálculo dos insumos para orçamento
3. Cálculo dos valores de custos


*_aos poucos eu irei alimentando com os códigos e algumas cositas mais..._