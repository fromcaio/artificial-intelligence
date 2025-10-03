class Heuristic:
    """
    Classe para encapsular a função heurística, que estima o custo de um nó até o objetivo.
    """
    def __init__(self, goal, values):
        self.goal = goal
        self.values = values

    def h(self, node):
        """Retorna o valor heurístico para um nó. Se o nó não for encontrado, retorna infinito."""
        return self.values.get(node, float('inf'))