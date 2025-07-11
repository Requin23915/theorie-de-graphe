# theorie-de-graphe
 📊 Graphe de connaissances - Réseaux sociaux

Ce projet est un exemple de graphe de connaissances dans le domaine des *réseaux sociaux*, construit à l’aide de la bibliothèque Python networkx.

---

## 🧠 Domaine : Réseaux sociaux

Le graphe modélise les utilisateurs, leurs interactions (amis, publications, likes), les groupes et les publications.

---

## ❓ Questions auxquelles le graphe répond

1. Qui sont les amis de l’utilisateur Alice ?
2. Quels utilisateurs ont commenté une publication de Bob ?
3. Quelles publications ont été aimées par Charlie ?
4. Combien de groupes Diana a-t-elle rejoints ?
5. Qui a publié le post le plus récent ?
6. Quels utilisateurs sont membres du même groupe que Eve ?
7. Quelle est la publication la plus commentée ?
8. Combien d’interactions a reçu une publication donnée ?
9. Quels sont les amis communs entre Alice et Frank ?
10. Qui a partagé le plus de publications ce mois-ci ?

## 🧩 Types de nœuds et relations

- *Nœuds* :
  - Utilisateur
  - Publication
  - Groupe
  - Événement
  - Commentaire

- *Relations* :
  - est_ami_avec
  - a_publié
  - a_commenté
  - a_aimé
  - membre_de
  - participe_à
  - commentaire_de
⚙️ Exécution du programme
### Prérequis :
- Python 3
- Bibliothèque networkx

### Installation :
```bash
pip install networkx
