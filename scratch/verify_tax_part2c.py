import json, sys
sys.stdout.reconfigure(encoding='utf-8')

tax = json.load(open('taxonomy_3tier.json', encoding='utf-8'))

part2c_tasks = [
    ('arc202_c', 'Number Theory', 'Multiplicative Functions', 'Mobius Function and Mobius Inversion'),
    ('abc215_g', 'Math', 'Probabilities and Expected Values', 'Probabilities and Expected Values'),
    ('arc175_d', 'Basics', 'Greedy and Constructive', 'Basic Constructive Algorithms'),
    ('abc143_f', 'Basics', 'Leveraging Monotonicity', 'Binary Search'),
    ('abc273_f', 'Dynamic Programming (DP)', 'Classic DP', 'Interval DP / Range DP / Matrix Chain Multiplication (MCM)'),
    ('arc052_c', 'Graph Theory', 'Shortest Paths', "Dijkstra's Algorithm"),
    ('arc080_c', 'Data Structures (DS)', 'Segment Tree', 'Segment Tree (Point Update Range Query)'),
    ('arc227_d', 'Graph Theory', 'Satisfiability', '2 SAT'),
    ('abc276_g', 'Basics', 'Basic Counting', 'Stars and Bars'),
    ('arc170_d', 'Game Theory', 'Grundy Number / Nim', 'Grundy Number and Basic Game Theory'),
    ('abc474_g', 'Graph Theory', 'Hamiltonian Path', 'Hamiltonian Path and Cycle'),
    ('abc150_f', 'Strings', 'String Matching', 'Knuth Morris Pratt (KMP) and Prefix Automaton'),
    ('arc223_d', 'Math', 'Probabilities and Expected Values', "Gambler's Ruin"),
    ('arc151_d', 'Math', 'Convolution', 'Fast Walsh Hadamard Transform (FWHT) and its Variations'),
    ('codefestival_2016_qualC_d', 'Dynamic Programming (DP)', 'Classic DP', 'Edit Distance'),
    ('agc032_c', 'Graph Theory', 'Eulerian Path', 'Eulerian Path and Cycle')
]

all_ok = True
for pid, d, s, t in part2c_tasks:
    if d not in tax:
        print(f"FAILED Domain: {d} for {pid}")
        all_ok = False
        continue
    if s not in tax[d]:
        print(f"FAILED Subtopic: {s} in {d} for {pid}")
        all_ok = False
        continue
    topics = [item[1] for item in tax[d][s]]
    if t not in topics:
        print(f"FAILED Topic: {t} in {d} > {s} for {pid}")
        all_ok = False
    else:
        print(f"[OK] {pid:25} -> {d} > {s} > {t}")

if all_ok:
    print("\nALL 16 TAXONOMY MAPPINGS ARE 100% VALID!")
