# Periodic Remainder Block Counting

**Domain**: `Math`  
**Subtopic**: `Periodic Arithmetic`  

This workbook contains curated, high-quality competitive programming problems teaching **Periodic Remainder Block Counting**.

---

## Curated Problems

### [problem:AtCoder-arc091_b] — Remainder Reminder
- **Contest**: `abc090`
- **Rating / Difficulty**: 1129
- **Specific Skill**: Periodic Remainder Block Counting
- **Individual Analysis**: [`../../analysis/AtCoder-arc091_b.md`](../../analysis/AtCoder-arc091_b.md)
- **Problem Statement Summary**: Count pairs (a, b) of integers with 1 <= a, b <= N such that a % b >= K.
- **Core Insight**: In each complete period of length b, the remainders >= K are K, K+1, ..., b-1 (exactly b - K values). There are floor(N / b) full periods. The remaining incomplete block has length N % b, contributing max(0LL, (N % b) - K + 1) valid values. If K == 0, subtract 1 for a = 0 (since a starts at 1).
- **Complexity**: Time: `O(N)` | Space: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, k;
    if (!(cin >> n >> k)) return 0;

    if (k == 0) {
        cout << n * n << "\n";
        return 0;
    }

    long long ans = 0;
    for (long long b = k + 1; b <= n; ++b) {
        long long full = n / b;
        long long rem = n % b;
        ans += full * (b - k);
        ans += max(0LL, rem - k + 1);
    }

    cout << ans << "\n";
    return 0;
}
```
