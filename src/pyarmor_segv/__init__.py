# No PyArmor Protection Code
from pathlib import Path


def func(root: Path):
    it = iter(root.glob("*.txt"))
    try:
        next(it)
    except StopIteration:
        raise ValueError from None
