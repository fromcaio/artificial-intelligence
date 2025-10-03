import heapq

class GreedyBestFirstSearch:
    """
    Implementa o algoritmo de busca gulosa pela melhor escolha.
    Prioriza o nó que está heuristicamente mais perto do objetivo.
    """
    def __init__(self, graph, heuristic):
        self.graph = graph
        self.heuristic = heuristic

    def search(self, start, goal):
        frontier = []
        heapq.heappush(frontier, (self.heuristic.h(start), start))
        came_from = {start: None}
        
        # Otimização: visited não é estritamente necessário se checarmos 'in came_from'
        # mas mantido para clareza como no original.
        visited = set()

        while frontier:
            _, current = heapq.heappop(frontier)

            if current == goal:
                return self.reconstruct_path(came_from, goal)

            visited.add(current)

            for neighbor in self.graph.neighbors(current):
                if neighbor not in came_from:
                    came_from[neighbor] = current
                    heapq.heappush(frontier, (self.heuristic.h(neighbor), neighbor))
        return None

    def reconstruct_path(self, came_from, goal):
        path = []
        current = goal
        while current is not None:
            path.append(current)
            current = came_from.get(current)
        path.reverse()
        return path


class AStarSearch:
    """
    Implementa o algoritmo de busca A* (A-star).
    Encontra o caminho de menor custo balanceando o custo real (g(n)) e a heurística (h(n)).
    """
    def __init__(self, graph, heuristic):
        self.graph = graph
        self.heuristic = heuristic

    def search(self, start, goal):
        frontier = []
        # A prioridade inicial deve incluir o custo g(n), que é 0 para o início.
        heapq.heappush(frontier, (0 + self.heuristic.h(start), start))
        
        came_from = {start: None}
        cost_so_far = {start: 0}

        while frontier:
            _, current = heapq.heappop(frontier)

            if current == goal:
                return self.reconstruct_path(came_from, goal)

            for neighbor in self.graph.neighbors(current):
                new_cost = cost_so_far[current] + self.graph.cost(current, neighbor)
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + self.heuristic.h(neighbor)
                    heapq.heappush(frontier, (priority, neighbor))
                    came_from[neighbor] = current
        return None

    def reconstruct_path(self, came_from, goal):
        path = []
        current = goal
        while current is not None:
            path.append(current)
            current = came_from.get(current)
        path.reverse()
        return path