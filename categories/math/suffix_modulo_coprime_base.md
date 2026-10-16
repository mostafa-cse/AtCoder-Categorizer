# Suffix Modulo 2019 Prefix Arithmetic (Coprime Base)

**Domain**: `Math`  
**Subtopic**: `Number Theory`  

This workbook contains curated, high-quality competitive programming problems teaching **Suffix Modulo 2019 Prefix Arithmetic (Coprime Base)**.

---

## Curated Problems

### [problem:AtCoder-abc164_d] — Multiple of 2019
- **Contest**: `abc164`
- **Rating / Difficulty**: 1232
- **Specific Skill**: Suffix Modulo 2019 Prefix Arithmetic (Coprime Base)
- **Individual Analysis**: [`../../analysis/AtCoder-abc164_d.md`](../../analysis/AtCoder-abc164_d.md)
- **Problem Statement Summary**: Given a string S of digits. Count contiguous substrings that represent a multiple of 2019 when viewed as an integer.
- **Core Insight**: Because gcd(10, 2019) = 1 (10 is coprime to 2019 = 3 * 673), dividing by powers of 10 modulo 2019 does not change divisibility! Thus, S[l..r] = 0 (mod 2019) if and only if suffix[l] == suffix[r + 1] (mod 2019). Two matching suffix remainders define a valid multiple of 2019.
- **Complexity**: Time: `O(|S|)` | Space: `O(MOD)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int MOD = 2019;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    vector<int> cnt(MOD, 0);
    cnt[0] = 1;

    int cur_rem = 0;
    int p10 = 1;
    long long ans = 0;

    for (int i = (int)s.size() - 1; i >= 0; --i) {
        int d = s[i] - '0';
        cur_rem = (cur_rem + d * p10) % MOD;
        p10 = (p10 * 10) % MOD;
        ans += cnt[cur_rem];
        cnt[cur_rem]++;
    }

    cout << ans << "\n";
    return 0;
}
```
