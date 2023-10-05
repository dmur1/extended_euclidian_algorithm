def eea(r0, r1):
    assert(r0 > r1)

    s0 = 1
    s1 = 0
    t0 = 0
    t1 = 1
    i = 1

    while True:
        i = i + 1
        r = r0 % r1
        if r == 0:
            break
        q = (r0 - r) // r1
        s = s0 - (q * s1)
        t = t0 - (q * t1)

        r0 = r1
        r1 = r
        s0 = s1
        s1 = s
        t0 = t1
        t1 = t

        print(f"i: {i} r: {r1} q: {q} s: {s1} t: {t1}")

    return r1, s1, t1

def test_eea(r0, r1):
    r, s, t = eea(r0, r1)
    assert((s * r0 + t * r1) == r)
    print((r, s, t))

test_eea(67, 12)        # (2, -5, 28)
test_eea(243, 198)      # (18, 9, -11)
test_eea(3587, 1819)    # (34, -36, 71)

