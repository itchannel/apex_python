import sys, os
from apex import Apex

test = Apex(sys.argv[1], sys.argv[2], sys.argv[3])

test.auth()

print(test.status())