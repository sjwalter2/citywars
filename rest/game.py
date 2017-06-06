from flask import Flask, jsonify, abort
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.game import GameSetup, Game, STATUS

app = Flask(__name__)

game = None

@app.route("/game/start")
def start():
	global game
	if game == None or game.getStatus() == STATUS.STOPPED:
		gameSetup = GameSetup(7, 7, 4)
		game = Game(gameSetup)
	return game.start()

@app.route("/game/stop")
def stop():
	validateGameStatus()
	return game.stop()

@app.route("/game/pause")
def pause():
	validateGameStatus()
	return game.pause()

@app.route("/game/resume")
def resume():
	validateGameStatus()
	return game.resume()

@app.route("/game/map")
def getMap():
	validateGameStatus()
	return jsonify(game.getMap().toJSON())

@app.route("/game")
def getGame():
	validateGameStatus()
	return jsonify(game.toJSON())

@app.route("/game/logs")
def getLogs():
	validateGameStatus()
	return jsonify(game.getLogs().toJSON())

def validateGameStatus():
	if game == None:
		print('Game not started')
		abort(400) # Bad Request

if __name__ == "__main__":
  app.run()