

def solve(value):
    return [list(row) for row in zip(*value)] if len({len(row) for row in value}) <= 1 else (_ for _ in ()).throw(ValueError("ragged matrix"))
