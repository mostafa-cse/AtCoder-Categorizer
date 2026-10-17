# Bitset-Accelerated Triangle Counting via Neighbor Set Intersections O(N^3 / 64)

**Domain**: `Data Structures (DS)`  
**Subtopic**: `Bitset Optimizations`  

This workbook contains curated, high-quality competitive programming problems teaching **Bitset-Accelerated Triangle Counting via Neighbor Set Intersections O(N^3 / 64)**.

---

## Curated Problems

### `[problem:AtCoder-abc258_g]` — Triangle
- **Rating / Difficulty**: 1944
- **Contest**: `abc258`
- **Analysis**: [`analysis/AtCoder-abc258_g.md`](../../analysis/AtCoder-abc258_g.md)
- **Key Idea**: For each pair of adjacent vertices (i, j) with i < j, the number of common neighbors k > j is the size of the set intersection of neighbors of i and neighbors of j restricted to indices > j. Using std::bitset<3000>, storing only neighbors with index > i, the count is simply (adj[i] & adj[j]).count(). Running bitwise AND over 64-bit machine words reduces operations by a factor of 64 to N^3 / 64 ~ 4.2 * 10^8 ops, executing in ~0.3s.
- **Time Complexity**: `O(N^3 / 64)`
- **Space Complexity**: `O(N^2 / 64)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <bitset>

using namespace std;

const int MAXN = 3000;
bitset<MAXN> adj[MAXN];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    for (int i = 0; i < n; ++i) {
        string s;
        cin >> s;
        for (int j = i + 1; j < n; ++j) {
            if (s[j] == '1') {
                adj[i].set(j);
            }
        }
    }

    long long count = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            if (adj[i].test(j)) {
                count += (adj[i] & adj[j]).count();
            }
        }
    }

    cout << count << "\n";
    return 0;
}
```
