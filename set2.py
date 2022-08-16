l = [1, 2, 'a', list(range(10)), 'z', (1, 2), {'AA', 'BB'}, 3.67]

# s_simple = set()
# for e in l:
    # if not isinstance(e, (list, set, dict)):
        # s_simple.add(e)

s_simple = {e for e in l if not isinstance(e, (list, set, dict))}


s_full = set()
for e in l:
    if isinstance(e, (list, set, dict)):
        s_full.update(e)
    else:
        s_full.add(e)
