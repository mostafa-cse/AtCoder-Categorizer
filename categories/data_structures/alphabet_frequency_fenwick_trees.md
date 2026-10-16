# Alphabet Frequency Fenwick Trees / Ordered Sets

**Domain**: `Data Structures`  
**Subtopic**: `Fenwick Tree`  

This workbook contains curated, high-quality competitive programming problems teaching **Alphabet Frequency Fenwick Trees / Ordered Sets**.

---

## Curated Problems

### `[problem:AtCoder-abc157_e]` — Simple String Queries
- **Rating / Difficulty**: 1443
- **Contest**: `abc157`
- **Analysis**: [`analysis/AtCoder-abc157_e.md`](../../analysis/AtCoder-abc157_e.md)
- **Key Idea**: Maintain 26 separate Fenwick trees (one per character 'a'..'z'). Update in O(log N) and query distinct count by summing over all 26 characters if their range count > 0 in O(26 log N).
- **Time Complexity**: `O((N + Q) * 26 * log N)`
- **Space Complexity**: `O(26 * N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct Fenwick {
    int n;
    vector<int> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0) {}

    void add(int i, int delta) {
        for (; i <= n; i += i & -i) tree[i] += delta;
    }

    int query(int i) const {
        int sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }

    int range_query(int l, int r) const {
        return query(r) - query(l - 1);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    string s;
    if (!(cin >> n >> s)) return 0;

    vector<Fenwick> bits(26, Fenwick(n));
    for (int i = 0; i < n; ++i) {
        bits[s[i] - 'a'].add(i + 1, 1);
    }

    int q;
    cin >> q;
    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int idx;
            char c;
            cin >> idx >> c;
            if (s[idx - 1] != c) {
                bits[s[idx - 1] - 'a'].add(idx, -1);
                bits[c - 'a'].add(idx, 1);
                s[idx - 1] = c;
            }
        } else {
            int l, r;
            cin >> l >> r;
            int distinct = 0;
            for (int c = 0; c < 26; ++c) {
                if (bits[c].range_query(l, r) > 0) {
                    distinct++;
                }
            }
            cout << distinct << "\n";
        }
    }

    return 0;
}
```
