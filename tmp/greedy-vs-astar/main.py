from src.graph import CampusGraph
from src.heuristic import Heuristic
from src.search import GreedyBestFirstSearch, AStarSearch

def main():
    """
    Função principal para configurar e executar os algoritmos de busca no grafo do campus.
    """
    # 1. Definindo a estrutura do grafo (nós e arestas)
    nodes = [
        "Entrada Lateral BR", "Entrada Principal BR", "Campo Futebol",
        "Ponto Onibus/Musica", "Capela CTAN", "Departamento de Arquitetura",
        "Restaurante Universitario", "Moradia Estudantil",
        "Departamento de Ciencia da Computacao", "Biblioteca",
        "Departamento de Zootecnia", "Departamento de Geografia",
        "Departamento de Artes Aplicadas", "Centro Pesquisa Queijos",
        "Entrada Estrada de Terra"
    ]
    edges = [
        ("Centro Pesquisa Queijos", "Entrada Estrada de Terra", 500),
        ("Departamento de Artes Aplicadas", "Centro Pesquisa Queijos", 79),
        ("Departamento de Geografia", "Departamento de Artes Aplicadas", 84),
        ("Departamento de Geografia", "Biblioteca", 150),
        ("Departamento de Geografia", "Departamento de Zootecnia", 140),
        ("Biblioteca", "Departamento de Zootecnia", 10),
        ("Biblioteca", "Departamento de Ciencia da Computacao", 61),
        ("Departamento de Zootecnia", "Departamento de Ciencia da Computacao", 61),
        ("Biblioteca", "Restaurante Universitario", 190),
        ("Departamento de Zootecnia", "Restaurante Universitario", 190),
        ("Departamento de Ciencia da Computacao", "Moradia Estudantil", 140),
        ("Restaurante Universitario", "Departamento de Arquitetura", 110),
        ("Restaurante Universitario", "Campo Futebol", 120),
        ("Departamento de Arquitetura", "Capela CTAN", 200),
        ("Capela CTAN", "Ponto Onibus/Musica", 110),
        ("Ponto Onibus/Musica", "Campo Futebol", 130),
        ("Capela CTAN", "Campo Futebol", 65),
        ("Campo Futebol", "Entrada Principal BR", 77),
        ("Campo Futebol", "Entrada Lateral BR", 120),
    ]

    # 2. Instanciando e populando o grafo
    campus = CampusGraph()
    campus.add_nodes(nodes)
    campus.add_edges(edges)

    # 3. Definindo a heurística (distância estimada até a "Entrada Principal BR")
    heuristic_values = {
        "Entrada Principal BR": 0, "Campo Futebol": 77, "Capela CTAN": 150,
        "Ponto Onibus/Musica": 180, "Restaurante Universitario": 250,
        "Departamento de Ciencia da Computacao": 300, "Biblioteca": 320,
        "Departamento de Zootecnia": 330, "Departamento de Geografia": 360,
        "Departamento de Artes Aplicadas": 400, "Centro Pesquisa Queijos": 450,
        "Entrada Estrada de Terra": 500, "Entrada Lateral BR": 120,
        "Moradia Estudantil": 350, "Departamento de Arquitetura": 220,
    }
    h = Heuristic(goal="Entrada Principal BR", values=heuristic_values)

    # 4. Definindo início e fim da busca
    start_node = "Entrada Estrada de Terra"
    goal_node = "Entrada Principal BR"

    # 5. Executando e imprimindo os resultados
    print("Executando buscas de '{}' para '{}'...\\n".format(start_node, goal_node))
    
    # Busca Gulosa
    gbfs = GreedyBestFirstSearch(campus, h)
    path_gulosa = gbfs.search(start=start_node, goal=goal_node)
    print("Caminho encontrado (Busca Gulosa):", path_gulosa)

    # Busca A*
    astar = AStarSearch(campus, h)
    path_astar = astar.search(start=start_node, goal=goal_node)
    print("Caminho encontrado (A*):", path_astar)

if __name__ == "__main__":
    main()