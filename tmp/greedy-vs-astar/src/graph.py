import networkx as nx

class CampusGraph:
    """
    Classe para encapsular o grafo do campus universitário, utilizando a biblioteca NetworkX.
    """
    def __init__(self):
        self.G = nx.Graph()

    def add_nodes(self, nodes):
        """Adiciona uma lista de nós ao grafo."""
        self.G.add_nodes_from(nodes)

    def add_edges(self, edges):
        """Adiciona uma lista de arestas ponderadas ao grafo."""
        # Formato esperado para edges: (origem, destino, peso)
        self.G.add_weighted_edges_from(edges)

    def neighbors(self, node):
        """Retorna os vizinhos de um nó específico."""
        return self.G.neighbors(node)

    def cost(self, u, v):
        """Retorna o custo (peso) da aresta entre dois nós."""
        return self.G[u][v]['weight']