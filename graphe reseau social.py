import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter, defaultdict

def creer_graphe():
    G = nx.MultiDiGraph()

    # Nœuds : Utilisateurs
    G.add_node("Alice", type="Utilisateur")
    G.add_node("Bob", type="Utilisateur")
    G.add_node("Charlie", type="Utilisateur")
    G.add_node("Diane", type="Utilisateur")

    # Nœuds : Publications
    G.add_node("Post1", type="Publication")
    G.add_node("Post2", type="Publication")
    G.add_node("Post3", type="Publication")

    # Nœuds : Groupes
    G.add_node("PythonLovers", type="Groupe")
    G.add_node("DataScience", type="Groupe")

    # Relations : Amitiés
    G.add_edge("Alice", "Bob", relation="est_ami_avec")
    G.add_edge("Bob", "Charlie", relation="est_ami_avec")
    G.add_edge("Charlie", "Diane", relation="est_ami_avec")
    G.add_edge("Alice", "Diane", relation="est_ami_avec")

    # Relations : Publications
    G.add_edge("Alice", "Post1", relation="a_publié")
    G.add_edge("Bob", "Post2", relation="a_publié")
    G.add_edge("Charlie", "Post3", relation="a_publié")

    # Relations : Likes
    G.add_edge("Bob", "Post1", relation="a_aimé")
    G.add_edge("Charlie", "Post1", relation="a_aimé")
    G.add_edge("Diane", "Post2", relation="a_aimé")
    G.add_edge("Alice", "Post3", relation="a_aimé")
    G.add_edge("Diane", "Post3", relation="a_aimé")

    # Appartenance à des groupes
    G.add_edge("Alice", "PythonLovers", relation="membre_de")
    G.add_edge("Bob", "PythonLovers", relation="membre_de")
    G.add_edge("Charlie", "DataScience", relation="membre_de")
    G.add_edge("Diane", "PythonLovers", relation="membre_de")
    G.add_edge("Diane", "DataScience", relation="membre_de")

    # Publication dans un groupe
    G.add_edge("Post1", "PythonLovers", relation="publié_dans")
    G.add_edge("Post2", "PythonLovers", relation="publié_dans")
    G.add_edge("Post3", "DataScience", relation="publié_dans")

    return G

# Fonctions pour répondre aux 10 questions

def amis_utilisateur(G, utilisateur):
    return [v for u, v, d in G.edges(data=True) if u == utilisateur and d["relation"] == "est_ami_avec"]

def publications_utilisateur(G, utilisateur):
    return [v for u, v, d in G.edges(data=True) if u == utilisateur and d["relation"] == "a_publié"]

def utilisateurs_ayant_aime(G, publication):
    return [u for u, v, d in G.edges(data=True) if v == publication and d["relation"] == "a_aimé"]

def groupes_utilisateur(G, utilisateur):
    return [v for u, v, d in G.edges(data=True) if u == utilisateur and d["relation"] == "membre_de"]

def utilisateurs_ayant_publié_dans_groupe(G, groupe):
    publications = [u for u, v, d in G.edges(data=True) if v == groupe and d["relation"] == "publié_dans"]
    auteurs = []
    for pub in publications:
        auteurs += [u for u, v, d in G.edges(data=True) if v == pub and d["relation"] == "a_publié"]
    return list(set(auteurs))

def publications_avec_plus_de_reactions(G):
    counter = Counter()
    for u, v, d in G.edges(data=True):
        if d["relation"] == "a_aimé":
            counter[v] += 1
    max_reactions = max(counter.values(), default=0)
    return [pub for pub, count in counter.items() if count == max_reactions]

def utilisateur_avec_plus_d_interactions(G):
    counter = Counter()
    for u, v, d in G.edges(data=True):
        if d["relation"] == "a_aimé":
            counter[u] += 1
    max_interactions = max(counter.values(), default=0)
    return [user for user, count in counter.items() if count == max_interactions]

def utilisateurs_partageant_publications(G):
    aime = defaultdict(set)
    for u, v, d in G.edges(data=True):
        if d["relation"] == "a_aimé":
            aime[v].add(u)
    pairs = set()
    for users in aime.values():
        users = list(users)
        for i in range(len(users)):
            for j in range(i+1, len(users)):
                pairs.add(tuple(sorted((users[i], users[j]))))
    return list(pairs)

def groupes_les_plus_populaires(G):
    counter = Counter()
    for u, v, d in G.edges(data=True):
        if d["relation"] == "membre_de":
            counter[v] += 1
    max_members = max(counter.values(), default=0)
    return [groupe for groupe, count in counter.items() if count == max_members]

def relations_utilisateur(G, utilisateur):
    relations = []
    for u, v, d in G.edges(data=True):
        if u == utilisateur:
            relations.append((d["relation"], v))
    return relations

# Exécution
if __name__ == "__main__":
    G = creer_graphe()

    print("1. Amis d'Alice :", amis_utilisateur(G, "Alice"))
    print("2. Publications d'Alice :", publications_utilisateur(G, "Alice"))
    print("3. Qui a aimé Post1 :", utilisateurs_ayant_aime(G, "Post1"))
    print("4. Groupes d'Alice :", groupes_utilisateur(G, "Alice"))
    print("5. Utilisateurs ayant publié dans PythonLovers :", utilisateurs_ayant_publié_dans_groupe(G, "PythonLovers"))
    print("6. Publications les plus aimées :", publications_avec_plus_de_reactions(G))
    print("7. Utilisateur le plus actif (likes) :", utilisateur_avec_plus_d_interactions(G))
    print("8. Utilisateurs partageant des publications aimées :", utilisateurs_partageant_publications(G))
    print("9. Groupes les plus populaires :", groupes_les_plus_populaires(G))
    print("10. Relations d'Alice :", relations_utilisateur(G, "Alice"))

    # Affichage du graphe
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color='skyblue',
            node_size=2000, font_size=10, font_weight='bold',
            edge_color='gray', arrows=True)
    for u, v, key, data in G.edges(data=True, keys=True):
        x = (pos[u][0] + pos[v][0]) / 2
        y = (pos[u][1] + pos[v][1]) / 2
        label = data.get('relation', '')
        plt.text(x, y, label, fontsize=8, color='red', ha='center', va='center')

    plt.title("Graphe de Connaissances - Réseau Social")
    plt.axis('off')
    plt.tight_layout()
    plt.show()
