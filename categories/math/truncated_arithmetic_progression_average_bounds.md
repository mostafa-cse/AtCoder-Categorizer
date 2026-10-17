# Average Remainder Bounding and Modular Divisibility on Truncated Arithmetic Progression

**Domain**: `Math`  
**Subtopic**: `Analytical Bounds`  

This workbook contains curated, high-quality competitive programming problems teaching **Average Remainder Bounding and Modular Divisibility on Truncated Arithmetic Progression**.

---

## Curated Problems

### `[problem:AtCoder-arc004_3]` — 平均値太郎の憂鬱
- **Rating / Difficulty**: 1904
- **Contest**: `arc004`
- **Analysis**: [`analysis/AtCoder-arc004_3.md`](../../analysis/AtCoder-arc004_3.md)
- **Key Idea**: Total sum is N(N+1)/2. Removing M gives sum S = N(N+1)/2 - M = X(N - 1) / Y. Since 1 <= M <= N, the average S / (N - 1) must lie strictly in [N/2, (N+2)/2]. This restricts N to at most two integer candidates near 2X/Y. Furthermore, Y must divide X(N - 1), so N = 1 mod Y.
- **Time Complexity**: `O(1)`
- **Space Complexity**: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <numeric>
#include <vector>

using namespace std;

long long gcd_val(long long a, long long b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long X, Y;
    char slash;
    if (!(cin >> X >> slash >> Y)) return 0;

    long long g = gcd_val(X, Y);
    X /= g;
    Y /= g;

    long long low_N = 2 * X / Y - 1;
    long long high_N = 2 * X / Y + 1;
    if (low_N < 2) low_N = 2;

    bool found = false;
    for (long long N = low_N; N <= high_N; ++N) {
        if ((N - 1) % Y == 0) {
            long long k = (N - 1) / Y;
            long long S = k * X;
            long long total = N * (N + 1) / 2;
            long long M = total - S;
            if (M >= 1 && M <= N) {
                cout << N << " " << M << "\n";
                found = true;
            }
        }
    }

    if (!found) {
        cout << "Impossible\n";
    }

    return 0;
}
```
