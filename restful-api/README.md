# 🌐 Introduction à HTTP, HTTPS et les requêtes API

---

## Sommaire

- [1. Différence entre HTTP et HTTPS](#1-différence-entre-http-et-https)
- [2. Fonctionnement de base d’une requête et réponse HTTP](#2-fonctionnement-de-base-dune-requête-et-réponse-http)
- [3. Méthodes HTTP et codes de statut](#3-méthodes-http-et-codes-de-statut)
  - [🔵 1xx – Informations](#🔵-1xx--informations)
  - [🟢 2xx – Succès](#🟢-2xx--succès)
  - [🟡 3xx – Redirections](#🟡-3xx--redirections)
  - [🔴 4xx – Erreurs client](#🔴-4xx--erreurs-client)
  - [🔥 5xx – Erreurs serveur](#🔥-5xx--erreurs-serveur)
- [4. curl : outil en ligne de commande](#4-curl--outil-en-ligne-de-commande)


---

## 1. Différence entre HTTP et HTTPS

### 🔍 Définition
- **HTTP** : HyperText Transfer Protocol  
- **HTTPS** : HyperText Transfer Protocol Secure  
> Protocole utilisé pour échanger des données entre ton navigateur et un site web.

### 🔐 La différence principale ? La sécurité.
- **HTTP** = non sécurisé → données transmises en clair  
- **HTTPS** = sécurisé → données chiffrées via certificat SSL

### 📦 Exemple
Connexion à un site bancaire :
- **HTTP** : tes identifiants peuvent être piratés.
- **HTTPS** : tes données sont protégées.

### 🔒 Comment savoir si un site est sécurisé ?
- L’URL commence par `https://`
- Un cadenas 🔒 est affiché dans la barre d’adresse

---

## 2. Fonctionnement de base d’une requête et réponse HTTP

### ⚙️ Comment ça marche ?
1. Ton navigateur envoie une **requête HTTP** au serveur
2. Le serveur renvoie une **réponse HTTP**

### 📫 Structure d’une requête HTTP

```http
GET /index.html HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
```

### 📦 Structure d’une réponse HTTP

```http
HTTP/1.1 200 OK
Content-Type: text/html

<html>...</html>
```

## 3. Méthodes HTTP et codes de statut

### ✋ Méthodes HTTP principales

| Méthode | Usage courant                          |
|---------|----------------------------------------|
| GET     | Récupérer une ressource                |
| POST    | Envoyer des données                    |
| PUT     | Modifier ou remplacer une ressource    |
| DELETE  | Supprimer une ressource                |
| PATCH   | Modifier partiellement une ressource   |


### 🧠 Exemples

```http
GET /produits/123       → Voir le produit 123
POST /produits          → Créer un nouveau produit
DELETE /produits/123    → Supprimer ce produit
```

### 🧾 Qu’est-ce qu’un code de statut HTTP ?

| Classe | Signification     | Exemple             |
|--------|-------------------|---------------------|
| 1xx    | Information       | En traitement       |
| 2xx    | Succès            | OK                  |
| 3xx    | Redirection       | Aller ailleurs      |
| 4xx    | Erreur client     | Mauvaise requête    |
| 5xx    | Erreur serveur    | Serveur en échec    |

---

### 🔵 1xx – Informations

| Code | Signification         | Explication                                               |
|------|-----------------------|-----------------------------------------------------------|
| 100  | Continue              | Le client peut continuer à envoyer la requête            |
| 101  | Switching Protocols   | Le serveur accepte un changement de protocole            |
| 102  | Processing            | Traitement long en cours                                  |

> 🧠 Le serveur dit « J’ai bien reçu, continue ! »

### 🟢 2xx – Succès

| Code | Signification     | Explication                                               |
|------|-------------------|-----------------------------------------------------------|
| 200  | OK                | Tout s’est bien passé                                     |
| 201  | Created           | Nouvelle ressource créée (ex : après un POST)            |
| 202  | Accepted          | Traitement accepté mais non terminé                      |
| 204  | No Content        | Réussite, mais aucune donnée à renvoyer                  |

> 🧠 Le serveur te fait un pouce en l’air 👍

---

### 🟡 3xx – Redirections

| Code | Signification          | Explication                                                 |
|------|------------------------|-------------------------------------------------------------|
| 301  | Moved Permanently      | Ressource déplacée définitivement                          |
| 302  | Found                  | Déplacement temporaire                                      |
| 303  | See Other              | Redirection vers une autre ressource via GET               |
| 304  | Not Modified           | La version en cache peut être utilisée                     |
| 307  | Temporary Redirect     | Redirection temporaire stricte (méthode inchangée)         |

> 🧠 Le serveur t’indique une nouvelle direction avec un panneau 🪧

---

### 🔴 4xx – Erreurs client

| Code | Signification         | Explication                                        |
|------|-----------------------|----------------------------------------------------|
| 400  | Bad Request           | Syntaxe de requête invalide                        |
| 401  | Unauthorized          | Authentification requise                           |
| 403  | Forbidden             | Accès refusé, même authentifié                     |
| 404  | Not Found             | Ressource inexistante                              |
| 405  | Method Not Allowed    | Méthode HTTP non autorisée                         |
| 408  | Request Timeout       | Requête trop lente                                 |
| 429  | Too Many Requests     | Trop de requêtes envoyées                          |

> 🧠 C’est toi qui t’es trompé ou tu n’as pas les permissions.

---

### 🔥 5xx – Erreurs serveur

| Code | Signification               | Explication                                               |
|------|-----------------------------|-----------------------------------------------------------|
| 500  | Internal Server Error       | Erreur interne du serveur                                 |
| 501  | Not Implemented             | Fonction non implémentée                                  |
| 502  | Bad Gateway                 | Mauvaise réponse d’un autre serveur                       |
| 503  | Service Unavailable         | Serveur indisponible (maintenance, surcharge...)          |
| 504  | Gateway Timeout             | Pas de réponse d’un serveur intermédiaire                 |
| 505  | HTTP Version Not Supported  | Version HTTP non reconnue                                 |

> 🧠 Cette fois, c’est le serveur qui a un souci 🤒🔧

## 4. curl : outil en ligne de commande

### Qu'est-ce que curl ?

`curl` (Client URL) est un outil en ligne de commande permettant de faire des requêtes HTTP (et autres) vers des URLs.

Il est très utilisé pour :

- Tester des APIs REST
- Envoyer ou recevoir des données en JSON
- Automatiser des appels réseau depuis des scripts


### 📥 Exemple basique : GET

```bash
curl https://jsonplaceholder.typicode.com/posts/1
```

### 📤 Exemple : POST avec données

```bash
curl -X POST https://jsonplaceholder.typicode.com/posts \
-H "Content-Type: application/json" \
-d '{"title": "Hello", "body": "Bonjour monde", "userId": 1}'
```

> - `-X POST` : méthode utilisée  
> - `-H` : en-tête HTTP (ici, JSON)  
> - `-d` : données à envoyer


### 👀 Voir les en-têtes de la réponse

```bash
curl -I https://jsonplaceholder.typicode.com/posts/1
```

> `-I` (majuscule) → affiche uniquement les en-têtes HTTP

---

### 🔎 Lire une réponse API

Quand tu fais une requête, tu obtiens :

- ✅ Un **code de statut** (ex : `200`, `404`, `500`…)
- 🧾 Un **corps de réponse** (souvent au format JSON)
- 🧠 Des **en-têtes HTTP** (informations techniques)

### 🔎 Exemple de sortie API (GET)

```json
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat",
  "body": "quia et suscipit suscipit..."
}
```

> ➡️ C’est un article lié à `userId: 1`, et tout va bien si le code est `200`.

### ❌ Exemple d’erreur

```bash
curl https://jsonplaceholder.typicode.com/doesnotexist
```

**Réponse :**

```http
HTTP/1.1 404 Not Found
```

> ➡️ Cela signifie que la ressource demandée n’existe pas.
