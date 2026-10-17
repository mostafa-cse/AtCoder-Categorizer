# Digit DP: Base-8 Conversion / Banned Digits Counting

**Domain**: `Dynamic Programming`  
**Subtopic**: `Digit DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Digit DP: Base-8 Conversion / Banned Digits Counting**.

---

## Curated Problems

### `[problem:AtCoder-abc007_4]` — 禁止された数字
- **Rating / Difficulty**: 1718
- **Contest**: `abc007`
- **Analysis**: [`analysis/AtCoder-abc007_4.md`](../../analysis/AtCoder-abc007_4.md)
- **Key Idea**: Count the complement: numbers in [1, X] containing NEITHER 4 nor 9. Digits {0, 1, 2, 3, 5, 6, 7, 8} are allowed (8 valid digits). This is equivalent to standard Digit DP or base-8 conversion.
- **Time Complexity**: `O(log10(B))`
- **Space Complexity**: `O(log10(B))`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <cstring>

using namespace std;

long long memo[20][2];
string S;

long long dp(int idx, bool is_less) {
    if (idx == (int)S.size()) return 1;
    if (memo[idx][is_less] != -1) return memo[idx][is_less];

    long long res = 0;
    int limit = is_less ? 9 : (S[idx] - '0');

    for (int d = 0; d <= limit; ++d) {
        if (d == 4 || d == 9) continue;
        res += dp(idx + 1, is_less || (d < limit));
    }

    return memo[idx][is_less] = res;
}

long long count_valid(long long n) {
    if (n < 0) return 0;
    S = to_string(n);
    memset(memo, -1, sizeof(memo));
    return dp(0, false);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b;
    if (!(cin >> a >> b)) return 0;

    long long valid_b = count_valid(b);
    long long valid_a = count_valid(a - 1);

    long long total_numbers = b - a + 1;
    long long valid_numbers = valid_b - valid_a;

    cout << total_numbers - valid_numbers << "\n";
    return 0;
}
```
