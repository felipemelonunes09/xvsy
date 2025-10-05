
from __future__ import annotations

import random
import pygame

from application.entities.TableEntity import TableEntity
from application.entities.Enemy import Enemy
from application.objects.Table import Table
from application.objects.cards.Card import PlainCard
from core.Engine import GameInstance
from application.objects.RuneDeck import RuneDeck
from application.entities.Player import Player
from config.Configuration import Configuration
from core.events.EngineClick import EngineClick
from core.events.EventFunctionManager import Event
from core.animations.dd.StaticAnimation import StaticAnimation

class GameState:
    class State:
        START           ="[gamestate].running"
        TURN            ="[gamestate].turn"
        CHANGE          ="[gamestate].change"
        ENDGAME         ="[gamestate].endgame"
        __testint_animation_01__ = "[gamestate].__testint_animation_01"

    def __init__(self):
        self.__state = GameState.State.__testint_animation_01__

    def current(self) -> GameState.State:
        return self.__state 

    def next(self):
        previous = self.__state
        match self.__state:
            case GameState.State.START:
                self.__state = GameState.State.TURN
            case GameState.State.TURN:
                self.__state = GameState.State.CHANGE
            case GameState.State.CHANGE:
                self.__state = GameState.State.TURN

        print(f"GameState: {previous} -> {self.__state}")

class Xvsy(GameInstance):

    def __init__(self):
        super().__init__()
        self.currentEntitys: TableEntity = None
        self._animation: StaticAnimation | None = None
        self._last_time = pygame.time.get_ticks()

    def update(self):

        match self.gameState.current():
            case GameState.State.START:
                self.gameState.next()
                self.currentEntity = self.player if random.choice([True, False]) else self.enemy
                self.currentEntity = self.player
                print(f"First player is {self.currentEntity}")   
            case GameState.State.TURN:
                self.currentEntity.turn()
                self.allowEventsIfPlayer()

                if self.currentEntity.getMana() == 0:
                    self.gameState.next()
            case GameState.State.CHANGE:
                self.currentEntity.refillMana()
                self.currentEntity = self.enemy if self.currentEntity == self.player else self.player
                self.gameState.next()
                    
            case GameState.State.__testint_animation_01__:
                if self._animation is None:
                    anim = PlainCard(position=(100, 300), scale=Configuration.card_scale)
                    self._animation = StaticAnimation(anim, targetPosition=(600, 300), speed=400.0)
                    self.addAnimation(self._animation)
                    self._animation.start()
                    self.addSprite(anim)

    def allowEventsIfPlayer(self):
        if self.currentEntity == self.player:
            if self.runeDeck.isClikedAndConsume():
                newRune = self.runeDeck.next()
                self.getEngine().startDrag(cursorSprite=newRune, payload={"rune": newRune})
                self.getSprites().add(newRune)

    def setup(self):
 
        self.runeDeck   = RuneDeck(position=(50, 300))
        self.gameState  = GameState()

        self.player     = Player(lowerDeckPosition=(125, 500), cardHandPosition=(125, 675))
        self.enemy      = Enemy(lowerDeckPosition=(125, 50), cardHandPosition=(125, -50))
        self.table      = Table()

        self.addSprite(self.table)
        self.addSprite(self.runeDeck).addSprite(self.player).addSprite(self.enemy)

        self.engine.setBackground(pygame.image.load(Configuration.engine_assets_dir / 'images' / 'background.png'))

