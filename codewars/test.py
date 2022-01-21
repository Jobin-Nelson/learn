def accum(s):
    return '-'.join([c.upper() + c*i for i, c in enumerate(s.lower())])
