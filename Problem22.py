# http://projecteuler.net/problem=22

filename = "Problem22.txt"

def score(name):
  return sum([ord(x) - ord('A') + 1 for x in name])

with open(filename) as f:
  names = f.read()
  names = names.translate(None, "\"\n")
  names = sorted(names.split(","))
  s = 0
  for i, name in enumerate(names):
    s += score(name) * (i + 1)

print s
