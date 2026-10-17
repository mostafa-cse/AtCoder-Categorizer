import json, sys
sys.stdout.reconfigure(encoding='utf-8')

tax = json.load(open('taxonomy_3tier.json', 'r', encoding='utf-8'))

checks = [
    ('arc047_c', 'Miscellaneous', 'General', 'Factorial Number System'),
    ('abc400_f', 'Dynamic Programming (DP)', 'Classic DP', 'Interval DP / Range DP / Matrix Chain Multiplication (MCM)'),
    ('abc311_g', 'Data Structures (DS)', 'Monotonic Data Structures', 'Monotonic Stack: All Nearest Smaller Values and All Subarray Maximum/Minimum'),
    ('arc154_d', 'Miscellaneous', 'Interactive Problems', 'Interactive Problems'),
    ('agc014_d', 'Game Theory', 'Graph Games', '[Problem] Matching Game On A Graph'),
    ('discovery_2016_final_c', 'Dynamic Programming (DP)', 'Dp on Different Structures', 'DP on Trees and DAGs'),
    ('arc004_4', 'Basics', 'Basic Counting', 'Stars and Bars'),
    ('arc231_c', 'Geometry', 'Euclidean Geometry', 'Euclidean Geometry'),
    ('abc242_f', 'Combinatorics', 'Inclusion Exclusion', 'Principle of Inclusion and Exclusion (PIE)'),
    ('abc443_g', 'Number Theory', 'Floor Sum', 'Floor Sum and Mod Sum of Arithmetic Progression'),
    ('m_solutions2020_e', 'Dynamic Programming (DP)', 'Bit Related DP', 'Bitmask DP'),
    ('abc245_g', 'Graph Theory', 'Shortest Paths', "Dijkstra's Algorithm"),
    ('arc131_d', 'Basics', 'More Techniques', 'Difference Array'),
    ('abc432_f', 'Dynamic Programming (DP)', 'Bit Related DP', 'Bitmask DP'),
    ('arc190_b', 'Combinatorics', 'Factorials and Binomial Coefficients (nCr)', 'Prefix Sum Queries of Binomial Coefficients'),
    ('abc196_f', 'Math', 'Convolution', 'Number Theoretic Transform (NTT)')
]

all_ok = True
for pid, dom, sub, top in checks:
    if dom not in tax:
        print(f"Domain not found: {dom}")
        all_ok = False
        continue
    if sub not in tax[dom]:
        print(f"Subtopic not found: {sub} in {dom}")
        all_ok = False
        continue
    topics = [item[1] for item in tax[dom][sub]]
    if top not in topics:
        print(f"Topic not found: {top} in {dom} > {sub}")
        all_ok = False
        continue
    print(f"[OK] {pid}: {dom} > {sub} > {top}")

if all_ok:
    print("\nALL 16 PROBLEMS 100% COMPLIANT WITH TAXONOMY!")
