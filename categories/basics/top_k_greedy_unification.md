# Top-(X+Y) Greedy Unification via Candidate Filtering

**Domain**: `Basics`  
**Subtopic**: `Greedy`  

This workbook contains curated, high-quality competitive programming problems teaching **Top-(X+Y) Greedy Unification via Candidate Filtering**.

---

## Curated Problems

### [problem:AtCoder-abc160_e] — Red and Green Apples
- **Contest**: `abc160`
- **Rating / Difficulty**: 1036
- **Specific Skill**: Top-(X+Y) Greedy Unification via Candidate Filtering
- **Individual Analysis**: [`../../analysis/AtCoder-abc160_e.md`](../../analysis/AtCoder-abc160_e.md)
- **Problem Statement Summary**: You need to eat X red apples and Y green apples. You have A red apples (values p_i), B green apples (values q_i), and C colorless apples (values r_i) that can be eaten as either red or green. Maximize the total deliciousness.
- **Core Insight**: Any chosen colorless apple should replace the smallest currently selected apple (whether red or green). Thus, we can pool the top X red apples, top Y green apples, and ALL C colorless apples into a single pool of X + Y + C items, and simply pick the largest X + Y items overall!
- **Complexity**: Time: `O(A log A + B log B + (X + Y + C) log(X + Y + C))` | Space: `O(A + B + C)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int x, y, a, b, c;
    if (!(cin >> x >> y >> a >> b >> c)) return 0;

    vector<long long> p(a), q(b), r(c);
    for (int i = 0; i < a; ++i) cin >> p[i];
    for (int i = 0; i < b; ++i) cin >> q[i];
    for (int i = 0; i < c; ++i) cin >> r[i];

    sort(p.rbegin(), p.rend());
    sort(q.rbegin(), q.rend());

    vector<long long> pool;
    pool.reserve(x + y + c);

    for (int i = 0; i < x; ++i) pool.push_back(p[i]);
    for (int i = 0; i < y; ++i) pool.push_back(q[i]);
    for (int i = 0; i < c; ++i) pool.push_back(r[i]);

    sort(pool.rbegin(), pool.rend());

    long long sum = 0;
    for (int i = 0; i < x + y; ++i) {
        sum += pool[i];
    }

    cout << sum << "\n";
    return 0;
}
```
