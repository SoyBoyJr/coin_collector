
import typer
from .game import run_game

app = typer.Typer(help="Coin Collector – Einfaches 2D-Sammelspiel")


@app.command()
def play(
    level: str = typer.Option(..., help="Pfad zur Level-JSON"),
    fps: int = typer.Option(60, help="Frames pro Sekunde"),
    debug: bool = typer.Option(False, help="Debug-Kollisionen anzeigen"),
):
    run_game(level_path=level, fps=fps, debug=debug)


if __name__ == "__main__":
    app()

