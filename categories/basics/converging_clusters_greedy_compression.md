# 1D Compression Invariant on Converging Directed Clusters

**Domain**: `Basics`  
**Subtopic**: `Greedy`  

This workbook contains curated, high-quality competitive programming problems teaching **1D Compression Invariant on Converging Directed Clusters**.

---

## Curated Problems

### `[problem:AtCoder-arc041_c]` — ウサギ跳び
- **Rating / Difficulty**: 1808
- **Contest**: `arc041`
- **Analysis**: [`analysis/AtCoder-arc041_c.md`](../../analysis/AtCoder-arc041_c.md)
- **Key Idea**: Rabbits decompose into independent converging blocks of 'R' followed by 'L'. Each 'R...RL...L' cluster will compress together. The gap between the rightmost R and leftmost L is traversed by either all R rabbits jumping right, or all L rabbits jumping left.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct Rabbit {
    long long x;
    char dir;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long L;
    if (!(cin >> n >> L)) return 0;

    vector<Rabbit> r(n);
    for (int i = 0; i < n; ++i) {
        cin >> r[i].x >> r[i].dir;
    }

    long long ans = 0;
    int idx = 0;

    while (idx < n) {
        vector<long long> R_pos, L_pos;
        while (idx < n && r[idx].dir == 'R') {
            R_pos.push_back(r[idx++].x);
        }
        while (idx < n && r[idx].dir == 'L') {
            L_pos.push_back(r[idx++].x);
        }

        if (R_pos.empty() && !L_pos.empty()) {
            for (int i = 0; i < (int)L_pos.size(); ++i) {
                ans += (L_pos[i] - (i + 1));
            }
        } else if (!R_pos.empty() && L_pos.empty()) {
            int k = R_pos.size();
            for (int i = 0; i < k; ++i) {
                ans += ((L - k + 1 + i) - R_pos[i]);
            }
        } else {
            int k_r = R_pos.size();
            int k_l = L_pos.size();

            for (int i = 0; i < k_r; ++i) {
                ans += (R_pos.back() - (k_r - 1 - i) - R_pos[i]);
            }
            for (int i = 0; i < k_l; ++i) {
                ans += (L_pos[i] - (L_pos.front() + i));
            }

            long long gap = L_pos.front() - R_pos.back() - 1;
            ans += gap * max(k_r, k_l);
        }
    }

    cout << ans << "\n";
    return 0;
}
```
