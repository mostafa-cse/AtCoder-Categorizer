# Reverse Operation Constructive Array Synthesis modulo N

**Domain**: `Basics`  
**Subtopic**: `Constructive Algorithms`  

This workbook contains curated, high-quality competitive programming problems teaching **Reverse Operation Constructive Array Synthesis modulo N**.

---

## Curated Problems

### `[problem:AtCoder-arc079_b]` — Decrease
- **Rating / Difficulty**: 1545
- **Contest**: `abc068`
- **Analysis**: [`analysis/AtCoder-arc079_b.md`](../../analysis/AtCoder-arc079_b.md)
- **Key Idea**: Fix N = 50. In a complete round of N operations where each index is operated once, each element undergoes one -N and (N-1) times +1, net change of -1 to all elements. Decompose K into q = K / N rounds and r = K % N remainder operations.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long k;
    if (!(cin >> k)) return 0;

    int n = 50;
    long long q = k / n;
    int r = k % n;

    vector<long long> a(n, n - 1 + q);
    for (int i = 0; i < r; ++i) {
        a[i] += n - r + 1;
    }
    for (int i = r; i < n; ++i) {
        a[i] -= r;
    }

    cout << n << "\n";
    for (int i = 0; i < n; ++i) {
        cout << a[i] << (i + 1 == n ? "\n" : " ");
    }

    return 0;
}
```
