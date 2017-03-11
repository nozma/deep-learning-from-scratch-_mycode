import nand_gate, or_gate, and_gate

def XOR(x1, x2):
    s1 = nand_gate.NAND(x1, x2)
    s2 = or_gate.OR(x1, x2)
    y = and_gate.AND(s1, s2)
    return y

for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
    y = XOR(xs[0], xs[1])
    print(str(xs) + ' -> ' + str(y))
