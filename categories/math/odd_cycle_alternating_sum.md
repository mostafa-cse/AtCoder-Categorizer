# Odd Cycle Telescoping Alternating Sum

**Domain**: `Math`  
**Subtopic**: `Linear Systems`  

This workbook contains curated, high-quality competitive programming problems teaching **Odd Cycle Telescoping Alternating Sum**.

---

## Curated Problems

### [problem:AtCoder-abc133_d] — Rain Flows into Dams
- **Contest**: `abc133`
- **Rating / Difficulty**: 938
- **Specific Skill**: Odd Cycle Telescoping Alternating Sum
- **Individual Analysis**: [`../../analysis/AtCoder-abc133_d.md`](../../analysis/AtCoder-abc133_d.md)
- **Problem Statement Summary**: N mountains and N dams in a circle (N is odd). Dam i receives half the rain from mountain i and mountain i+1 (dam N between N and 1). Given dam water amounts A_1..A_N, find rain on each mountain X_1..X_N.
- **Core Insight**: Notice X_1 = sum_{i=1}^N A_i - 2 * (A_2 + A_4 + ... + A_{N-1}). Once X_1 is known, every subsequent variable is determined in O(1) via X_{i+1} = 2 * A_i - X_i.
- **Complexity**: Time: `O(N)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n + 1);
    long long total_a = 0;
    long long even_a = 0;

    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
        total_a += a[i];
        if (i % 2 == 0) {
            even_a += a[i];
        }
    }

    vector<long long> x(n + 1);
    x[1] = total_a - 2 * even_a;

    for (int i = 1; i < n; ++i) {
        x[i + 1] = 2 * a[i] - x[i];
    }

    for (int i = 1; i <= n; ++i) {
        cout << x[i] << (i == n ? '\n' : ' ');
    }

    return 0;
}
```
