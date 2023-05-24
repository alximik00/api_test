import math
def transform(input, metadata):
  r_dict = r.json()
  a_mult = r.get('a_mult', 0)
  return { 'product': input.get('a', 0) * a_mult }