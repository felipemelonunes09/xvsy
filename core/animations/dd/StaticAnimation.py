import pygame


class StaticAnimation:
    def __init__(self, sprite: pygame.sprite.Sprite, targetPosition: tuple[int, int], speed: float):
        self.__sprite = sprite
        self.__targetPosition = pygame.Vector2(targetPosition)
        self.__finished = False
        self.__started = False
        self.__speed = float(speed)

        print(self.__getSpritePos())
        print(self.__targetPosition)



    def start(self) -> None:
        self.__started = True
        self.__finished = False

    def reset(self, targetPosition: tuple[int, int] | None = None, speed: float | None = None) -> None:
        if targetPosition is not None:
            self.__targetPosition = pygame.Vector2(targetPosition)
        if speed is not None:
            self.__speed = float(speed)
        self.__started = False
        self.__finished = False

    def isFinished(self) -> bool:
        return self.__finished

    def update(self, dt: float) -> None:
        if not self.__started or self.__finished:
            return

        pos = self.__getSpritePos()
        if pos is None:
            self.__finished = True
            return

        pos_v = pygame.Vector2(pos)
        vec = self.__targetPosition - pos_v
        dist = vec.length()
        if dist <= 1e-3:
            self._set_sprite_pos(self.__targetPosition)
            self.__finished = True
            return

        step = self.__speed * dt
        if step >= dist:
            self.__setSpritePos(self.__targetPosition)
            self.__finished = True
        else:
            newpos = pos_v + vec.normalize() * step
            print(newpos)
            self.__setSpritePos(newpos)

    def __getSpritePos(self) -> tuple[float, float] | None:
        s = self.__sprite
        if hasattr(s, "rect"):
            return float(s.rect.x), float(s.rect.y)
        if hasattr(s, "position"):
            p = s.position
            if isinstance(p, (tuple, list)):
                return float(p[0]), float(p[1])
            try:
                return float(p.x), float(p.y)
            except Exception:
                return None
        if hasattr(s, "x") and hasattr(s, "y"):
            return float(s.x), float(s.y)
        return None

    def __setSpritePos(self, pos: pygame.Vector2 | tuple[float, float]) -> None:
        x, y = int(pos[0]), int(pos[1])
        s = self.__sprite
        if hasattr(s, "rect"):
            s.rect.topleft = (x, y)
            return
        if hasattr(s, "position"):
            if isinstance(s.position, pygame.math.Vector2):
                s.position.x = x
                s.position.y = y
            else:
                s.position = (x, y)
            return
        if hasattr(s, "x") and hasattr(s, "y"):
            s.x = x
            s.y = y
            return


