# Pigeonhole Principle 2^N > 200 Modulo 200 Subset Collision

**Domain**: `Math`  
**Subtopic**: `Pigeonhole Principle`  

This workbook contains curated, high-quality competitive programming problems teaching **Pigeonhole Principle 2^N > 200 Modulo 200 Subset Collision**.

---

## Curated Problems

### [problem:AtCoder-abc200_d] — Happy Birthday! 2
- **Contest**: `abc200`
- **Rating / Difficulty**: 1217
- **Specific Skill**: Pigeonhole Principle 2^N > 200 Modulo 200 Subset Collision
- **Individual Analysis**: [`../../analysis/AtCoder-abc200_d.md`](../../analysis/AtCoder-abc200_d.md)
- **Problem Statement Summary**: Given an array A of N positive integers. Find two distinct non-empty subsets B and C of A whose elements have the same sum modulo 200.
- **Core Insight**: Consider only the first min(N, 8) elements. If min(N, 8) = 8, there are 2^8 - 1 = 255 non-empty subsets. By the Pigeonhole Principle, among 255 subsets there MUST exist at least two distinct subsets with the exact same remainder modulo 200!
- **Complexity**: Time: `O(2^min(N, 8)) <= 256 operations` | Space: `O(200)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int m = min(n, 8);
    vector<long long> a(m);
    for (int i = 0; i < m; ++i) {
        cin >> a[i];
    }
    for (int i = m; i < n; ++i) {
        long long dummy;
        cin >> dummy;
    }

    vector<int> seen(200, 0);

    for (int mask = 1; mask < (1 << m); ++mask) {
        long long sum = 0;
        for (int i = 0; i < m; ++i) {
            if ((mask >> i) & 1) {
                sum += a[i];
            }
        }
        int rem = sum % 200;

        if (seen[rem] != 0) {
            int mask1 = seen[rem];
            int mask2 = mask;

            vector<int> b, c;
            for (int i = 0; i < m; ++i) {
                if ((mask1 >> i) & 1) b.push_back(i + 1);
                if ((mask2 >> i) & 1) c.push_back(i + 1);
            }

            cout << "Yes\n";
            cout << b.size();
            for (int x : b) cout << " " << x;
            cout << "\n";
            cout << c.size();
            for (int x : c) cout << " " << x;
            cout << "\n";
            return 0;
        }

        seen[rem] = mask;
    }

    cout << "No\n";
    return 0;
}
```
