
import pytest
from coin_collector.config import load_level


def test_invalid_level_raises_error(tmp_path):
    bad_level = tmp_path / "bad.json"
    bad_level.write_text(
        '{"width": "groß", "height": 600, "player_start": [0,0], "coins": [], "walls": []}'
    )

    with pytest.raises(ValueError):
        load_level(str(bad_level))
