
## Sumário:
____

[Contexto](#contextualização) 

[Resolução do Problema](#resolução-do-problema)

[Implementação](#implementação)

[Conclusão](#conclusão)

[Clonar Git](#clonar-git)

____

## Contextualização:
<br>
Um planejador de voos aéreos estava decidindo otimizar as rotas de voos no mundo. Para isso ele procurou os principais aeroportos internacionais para entender como são suas conexões e a distância entre eles, a fim de otimizar as rotas e proporcionar uma redução de custo e tráfego aéreo. Seria mesmo possível tal fato?

Suponha uma situação hipotética em que você deseja viajar o mais rápido possível para outro país, mas não conhece as rotas e portanto não terá como saber o meio mais rápido. Ou ainda pior, algumas rotas foram canceladas e apenas poucas sobraram, logo, você deve optar por um caminho mapeado previamente para alcançar seu objetivo. Como resolver?

[Acessar base de dados](https://drive.google.com/file/d/1V86ZiVePa0FSoB-TZ38AkVKpghoIvRgv/view)

Ao todo anotamos 135 conexões realizadas entre 93 aeroportos localizadas no mundo todo.
A foto ao lado comprova esse quantitativo após colocarmos os dados em uma lista e vermos se existia alguma repetição ou não. 
No final, fizemos o programa dar um output relacionado a cada vértice e seu quantitativo, bem como todas as conexões analisadas no banco de dados.

Utilizamos o miro para analisar toda a base de dados e fazer a construção de um grafo temporário apenas para facilitar a nossa visualização e a explicação no projeto.

[Acessar grafo no MIRO](https://miro.com/app/board/uXjVO80ehqk=/)

______
## Resolução do Problema: 
<br>
Uma solução simples e eficaz seria utilizar algum programa ou alguma tecnologia que calculasse e nos desse esse caminho e o trajeto a ser realizado. Mas será que existe tal algoritmo?
A resposta é sim. O problema pode ser solucionado ao utilizar algoritmos bastante conhecidos como o Algoritmo de Dijkstra ou de Bellman-Ford. Optamos pelo de Bellman-Ford e o nosso objetivo consiste em partir de uma origem definida até o destino final. Além disso, estaremos mostrando todo o percurso para alcançar o destino, bem como a distância entre cada ponto.
Dessa forma, além de facilmente escolher o menor caminho entre um aeroporto e outro baseado de acordo com nossa base de dados, também é possível saber a distância entre cada aeroporto individualmente e a sua soma final para todo o trajeto.

Métodos Utilizados:

Para resolver tal problema proposto, utilizaremos o algoritmo de Bellman-Ford, um algoritmo que se assemelha bastante com o algoritmo de Dijkstra, pois os dois têm o mesmo objetivo de encontrar o menor caminho entre os vértices de uma grafo direcionado, porém o Bellman-Ford aceita arestas negativas em uma grafo, enquanto o Dijkstra aceita somente positivas. 

Utilizando o Bellman-Ford, nós escolhemos um vértice de origem, que em nosso exemplo seria uma aeroporto qualquer que compõe a base de dados,  e selecionamos arestas aleatoriamente dentro do grafo até que todas possibilidades tenham sido feitas e nos retorne o grafo com seus menores caminhos para um destino. Logo, por encontrar o menor caminho de forma eficiente, é notório que tal método é suficiente para solucionar o nosso problema proposto anteriormente. 

No final se torna possível obter o menor caminho dentre todas as possibilidades ligando àquele aeroporto passado como origem até outro, com a resposta sendo dada em milhas ou km. Vale ressaltar que escolhemos este dado apenas para facilitar os cálculos, porém poderíamos passar o preço da viagem também ou até a hora. No entanto, ambos são diretamente proporcionais à distância, logo, indo de X até Y com uma distância de 8000 milhas custará um preço razoavelmente alto e um tempo moderado.

Um ponto importante a ser ressaltado de Bellman-Ford é que ele percorre todas as arestas |V| - 1 vezes, isto é, parte de um vértice de origem e relaxa todas as arestas ligadas à ele. Depois partimos para outro vértice e relaxamos todas as arestas conectadas a ele. Tudo isso em um loop até que seja percorrido |V| – 1. 

A técnica de relaxar é basicamente escolher o menor caminho(menor custo) dado dois caminhos até um mesmo vértice. 

Após esse loop, o programa faz com que ele entre em outra repetição apenas para checar se existe arestas negativas ou não. No entanto, como estamos tratando da distância entre um aeroporto e outro nunca teremos distância negativa, porém é importante ter essa etapa em seu programa, uma vez que é a definição do próprio algoritmo de Bellman-Ford.

Por fim, fizemos uma interface gráfica e um visualizador de grafos unificando todos em um único programa. Mas o ponto principal é apenas demonstrar como encontrar o menor caminho com o algoritmo escolhido.

____

## Implementação:
<br>

Como escolhemos o Algoritmo de Bellman-Ford criamos um programa que partirá de uma origem definida até seu destino relaxando todas as arestas existentes na base de dados. Além disso, criamos uma interface gráfica e um visualizador de grafos, unificando todos eles juntamente do próprio Algoritmo de Bellman-Ford.

### Bibliotecas:

As bibliotecas que utilizamos foram:
	- PySimpleGUI
	- Networkx
	- Matplotlib

### PySimpleGUI --> Interface Gráfica
### Networkx --> Visualizador de Grafos
### Matplotlib --> Plotar o Visualizador de Grafos
<br>

### Interface Gráfica:

Nossa Interface Gráfica é capaz de calcular a rota mostrando todos os caminhos percorrido até o destino, além de mostrar todos os aeroportos disponíveis também(quantidade de vértices).

Por fim, adicionamos a opção de Visualizar Grafo que mostra exatamente como está sendo feita todas as conexões caso tenha alguma dúvida ou não saiba para onde ir.

### Visualizador de Grafos:

O visualizar de grafos consegue representar com precisão todas as conexões feitas como se fosse exatamente um grafo direcionado que é o nosso objetivo. Além disso, as informações batem com o grafo provisório que fizemos no Miro mostrado em slides anteriores.

_____

## Conclusão:
<br>
Finalizando o projeto podemos constatar o sucesso do algoritmo implantado, bem como a resolução do problema proposto. Vale ressaltar que a complexidade do algoritmo é O(|V| x |E|), uma complexidade relativamente boa , que nos traz um bom resultado se implementada no exercício proposto. 
Poderíamos tentar aprimorar o algoritmo para mostrar não só o menor caminho de um aeroporto à outro, mas também mostrar todos os menores caminhos possíveis existentes entre todos os aeroportos! Mas é claro, levaria mais tempo e seria um pouco mais complicado. Nosso objetivo é apenas demonstrar como funciona o Algoritmo de Bellman-Ford e sua aplicação no dia a dia podendo ser de extrema importância.

<br>

### Referências:

https://www.flightconnections.com

http://www.distanciascidades.com/pesquisa/

https://distancecalculator.globefeed.com/Distance_Between_Countries.asp

https://www.youtube.com/watch?v=Et0fYeA2XxY

___
## Clonar Git

```bash
$ cd 
$ cd Desktop
$ mkdir GithubRepository
$ cd GithubRepository
$ git clone https://hostname/YOUR-USERNAME/YOUR-REPOSITORY

```

Ferramenta:<br>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
