def aggregate(*args, **kwargs):
  dict = {}
  for w in args:
    dict[w] = dict.get(w, 0) + 1
  for w, f in kwargs.items():
    dict[w] = dict.get(w, 0) + f
  return dict

print(aggregate())
print(aggregate(a=5, b=10, d=4))
print(aggregate('a', 'b', 'c', 'b', 'c'))
print(aggregate('a', 'b', 'c', 'b', 'c', a=5, b=10, d=4))