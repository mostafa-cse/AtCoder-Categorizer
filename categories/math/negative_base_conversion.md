# Negative Base Division / Modulo Arithmetic

**Domain**: `Math`  
**Subtopic**: `Base Conversion`  

This workbook contains curated, high-quality competitive programming problems teaching **Negative Base Division / Modulo Arithmetic**.

---

## Curated Problems

### [problem:AtCoder-abc105_c] — Base -2 Number
- **Contest**: `abc105`
- **Rating / Difficulty**: 1204
- **Specific Skill**: Negative Base Division / Modulo Arithmetic
- **Individual Analysis**: [`../../analysis/AtCoder-abc105_c.md`](../../analysis/AtCoder-abc105_c.md)
- **Problem Statement Summary**: Given an integer N. Find its base -2 representation, i.e., a binary string S = S_k...S_0 such that N = sum_{i=0}^k S_i * (-2)^i with S_k != 0 (or '0' if N = 0).
- **Core Insight**: When we extract rem = N % (-2), C++ standard gives rem in {-1, 0, 1}. If rem is negative (-1), we adjust rem += 2 and quotient N = (N - rem) / (-2). This ensures every remainder digit is strictly in {0, 1}.
- **Complexity**: Time: `O(log_2 |N|)` | Space: `O(log_2 |N|)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    if (n == 0) {
        cout << "0\n";
        return 0;
    }

    string res = "";
    while (n != 0) {
        long long rem = n % -2;
        n /= -2;
        if (rem < 0) {
            rem += 2;
            n += 1;
        }
        res += to_string(rem);
    }

    reverse(res.begin(), res.end());
    cout << res << "\n";
    return 0;
}
```
