# Priority Queue Top-K Sum of Three Arrays (Pruning to K)

**Domain**: `Basics`  
**Subtopic**: `Priority Queue`  

This workbook contains curated, high-quality competitive programming problems teaching **Priority Queue Top-K Sum of Three Arrays (Pruning to K)**.

---

## Curated Problems

### `[problem:AtCoder-abc123_d]` — Cake 123
- **Rating / Difficulty**: 1489
- **Contest**: `abc123`
- **Analysis**: [`analysis/AtCoder-abc123_d.md`](../../analysis/AtCoder-abc123_d.md)
- **Key Idea**: Notice that K <= 3000 is much smaller than X * Y * Z = 10^9. First compute all X * Y sums of A_i + B_j, sort descending, and retain only the top min(K, X * Y) sums. Then pair these top sums with C.
- **Time Complexity**: `O(X * Y log(X * Y) + K * Z log(K * Z))`
- **Space Complexity**: `O(X * Y + K * Z)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int x, y, z, k;
    if (!(cin >> x >> y >> z >> k)) return 0;

    vector<long long> a(x), b(y), c(z);
    for (int i = 0; i < x; ++i) cin >> a[i];
    for (int i = 0; i < y; ++i) cin >> b[i];
    for (int i = 0; i < z; ++i) cin >> c[i];

    vector<long long> ab;
    ab.reserve(x * y);
    for (int i = 0; i < x; ++i) {
        for (int j = 0; j < y; ++j) {
            ab.push_back(a[i] + b[j]);
        }
    }

    sort(ab.rbegin(), ab.rend());
    if ((int)ab.size() > k) ab.resize(k);

    vector<long long> abc;
    abc.reserve(ab.size() * z);
    for (long long sum_ab : ab) {
        for (int i = 0; i < z; ++i) {
            abc.push_back(sum_ab + c[i]);
        }
    }

    sort(abc.rbegin(), abc.rend());
    for (int i = 0; i < k; ++i) {
        cout << abc[i] << "\n";
    }

    return 0;
}
```
