from flask import Flask, jsonify, request
from cartes import Carte, Paquet
from jeu import *

app = Flask(__name__)
game = Jeu()  # Instance de votre jeu

@app.route('/start_game', methods=['POST'])
def start_game():
    data = request.json
    nb_joueurs = data.get('nb_joueurs', 4)  # Nombre de joueurs par défaut à 4
    game.start_game(nb_joueurs)  # Initialiser le jeu avec le nombre de joueurs
    return jsonify({"message": "Le jeu a commencé", "status": "success"})

@app.route('/get_hand/<int:joueur_id>', methods=['GET'])
def get_hand(joueur_id):
    hand = game.get_hand(joueur_id)
    hand_data = [str(carte) for carte in hand]
    return jsonify({"hand": hand_data})

@app.route('/play_card', methods=['POST'])
def play_card():
    data = request.json
    joueur_id = data.get('joueur_id')
    card_index = data.get('card_index')
    result = game.play_card(joueur_id, card_index)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
