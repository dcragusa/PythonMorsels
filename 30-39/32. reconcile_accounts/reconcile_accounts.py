from collections import defaultdict, deque
from datetime import date, timedelta

one_day = timedelta(days=1)


def match_transactions(p1, t1, p2, t2):
    for t in sorted(p1):
        while p1[t]:
            idx1 = p1[t].popleft()
            if len(t1[idx1]) > 4:
                # we have already processed this transaction and added FOUND/MISSING
                continue
            match = False
            for t_day in [(t[0] - one_day, *t[1:]), t, (t[0] + one_day, *t[1:])]:
                if t_day in p2 and p2[t_day]:
                    t1[idx1].append('FOUND')
                    idx2 = p2[t_day].popleft()
                    t2[idx2].append('FOUND')
                    match = True
                    break
            if not match:
                t1[idx1].append('MISSING')


def reconcile_accounts(t1, t2):
    positions1, positions2 = defaultdict(deque), defaultdict(deque)
    for idx, t in enumerate([(date.fromisoformat(t[0]), *t[1:]) for t in t1]):
        positions1[t].append(idx)
    for idx, t in enumerate([(date.fromisoformat(t[0]), *t[1:]) for t in t2]):
        positions2[t].append(idx)

    match_transactions(positions1, t1, positions2, t2)
    match_transactions(positions2, t2, positions1, t1)

    return t1, t2
