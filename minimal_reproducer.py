import sys
from pathlib import Path
from pyarmor_segv import func  # pyright: ignore[reportMissingImports]

try:
    func(Path('empty'))
except ValueError:
    # Get the obfuscated function's frame
    tb = sys.exc_info()[2].tb_next  # type: ignore
    frame = tb.tb_frame  # type: ignore
    code = frame.f_code
    print(f"frame.f_code: {code}")
    print(f"co_name: {code.co_name}")
    print(f"Computing hash(frame.f_code)...: {hash(code)}")
    print("Success")
