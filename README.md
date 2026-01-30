Replication of PyArmor segmentation fault in hashing objects.

Please install `uv` to replicate the experiment. After installing `uv`, you can run:

```
./replicate.sh
```

to get the result like following:

```
> ./replicate.sh 
Trial  1: frame.f_code: <code object func at 0x7776cf78c370, file "<frozen pyarmor_segv>", line 5>
co_name: func
Computing hash(frame.f_code)...: -3915728441605713561
Success
Normal ✓
Trial  2: frame.f_code: <code object func at 0x7251b5ec8370, file "<frozen pyarmor_segv>", line 5>
co_name: func
SEGFAULT ✗
Trial  3: frame.f_code: <code object func at 0x764dbfd10370, file "<frozen pyarmor_segv>", line 5>
co_name: func
SEGFAULT ✗
Trial  4: frame.f_code: <code object func at 0x733c5db98370, file "<frozen pyarmor_segv>", line 5>
co_name: func
Computing hash(frame.f_code)...: -1940020248159428493
Success
Normal ✓
Trial  5: frame.f_code: <code object func at 0x7b56701c8370, file "<frozen pyarmor_segv>", line 5>
co_name: func
SEGFAULT ✗
Trial  6: frame.f_code: <code object func at 0x7b871eb74370, file "<frozen pyarmor_segv>", line 5>
co_name: func
Computing hash(frame.f_code)...: -5207489521542538451
Success
Normal ✓
Trial  7: frame.f_code: <code object func at 0x7f8314848370, file "<frozen pyarmor_segv>", line 5>
co_name: func
SEGFAULT ✗
Trial  8: frame.f_code: <code object func at 0x735fb1d6c370, file "<frozen pyarmor_segv>", line 5>
co_name: func
SEGFAULT ✗
Trial  9: frame.f_code: <code object func at 0x74676b578370, file "<frozen pyarmor_segv>", line 5>
co_name: func
SEGFAULT ✗
Trial 10: frame.f_code: <code object func at 0x72a01b358370, file "<frozen pyarmor_segv>", line 5>
co_name: func
SEGFAULT ✗
```
