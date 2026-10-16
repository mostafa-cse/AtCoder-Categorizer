# Digit DP with Carry on Minimum Digits for Payment and Change

**Domain**: `Dynamic Programming`  
**Subtopic**: `Digit DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Digit DP with Carry on Minimum Digits for Payment and Change**.

---

## Curated Problems

### `[problem:AtCoder-abc155_e]` — Payment
- **Rating / Difficulty**: 1569
- **Contest**: `abc155`
- **Analysis**: [`analysis/AtCoder-abc155_e.md`](../../analysis/AtCoder-abc155_e.md)
- **Key Idea**: Process digits from right to left (least significant to most significant) with a carry state. At each digit d, you can either pay d notes with no carry, or pay 10 notes to round up (costing 10 - d notes in change) and passing a carry of 1 to the next digit.
- **Time Complexity**: `O(|N|)`
- **Space Complexity**: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    reverse(s.begin(), s.end());
    s.push_back('0');

    long long dp0 = 0; // carry = 0
    long long dp1 = 1; // carry = 1

    for (char c : s) {
        int d = c - '0';
        long long next_dp0 = min(dp0 + d, dp1 + d + 1);
        long long next_dp1 = min(dp0 + (10 - d), dp1 + (10 - (d + 1)));
        dp0 = next_dp0;
        dp1 = next_dp1;
    }

    cout << dp0 << "\n";
    return 0;
}
```
