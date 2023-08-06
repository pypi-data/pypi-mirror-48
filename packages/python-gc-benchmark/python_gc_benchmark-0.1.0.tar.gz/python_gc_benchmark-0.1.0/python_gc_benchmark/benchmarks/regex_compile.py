
"""Benchmark how quickly Python's regex implementation can compile regexes.

We bring in all the regexes used by the other regex benchmarks, capture them by
stubbing out the re module, then compile those regexes repeatedly. We muck with
the re module's caching to force it to recompile every regex we give it.
"""

# Python imports
import re

# Local imports
from six.moves import xrange


def capture_regexes():
    regexes = []

    real_compile = re.compile
    real_search = re.search
    real_sub = re.sub

    def capture_compile(regex, flags=0):
        regexes.append((regex, flags))
        return real_compile(regex, flags)

    def capture_search(regex, target, flags=0):
        regexes.append((regex, flags))
        return real_search(regex, target, flags)

    def capture_sub(regex, *args):
        regexes.append((regex, 0))
        return real_sub(regex, *args)

    re.compile = capture_compile
    re.search = capture_search
    re.sub = capture_sub
    try:
        import bm_regex_effbot
        bm_regex_effbot.bench_regex_effbot(1)

        import bm_regex_v8
        bm_regex_v8.bench_regex_v8(1)
    finally:
        re.compile = real_compile
        re.search = real_search
        re.sub = real_sub
    return regexes


def run_regex_compile(loops, regexes):
    range_it = xrange(loops)

    for _ in range_it:
        for regex, flags in regexes:
            re.purge()
            # ignore result (compiled regex)
            re.compile(regex, flags)


if __name__ == "__main__":
    regexes = capture_regexes()
    run_regex_compile(20, regexes)
