# 8-Sign Octant Projection for 3D Extremal Sums

**Domain**: `Basics`  
**Subtopic**: `Complete Search`  

This workbook contains curated, high-quality competitive programming problems teaching **8-Sign Octant Projection for 3D Extremal Sums**.

---

## Curated Problems

### [problem:AtCoder-abc100_d] — Patisserie ABC
- **Contest**: `abc100`
- **Rating / Difficulty**: 1331
- **Specific Skill**: 8-Sign Octant Projection for 3D Extremal Sums
- **Individual Analysis**: [`../../analysis/AtCoder-abc100_d.md`](../../analysis/AtCoder-abc100_d.md)
- **Problem Statement Summary**: N cakes, cake i has beauty x_i, taste y_i, popularity z_i. Choose M cakes to maximize |sum x_i| + |sum y_i| + |sum z_i|.
- **Core Insight**: There are only 2^3 = 8 sign assignments (s_x, s_y, s_z). For any fixed sign tuple, the objective becomes a simple linear sum: sum (s_x * x_i + s_y * y_i + s_z * z_i). To maximize this sum over M cakes, simply evaluate score_i = s_x * x_i + s_y * y_i + s_z * z_i for all N cakes, sort in descending order, and take the top M. The global maximum over all 8 sign configurations is the exact answer!
- **Complexity**: Time: `O(8 * N log N)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Cake {
    long long x, y, z;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<Cake> cakes(n);
    for (int i = 0; i < n; ++i) {
        cin >> cakes[i].x >> cakes[i].y >> cakes[i].z;
    }

    long long max_val = 0;

    for (int sx : {-1, 1}) {
        for (int sy : {-1, 1}) {
            for (int sz : {-1, 1}) {
                vector<long long> scores(n);
                for (int i = 0; i < n; ++i) {
                    scores[i] = sx * cakes[i].x + sy * cakes[i].y + sz * cakes[i].z;
                }
                sort(scores.rbegin(), scores.rend());

                long long current_sum = 0;
                for (int i = 0; i < m; ++i) {
                    current_sum += scores[i];
                }

                max_val = max(max_val, current_sum);
            }
        }
    }

    cout << max_val << "\n";
    return 0;
}
```
