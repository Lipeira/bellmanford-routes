import PySimpleGUI as sg
import networkx as nx
import matplotlib.pyplot as plt


def VisualizarGrafo(grafo):
    G = nx.DiGraph()
    G.add_edges_from(grafo)
    nx.draw_networkx(G)
    plt.show()


class Vertices:
    def __init__(self):
        self.aeroportos = []
        self.caminhos = []


def relax(p, u, v, w, pred):
    if p[v] > p[u] + w:
        pred[v] = u
        p[v] = p[u] + w


def caminho(antecessor, peso, u, v, km, milhas):
    listaresult = [v]
    ant = antecessor[v]

    pesoresult = [str(peso[v])]

    while ant != -1:
        listaresult.append(ant)
        pesoresult.append(str(peso[ant]))
        ant = antecessor[ant]

    listaresult = listaresult[::-1]
    pesoresult = pesoresult[::-1]
    listaresultstring = []
    stringresult = " --> ".join(listaresult)
    stringpesoresult = " --> ".join(pesoresult)

    if len(listaresult) == 1:
        texto = f"Infelizmente não há rotas entre:\n\nOrigem: {u}\nDestino: {v}"
        sg.popup("RESULTADO:", texto)

    else:
        if milhas == True and km == False:
            for i in range(len(listaresult) - 1):
                stringatual = f"{listaresult[i]} --> {listaresult[i + 1]} : Distância = {((int(pesoresult[i + 1]) - int(pesoresult[i]))):.1f} Milhas "
                listaresultstring.append(stringatual)

            stringatual = f"\nDistância Total: {pesoresult[-1]} Milhas"
            listaresultstring.append(stringatual)

        elif milhas == False and km == True:
            for i in range(len(listaresult) - 1):
                stringatual = f"{listaresult[i]} --> {listaresult[i + 1]} : Distância = {(((int(pesoresult[i + 1]) - int(pesoresult[i]))) * 1.60934):.1f} km "
                listaresultstring.append(stringatual)

            stringatual = f"\nDistância Total: {(float(pesoresult[-1]) * 1.60934):.1f} km"
            listaresultstring.append(stringatual)

        else:
            for i in range(len(listaresult) - 1):
                stringatual = f"{listaresult[i]} --> {listaresult[i + 1]} : Distância = {(((int(pesoresult[i + 1]) - int(pesoresult[i]))) * 1.60934):.1f} km ou {((int(pesoresult[i + 1]) - int(pesoresult[i]))):.1f} Milhas"
                listaresultstring.append(stringatual)

            stringatual = f"\nDistância Total: {(float(pesoresult[-1]) * 1.60934):.1f} km ou {pesoresult[-1]} Milhas"
            listaresultstring.append(stringatual)

        listaresultstring.append(f"\nRota total:\n{stringresult}")
        stringfinal = "\n".join(listaresultstring)

        sg.popup("MENOR ROTA:", stringfinal)


def bellmanford(origin, graph, destiny, km, milhas):
    pred = {}
    p = {}
    for i in graph.aeroportos:
        p[i] = 9999999999
        pred[i] = -1

    p[origin] = 0

    for i in range(len(graph.aeroportos) - 1):
        for u, v, w in graph.caminhos:
            relax(p, u, v, w, pred)

    for u, v, w in graph.caminhos:
        if p[v] > p[u] + w:
            print('Ciclo negativo encontrado!')
            return False

    caminho(pred, p, origin, destiny, km, milhas)

    return True


class TelaPython:
    def __init__(self):

        sg.theme("Black")
        layout = [

            [sg.Text("Origem:", size=(10, 0)), sg.Input(size=(30, 0), key="origemi")],
            [sg.Text("Destino:", size=(10, 0)), sg.Input(size=(30, 0), key="destinoi")],
            [sg.Text("Escolha a(s) medidas de conversão:")],
            [sg.Checkbox("Km", key="conversaokm"), sg.Checkbox("Milhas", key="conversaomilhas")],
            [sg.Button("Calcular rota"), sg.Button("Lista de aeroportos disponíveis")],
            [sg.Button("Visualizar Grafo")]

        ]

        self.janela = sg.Window("Menores Rotas Aeroportos", layout)

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            origem = self.values["origemi"]
            destino = self.values["destinoi"]
            km = self.values["conversaokm"]
            milhas = self.values["conversaomilhas"]

            if self.button == sg.WINDOW_CLOSED:
                break

            if self.button == "Calcular rota":

                if origem == "" or destino == "":
                    text = f"Input vazio!"
                    sg.popup("ERRO", text)

                elif origem in v.aeroportos and destino in v.aeroportos:

                    if milhas == False and km == False:
                        text = f"Escolha uma das opções de medidas de distância!"
                        sg.popup("ERRO", text)
                    else:
                        bellmanford(origem, v, destino, km, milhas)

                    text = f"Origem: {origem}\nDestino: {destino}\n\n Não há caminho direto entre eles!"

                elif origem in v.aeroportos and destino not in v.aeroportos:
                    text = f"{destino} não está na base de dados!\nverifique a lista de aeroportos disponíveis! "
                    sg.popup("ERRO", text)

                elif origem not in v.aeroportos and destino in v.aeroportos:
                    text = f"{origem} não está na base de dados!\nverifique a lista de aeroportos disponíveis! "
                    sg.popup("ERRO", text)

                else:
                    text = f"{origem} e {destino} não estão na base de dados!\nverifique a lista de aeroportos disponíveis! "
                    sg.popup("ERRO", text)

            if self.button == "Lista de aeroportos disponíveis":
                text = "\t".join(v.aeroportos)

                sg.popup("Lista de aeroportos disponíveis", text)

            if self.button == "Visualizar Grafo":
                VisualizarGrafo(grafo)


v = Vertices()
tela = TelaPython()
grafo = []

try:
    arquivodistancias = open("Dados.txt", "r")

    with arquivodistancias:
        for line in arquivodistancias:
            o, d, w = line.split()

            if o not in v.aeroportos:
                v.aeroportos.append(o)
            if d not in v.aeroportos:
                v.aeroportos.append(d)

            if [o, d, w] not in v.caminhos:
                v.caminhos.append([o, d, int(w)])
            else:
                pass

            grafo.append([o, d])

    print("qtd vertices:")
    print(len(v.aeroportos))
    print("qtd conexoes:")
    print(len(v.caminhos))

except FileNotFoundError as msg:
    print(msg)

tela.Iniciar()

