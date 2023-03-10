# duplicates should be 'True'
import sys
from pylint import lint

DUPLICATES = False

run = lint.Run(["dupesuggestions.py"], do_exit=False)

duplicates = run.linter.check("dupesuggestions")

if duplicates == DUPLICATES:
    print("Linter failed: The file does NOT contain duplicates!")
else:
    print("Linter passed: The file DOES contain duplicates!")
    sys.exit(1)

sys.exit(0)
