# Problem Analysis: AtCoder-arc053_c — 魔法使い高橋君

**Problem ID**: `AtCoder-arc053_c`  
**Contest**: `arc053`  
**Rating / Difficulty**: 1901  
**URL**: https://atcoder.jp/contests/arc053/tasks/arc053_c  
**VJudge Tag**: `[problem:AtCoder-arc053_c]`  
**Category File**: [`../categories/basics/greedy_exchange_bipartite_deltas.md`](../categories/basics/greedy_exchange_bipartite_deltas.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy`  
- **Topic (Skill)**: `Greedy Exchange Argument on Bipartite Temperature Deltas (a < b ascending, a >= b descending)`  

---

## 1. Problem Statement & Key Idea
Takahashi casts N spells. Spell i first raises temperature by a_i, then lowers it by b_i. Initial temperature is 0. Find an ordering of all N spells that minimizes the maximum temperature reached at any point.

Partition spells into net-decrease (a_i < b_i) and net-increase (a_i >= b_i). For net-decrease spells, doing them first reduces the baseline for subsequent spells; exchange argument shows sorting them by a_i ascending minimizes peak. For net-increase spells, doing them last after all temperature reductions, reverse view shows sorting by b_i descending minimizes peak.

## 2. Core Observation & Invariant
For any two spells in the decrease group, max(a_1, a_1 - b_1 + a_2) <= max(a_2, a_2 - b_2 + a_1) holds iff a_1 <= a_2. Hence sorting gives optimal order in O(N log N).

## 3. Step-by-Step Algorithm
1. Partition spells into decr (a_i < b_i) and incr (a_i >= b_i).
2. Sort decr by a_i ascending.
3. Sort incr by b_i descending.
4. Simulate the process through decr then incr, maintaining max_temp and current_temp.
5. Print max_temp.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Spell {
    long long a, b;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Spell> decr, incr;
    for (int i = 0; i < n; ++i) {
        long long a, b;
        cin >> a >> b;
        if (a < b) {
            decr.push_back({a, b});
        } else {
            incr.push_back({a, b});
        }
    }

    sort(decr.begin(), decr.end(), [](const Spell& x, const Spell& y) {
        return x.a < y.a;
    });

    sort(incr.begin(), incr.end(), [](const Spell& x, const Spell& y) {
        return x.b > y.b;
    });

    long long current = 0;
    long long max_temp = 0;

    for (const auto& s : decr) {
        max_temp = max(max_temp, current + s.a);
        current += (s.a - s.b);
    }

    for (const auto& s : incr) {
        max_temp = max(max_temp, current + s.a);
        current += (s.a - s.b);
    }

    cout << max_temp << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Greedy exchange argument partitioning on asymmetric delta transitions.
- **Reusable Pattern**: `Bipartite Delta Ordering: Sort positive gain by a_i asc, negative gain by b_i desc.`
