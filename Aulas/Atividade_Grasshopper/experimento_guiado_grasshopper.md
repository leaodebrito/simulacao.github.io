# Simulações de projeto com programação visual

## Programação e algoritmos (um resumo)
A programação informática é o ato de compor os elementos da linguagem de programação selecionada pela ordem que provocará o efeito desejado. O efeito pode ser diferente em cada caso específico - depende da imaginação, conhecimento e experiência do programador.
É claro que tal composição tem de ser correta em muitos sentidos:

- **alfabeticamente** - um programa precisa de ser escrito num guião reconhecível, tal como romano, cirílico, etc.
- **lexicamente** - cada linguagem de programação tem o seu dicionário e é preciso dominá-lo; felizmente, é muito mais simples e menor do que o dicionário de qualquer língua natural;
- **sintaticamente** - cada linguagem tem as suas regras, e estas devem ser obedecidas;
- **semanticamente** - o programa tem de fazer sentido.

_____
## O Exercício
**Justificar a escolha de uma solução para uma torre com base em aspectos geométricos, financeiros e urbanísticos**

_____
## Objeto do exercício

![](imagens/tipologia%20do%20estudo.png)

Possuímos um terreno em determinada localidade da cidade de Salvador, que apresenta os seguinte índices urbanísticos:
1. CAB: 1,5
2. CAM: 3,0
3. IP: 0,6

Deseja-se construir uma edificação residencial de apartamentos para venda neste terreno. Devemos achar uma solução ou um conjunto de soluções que possibilitem um retorno financeiro. Deve-se levar em consideração fatores como solução estrutural e renda do comprador para determinar se a solução é aceitável ou não.

Dados extras:
- Renda do comprador: R$10.000,00
- Financiamento: 30 anos
- Considerar 30% da renda para pagamento de parcelas
- Considerar entrada de 30% do valor da unidade

Caracteristicas da edificação
- Torre residencial
- Estrutura em concreto armado
- Participação da estrutura de concreto no custo total: 17%
_____

## Lógica do experimento

No link abaixo esta anexo a construção mental feita no nosso primeiro encontro que irá guiar nossas proximas atividades

[Esboço da estrutura do modelo](Aulas/Atividade_Grasshopper/esboco_experiemento/esboco_experimento.pdf)

_____

## Código para modelagem
Para desenvolver nossa simulação, vamos dividir nosso código em dois tipos de linguagem diferentes. A programação visual Grasshopper e a linguaguem script Python (aplicada nos blocos de código disponibilizados abaixo).

O código que iremos desenvolver estará divido da seguinte maneira:
1. Parâmetros de entrada
   1. Definição de parâmetros
   2. Definição de espaço de soluções
2. Modelagem indices urbanísticos
   1. Modelagem terreno
   2. Modelagem recuo
   3. Modelagem área ocupada
3. Modelagem estrutura
   1. Modelagem pilares
   2. Modelagem vigas
   3. Modelagem lajes
4. Extração de dados
5. Tratamento de dados
6. Análise de dados


### Blocos de código de apoio
Abaixo são disponibilizados insumos e blocos de códigos necessários para o desenvolvimento do modelo

- [Pologional de referência do trabalho](Aulas/Atividade_Grasshopper/Poligonal/Poligonal de referência.3dm)
- [Quantificação de elementos estruturais de concreto armado](Aulas/Atividade_Grasshopper/blocos de código/Componentes de quantificação.gh)
- [Extração de dados para CSV]()

_____


*_aos poucos eu irei alimentando com os códigos e algumas cositas mais..._