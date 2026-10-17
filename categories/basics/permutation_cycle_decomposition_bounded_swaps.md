# Basic Constructive Algorithms

**Domain**: `Basics`  
**Subtopic**: `Greedy and Constructive`  

This workbook contains curated, high-quality competitive programming problems teaching **Basic Constructive Algorithms**.

---

## Curated Problems

### `[problem:AtCoder-nikkei2019_2_qual_c]` — Swaps
- **Rating / Difficulty**: 2136
- **Contest**: `nikkei2019-2-qual`
- **Analysis**: [`analysis/AtCoder-nikkei2019_2_qual_c.md`](../../analysis/AtCoder-nikkei2019_2_qual_c.md)
- **Key Idea**: Sort A and B independently. If sorted A_i > B_i for any i, it is impossible. If sorted A_i <= B_i holds for all i, pairing A_i with B_i defines a permutation on positions. A permutation with c disjoint cycles requires N - c swaps to sort. Thus, if the permutation has c >= 2 cycles, N - c <= N - 2 swaps suffice! If c = 1, it requires N - 1 swaps unless we can shortcut two adjacent elements: if sorted A_{i+1} <= B_i for any i, we can split the single cycle into two cycles without violating the inequality A <= B.
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

struct Element {
    long long a;
    int id;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Element> a(n);
    vector<long long> b(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i].a;
        a[i].id = i;
    }
    for (int i = 0; i < n; ++i) {
        cin >> b[i];
    }

    sort(a.begin(), a.end(), [](const Element& x, const Element& y) {
        return x.a < y.a;
    });
    sort(b.begin(), b.end());

    for (int i = 0; i < n; ++i) {
        if (a[i].a > b[i]) {
            cout << "No\n";
            return 0;
        }
    }

    for (int i = 0; i < n - 1; ++i) {
        if (a[i + 1].a <= b[i]) {
            cout << "Yes\n";
            return 0;
        }
    }

    vector<bool> vis(n, false);
    int cycles = 0;
    for (int i = 0; i < n; ++i) {
        if (!vis[i]) {
            cycles++;
            int cur = i;
            while (!vis[cur]) {
                vis[cur] = true;
                cur = a[cur].id;
            }
        }
    }

    if (cycles >= 2) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }

    return 0;
}
```
