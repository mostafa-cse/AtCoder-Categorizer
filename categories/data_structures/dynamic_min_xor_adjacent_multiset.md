# Dynamic Minimum XOR Pair Maintenance via Adjacent Elements in Sorted Multiset

**Domain**: `Data Structures (DS)`  
**Subtopic**: `Queue & Priority Queue`  

This workbook contains curated, high-quality competitive programming problems teaching **Dynamic Minimum XOR Pair Maintenance via Adjacent Elements in Sorted Multiset**.

---

## Curated Problems

### `[problem:AtCoder-abc308_g]` — Minimum Xor Pair Query
- **Rating / Difficulty**: 2008
- **Contest**: `abc308`
- **Analysis**: [`analysis/AtCoder-abc308_g.md`](../../analysis/AtCoder-abc308_g.md)
- **Key Idea**: In any sorted array a_1 <= a_2 <= ... <= a_k, the minimum XOR pair is always formed by two adjacent elements: min_{i < j} (a_i XOR a_j) = min_{1 <= i < k} (a_i XOR a_{i+1}). This follows from Trie properties, as adjacent elements share the longest common binary prefix. We maintain elements in a sorted std::multiset<int> S, and adjacent differences in another std::multiset<int> diffs. Insertions and deletions update only adjacent pairs in O(log |S|).
- **Time Complexity**: `O(Q log Q)`
- **Space Complexity**: `O(Q)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <set>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    multiset<int> s;
    multiset<int> diffs;

    auto add_diff = [&](int val) {
        diffs.insert(val);
    };

    auto remove_diff = [&](int val) {
        auto it = diffs.find(val);
        if (it != diffs.end()) {
            diffs.erase(it);
        }
    };

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int x;
            cin >> x;
            auto it = s.lower_bound(x);
            if (it != s.end() && it != s.begin()) {
                remove_diff(*prev(it) ^ *it);
            }
            if (it != s.end()) {
                add_diff(x ^ *it);
            }
            if (it != s.begin()) {
                add_diff(*prev(it) ^ x);
            }
            s.insert(x);
        } else if (type == 2) {
            int x;
            cin >> x;
            auto it = s.find(x);
            auto prv = (it != s.begin() ? prev(it) : s.end());
            auto nxt = next(it);

            if (prv != s.end()) {
                remove_diff(*prv ^ x);
            }
            if (nxt != s.end()) {
                remove_diff(x ^ *nxt);
            }
            if (prv != s.end() && nxt != s.end()) {
                add_diff(*prv ^ *nxt);
            }
            s.erase(it);
        } else {
            cout << *diffs.begin() << "\n";
        }
    }

    return 0;
}
```
