import json, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('taxonomy_3tier.json', 'r', encoding='utf-8') as f:
    tax = json.load(f)

candidates = [
    {
        "id": "abc314_g",
        "domain": "Basics",
        "subtopic": "Standard Template Library (STL)",
        "topic": "Priority Queue / Heap"
    },
    {
        "id": "arc211_d",
        "domain": "Graph Theory",
        "subtopic": "Graph Traversal",
        "topic": "Topological Sorting"
    },
    {
        "id": "arc229_f",
        "domain": "Combinatorics",
        "subtopic": "Techniques",
        "topic": "Contribution Technique"
    },
    {
        "id": "abc281_g",
        "domain": "Graph Theory",
        "subtopic": "Graph Counting",
        "topic": "Counting Labeled Graphs"
    },
    {
        "id": "abc379_g",
        "domain": "Miscellaneous",
        "subtopic": "General",
        "topic": "Broken Profile DP / Plug DP"
    },
    {
        "id": "arc159_c",
        "domain": "Basics",
        "subtopic": "Greedy and Constructive",
        "topic": "Basic Constructive Algorithms"
    },
    {
        "id": "abc234_g",
        "domain": "Data Structures (DS)",
        "subtopic": "Segment Tree",
        "topic": "Segment Tree with Lazy Propagation"
    },
    {
        "id": "abc258_f",
        "domain": "Graph Theory",
        "subtopic": "Shortest Paths",
        "topic": "Dijkstra's Algorithm"
    },
    {
        "id": "abc295_f",
        "domain": "Dynamic Programming (DP)",
        "subtopic": "Digit DP",
        "topic": "Digit DP"
    },
    {
        "id": "abc209_f",
        "domain": "Dynamic Programming (DP)",
        "subtopic": "Intro to DP",
        "topic": "Knapsack and Basic Dynamic Programming"
    },
    {
        "id": "agc024_d",
        "domain": "Miscellaneous",
        "subtopic": "General",
        "topic": "Tree Isomorphism"
    },
    {
        "id": "arc068_c",
        "domain": "Data Structures (DS)",
        "subtopic": "Square Root Decomposition",
        "topic": "Splitting Objects into Light and Heavy / Case Processing"
    },
    {
        "id": "arc049_c",
        "domain": "Graph Theory",
        "subtopic": "Graph Traversal",
        "topic": "Topological Sorting"
    },
    {
        "id": "arc044_c",
        "domain": "Dynamic Programming (DP)",
        "subtopic": "Intro to DP",
        "topic": "Knapsack and Basic Dynamic Programming"
    },
    {
        "id": "exawizards2019_e",
        "domain": "Math",
        "subtopic": "Probabilities and Expected Values",
        "topic": "Gambler's Ruin"
    },
    {
        "id": "panasonic2020_e",
        "domain": "Strings",
        "subtopic": "String Matching",
        "topic": "String Matching using Bitsets"
    }
]

all_ok = True
for c in candidates:
    d = c['domain']
    s = c['subtopic']
    t = c['topic']
    
    if d not in tax:
        print(f"[!] Invalid Domain: '{d}' for {c['id']}")
        all_ok = False
        continue
    if s not in tax[d]:
        print(f"[!] Invalid Subtopic: '{s}' in Domain '{d}' for {c['id']}")
        all_ok = False
        continue
    valid_topics = [item[1] if isinstance(item, list) else item for item in tax[d][s]]
    if t not in valid_topics:
        print(f"[!] Invalid Topic: '{t}' in '{d}' > '{s}' for {c['id']}")
        all_ok = False
        continue
    print(f"[+] {c['id']}: {d} > {s} > {t} VALID")

if all_ok:
    print("\nALL 16 CANDIDATES ARE 100% TAXONOMY COMPLIANT!")
