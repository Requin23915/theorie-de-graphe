import networkx as nx
import matplotlib.pyplot as plt

def creer_graphe():
    G = nx.MultiDiGraph()

    # Nœuds
    G.add_node("Alice", type="Utilisateur")
    G.add_node("Bob", type="Utilisateur")
    G.add_node("Post123", type="Publication")
    G.add_node("DevGroup", type="Groupe")

    # Relations
    G.add_edge("Alice", "Bob", relation="est_ami_avec")
    G.add_edge("Bob", "Post123", relation="a_publié")
    G.add_edge("Alice", "Post123", relation="a_aimé")
    G.add_edge("Alice", "DevGroup", relation="membre_de")

    return G

if __name__ == "__main__":
    graphe = creer_graphe()
    print("✅ Graphe créé avec", graphe.number_of_nodes(), "nœuds et", graphe.number_of_edges(), "relations.")

    # Affichage graphique
    pos = nx.spring_layout(graphe)  # Position automatique des nœuds

    plt.figure(figsize=(8, 6))
    nx.draw(graphe, pos, with_labels=True, node_color='skyblue',
            node_size=1500, font_size=10, font_weight='bold',
            edge_color='gray', arrows=True)

    # Ajout manuel des labels des arêtes (fonctionne pour MultiDiGraph)
    for u, v, key, data in graphe.edges(data=True, keys=True):
        x = (pos[u][0] + pos[v][0]) / 2
        y = (pos[u][1] + pos[v][1]) / 2
        label = data.get('relation', '')
        plt.text(x, y, label, fontsize=9, color='red', ha='center', va='center')

    plt.title("Graphe Réseau Social")
    plt.axis('off')
    plt.tight_layout()
    plt.show()
