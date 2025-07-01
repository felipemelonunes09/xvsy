
import pygame

from application.entities.Enemy import Enemy
from application.objects.Table import Table
from application.scene.LowerDeck import LowerDeck
from core.Engine import GameInstance
from application.objects.RuneDeck import RuneDeck
from application.entities.Player import Player
from config.Configuration import Configuration

class GameState:
    class State:
        START           ="[gamestate].running"
        PLAYER_TURN     ="[gamestate].player.turn"
        ENEMY_TURN      ="[gamestate].enemy.turn"
        ENDGAME         ="[gamestate].endgame"

    def __init__(self):
        self.__state = GameState.State.START

    def current(self):
        pass

    def next(self):
        pass

class Xvsy(GameInstance):

    def update(self):
        match self.gameState.current():
            case GameState.State.START:
                self.runeDeck.shuffle()
            case GameState.State.PLAYER_TURN:
                self.player.update()
            case GameState.State.ENEMY_TURN:
                self.enemy.update()

        self.gameState.next()

    def setup(self):

        self.runeDeck   = RuneDeck(position=(50, 300))
        self.gameState  = GameState()

        self.player     = Player()
        self.enemy      = Enemy()
        self.table      = Table()

        self.getSprites().add(self.table)
        self.getSprites().add(self.runeDeck)
        self.engine.setBackground(pygame.image.load(Configuration.engine_assets_dir / 'images' / 'background.png'))

