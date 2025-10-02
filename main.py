from core.Bootstrap import Bootstrap
from core.Engine import Engine
from application.Xvsy import Xvsy

if __name__ == "__main__":
    engine = Engine(Bootstrap().__config__(), Xvsy())
    engine.run()