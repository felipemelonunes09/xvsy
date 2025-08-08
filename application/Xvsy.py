
from __future__ import annotations

import pygame

from application.objects.Table import Table
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

    def current(self) -> GameState.State:
        return self.__state 

    def next(self):
        match self.__state:
            case GameState.State.START:
                self.__state = GameState.State.PLAYER_TURN

class Xvsy(GameInstance):

    def update(self):
        match self.gameState.current():
            case GameState.State.START:
                self.gameState.next()
            case GameState.State.PLAYER_TURN:
                if self.runeDeck.isClikedAndConsume():
                    newRune = self.runeDeck.next()
                    self.getEngine().startDrag(cursorSprite=newRune, payload={"rune": newRune})
                    self.getSprites().add(newRune)

                if self.player.getRuneFrame().hasDroppedRune():
                    self.gameState.next()

    def setup(self):
 
        self.runeDeck   = RuneDeck(position=(50, 300))
        self.gameState  = GameState()

        self.player     = Player(lowerDeckPosition=(125, 500))
        #self.enemy      = Enemy()
        self.table      = Table()

        self.addSprite(self.table)
        self.addSprite(self.runeDeck).addSprite(self.player)

        self.engine.setBackground(pygame.image.load(Configuration.engine_assets_dir / 'images' / 'background.png'))

