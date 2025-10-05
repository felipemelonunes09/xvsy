
from __future__ import annotations

import random
import pygame

from application.Actions import Actions
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
        START                   ="[gamestate].running"
        TURN                    ="[gamestate].turn"
        CHANGE                  ="[gamestate].change"
        ENDGAME                 ="[gamestate].endgame"

        __getCardFromRuneDeck__ = "[gamestate].__getCardFromRuneDeck__"

    def __init__(self):
        self.__state = GameState.State.START

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
        self.__runeDeckAnimation = None


    def update(self):

        match self.gameState.current():
            case GameState.State.START:
                self.gameState.next()
                self.currentEntity = self.player if random.choice([True, False]) else self.enemy
                print(f"First player is {self.currentEntity}")   

            case GameState.State.TURN:
                action = self.currentEntity.turn()
                self.allowEventsIfPlayer()
                if (action == Actions.GET_CARD_FROM_RUNE_DECK):
                    self.currentEntity.getRuneCardFromDeck()
                    if (self.currentEntity == self.enemy):
                        card = self.runeDeck.next()
                        position = self.enemy.addRune(card)
                        self.dealCardForEnemyRuneFrame(position)

                if self.currentEntity.getMana() == 0:
                    self.gameState.next()

            case GameState.State.CHANGE:
                self.currentEntity.refillMana()
                self.currentEntity = self.enemy if self.currentEntity == self.player else self.player
                self.gameState.next()
                    
            case GameState.State.__getCardFromRuneDeck__:
                if self.__runeDeckAnimation is None:
                    self.dealCardForEnemyRuneFrame(4)
                    self.__runeDeckAnimation = True

    def dealCardForEnemyRuneFrame(self, position: tuple[int, int]):
        card = PlainCard(position=(100, 300), scale=Configuration.card_scale)
        animation = StaticAnimation(card, targetPosition=position, speed=500)
        self.startAnimation(animation)
        self.addSprite(card)

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

