# Greedy Top Elements Average + Combinatorics on Boundary Frequency

**Domain**: `Math`  
**Subtopic**: `Combinatorics`  

This workbook contains curated, high-quality competitive programming problems teaching **Greedy Top Elements Average + Combinatorics on Boundary Frequency**.

---

## Curated Problems

### `[problem:AtCoder-abc057_d]` — Maximum Average Sets
- **Rating / Difficulty**: 1658
- **Contest**: `abc057`
- **Analysis**: [`analysis/AtCoder-abc057_d.md`](../../analysis/AtCoder-abc057_d.md)
- **Key Idea**: Sort elements descending. The maximum mean is always achieved by picking the top A elements. If all top A elements are equal, we can pick any number of them from A to min(B, total_count). Otherwise, we MUST pick exactly A elements.
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N^2)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

long long C[55][55];

void precompute_comb() {
    for (int i = 0; i <= 50; ++i) {
        C[i][0] = 1;
        for (int j = 1; j <= i; ++j) {
            C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    precompute_comb();

    int n, a, b;
    if (!(cin >> n >> a >> b)) return 0;

    vector<long long> v(n);
    for (int i = 0; i < n; ++i) {
        cin >> v[i];
    }

    sort(v.rbegin(), v.rend());

    long long sum_a = 0;
    for (int i = 0; i < a; ++i) {
        sum_a += v[i];
    }

    double max_avg = (double)sum_a / a;
    long long ways = 0;

    if (v[0] == v[a - 1]) {
        int total_cnt = 0;
        for (int i = 0; i < n; ++i) {
            if (v[i] == v[0]) total_cnt++;
        }
        for (int k = a; k <= min(b, total_cnt); ++k) {
            ways += C[total_cnt][k];
        }
    } else {
        long long boundary_val = v[a - 1];
        int total_cnt = 0;
        for (int i = 0; i < n; ++i) {
            if (v[i] == boundary_val) total_cnt++;
        }
        int needed_cnt = 0;
        for (int i = 0; i < a; ++i) {
            if (v[i] == boundary_val) needed_cnt++;
        }
        ways = C[total_cnt][needed_cnt];
    }

    cout << fixed << setprecision(12) << max_avg << "\n";
    cout << ways << "\n";
    return 0;
}
```
