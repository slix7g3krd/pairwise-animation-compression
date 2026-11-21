import pytest
import math
from render import animation_compression as mod

CASES = [
    ("quat", 'm.quat_normalize(2, 0, 0, 0) == approx((1.0, 0.0, 0.0, 0.0))'),
    ("arc", 'm.arc_error(1, 1) == 0'),
    ("keep", 'm.keep_count([0.1, 0.9, 0.2], 0.5) == 2'),
    ("root", 'm.root_track("root") is True'),
    ("resample", 'm.resample_count(2, 30) == 60'),
    ("bits", 'm.scale_bits(16) == 16'),
    ("loop", 'm.loop_aligned(1, 1) is True'),
    ("event", 'm.event_kept(5, [5, 7]) is True'),
    ("precision", 'm.shared_precision([8, 12, 16]) == 16'),
    ("path", 'm.decode_path("pc") == "fixed"'),
    ("budget", 'm.segment_budget(120, 3) == 40'),
    ("time", 'm.sample_time(30, 30) == approx(1.0)'),
    ("lerp", 'm.lerp(0, 10, 0.5) == approx(5.0)'),
    ("key", 'm.anim_key(3, 2) == "3:2"'),
    ("ratio", 'm.ratio(100, 25) == approx(4.0)')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
