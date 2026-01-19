````markdown
# Coin Collector 🎮

Ein kleines 2D-Spiel mit **pygame**, bei dem eine Spielfigur Münzen einsammelt und Hindernissen ausweicht.  
Level werden über **JSON** definiert und mit **pydantic** validiert.  
Der Start erfolgt über eine **CLI mit typer**.

---

## Voraussetzungen
- Python 3.11+
- uv installiert

---

## Projekt starten

Zuerst sicherstellen, dass alle Abhängigkeiten installiert sind:

```bash
uv sync
````

### Spiel mit Beispiel-Level starten

```bash
uv run -m coin_collector --level src/coin_collector/levels/level_example.json
```

### Spiel mit eigenem Level starten

```bash
uv run -m coin_collector --level src/coin_collector/levels/jakob_level.json --fps 60 --debug
```

---

## Steuerung

* **Pfeiltasten / WASD**: Spieler bewegen
* **ESC**: Spiel beenden
* **Fenster schließen (X)**: Spiel beenden

---

## Spielziel

* Sammle alle Münzen ein
* Weiche Hindernissen aus
* Wenn alle Münzen gesammelt sind, erscheint eine Meldung im Fenstertitel

---

## Tests (optional)

```bash
uv run pytest
```

---

## Code-Qualität (optional)

```bash
uv run ruff check src tests
```

```
```
