
from pathlib import Path
from pydantic import BaseModel, Field, ValidationError
from typing import List, Tuple
import json


class Coin(BaseModel):
    x: int
    y: int
    r: int = Field(gt=0)


class Wall(BaseModel):
    x: int
    y: int
    w: int = Field(gt=0)
    h: int = Field(gt=0)


class LevelConfig(BaseModel):
    width: int = Field(gt=0)
    height: int = Field(gt=0)
    player_start: Tuple[int, int]
    coins: List[Coin]
    walls: List[Wall]


def load_level(path: str) -> LevelConfig:
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        return LevelConfig(**data)
    except ValidationError as e:
        raise ValueError(f"Ungültige Level-Datei:\n{e}") from e

