# Greedy Exchange Argument on Bipartite Temperature Deltas (a < b ascending, a >= b descending)

**Domain**: `Basics`  
**Subtopic**: `Greedy`  

This workbook contains curated, high-quality competitive programming problems teaching **Greedy Exchange Argument on Bipartite Temperature Deltas (a < b ascending, a >= b descending)**.

---

## Curated Problems

### `[problem:AtCoder-arc053_c]` — 魔法使い高橋君
- **Rating / Difficulty**: 1901
- **Contest**: `arc053`
- **Analysis**: [`analysis/AtCoder-arc053_c.md`](../../analysis/AtCoder-arc053_c.md)
- **Key Idea**: Partition spells into net-decrease (a_i < b_i) and net-increase (a_i >= b_i). For net-decrease spells, doing them first reduces the baseline for subsequent spells; exchange argument shows sorting them by a_i ascending minimizes peak. For net-increase spells, doing them last after all temperature reductions, reverse view shows sorting by b_i descending minimizes peak.
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
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
