# Base-10 Multi-Dimensional Fast Zeta Transform / SOS DP for Carry-Free Pairs

**Domain**: `Dynamic Programming (DP)`  
**Subtopic**: `SOS DP / Fast Zeta Transform`  

This workbook contains curated, high-quality competitive programming problems teaching **Base-10 Multi-Dimensional Fast Zeta Transform / SOS DP for Carry-Free Pairs**.

---

## Curated Problems

### `[problem:AtCoder-arc136_d]` — Without Carry
- **Rating / Difficulty**: 1908
- **Contest**: `arc136`
- **Analysis**: [`analysis/AtCoder-arc136_d.md`](../../analysis/AtCoder-arc136_d.md)
- **Key Idea**: A_i + A_j has no carry iff for all 6 digits d, digit_d(A_i) + digit_d(A_j) <= 9, or digit_d(A_j) <= 9 - digit_d(A_i). Let comp(A_i) be the number with digits 9 - digit_d(A_i). We need the count of A_j whose digits are sub-digits of comp(A_i). This is a 6-dimensional submask sum query over base 10, solved in 6 * 10^6 operations via Fast Zeta Transform (SOS DP in base 10).
- **Time Complexity**: `O(6 * 10^6 + N)`
- **Space Complexity**: `O(10^6)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MAX = 1000000;
int dp[MAX];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
        dp[arr[i]]++;
    }

    // Fast Zeta Transform (SOS DP) in base 10 across 6 digits
    int p10 = 1;
    for (int d = 0; d < 6; ++d) {
        for (int i = 0; i < MAX; ++i) {
            if ((i / p10) % 10 < 9) {
                dp[i + p10] += dp[i];
            }
        }
        p10 *= 10;
    }

    auto get_comp = [](int x) {
        int comp = 0;
        int p = 1;
        for (int d = 0; d < 6; ++d) {
            int digit = (x / p) % 10;
            comp += (9 - digit) * p;
            p *= 10;
        }
        return comp;
    };

    long long total_pairs = 0;
    for (int i = 0; i < n; ++i) {
        int comp = get_comp(arr[i]);
        int count = dp[comp];
        bool self_ok = true;
        int temp = arr[i];
        while (temp > 0) {
            if ((temp % 10) * 2 >= 10) {
                self_ok = false;
                break;
            }
            temp /= 10;
        }
        if (self_ok) {
            count--;
        }
        total_pairs += count;
    }

    cout << total_pairs / 2 << "\n";
    return 0;
}
```
