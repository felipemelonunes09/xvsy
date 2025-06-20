from pathlib import Path

class Configuration:
    
    engine_version: int 
    engine_fps: int
    engine_resolution: tuple[int, int]

    engine_PATH: Path
    engine_assets_dir: Path

    game_context_title: str
    game_style_frame_offset: int

    __loaded__: bool = False

    def load(self, configObject: dict[str, any], workingPath: Path):
        Configuration.engine_version            = configObject["engine"]["version"]
        Configuration.engine_fps                = configObject["engine"]["fps"]
        Configuration.engine_resolution         = tuple(configObject["engine"]["resolution"])
        Configuration.engine_PATH               = workingPath
        Configuration.engine_assets_dir         = workingPath / 'assets'
        Configuration.game_style_frame_offset   = 150
        Configuration.__loaded__                = True    

