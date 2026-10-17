# Basic Greedy Algorithms

**Domain**: `Basics`  
**Subtopic**: `Greedy and Constructive`  

This workbook contains curated, high-quality competitive programming problems teaching **Basic Greedy Algorithms**.

---

## Curated Problems

### `[problem:AtCoder-abc027_d]` — Robot Movement
- **Rating / Difficulty**: 2081
- **Contest**: `abc027`
- **Analysis**: [`analysis/AtCoder-abc027_d.md`](../../analysis/AtCoder-abc027_d.md)
- **Key Idea**: Each operation (+ or -) performed at index i affects all subsequent 'M' characters. Specifically, choosing +1 at index i contributes +1 * (number of 'M' after index i) to the score, and -1 contributes -1 * (number of 'M' after index i). Thus, the i-th non-'M' position has an intrinsic coefficient c_i = count of 'M's in S[i+1..|S|]. To maximize the total sum sum c_i * sign_i with exactly half chosen as +1 and half as -1, we simply sort the coefficients c_i in ascending order, assign -1 to the smaller half, and +1 to the larger half.
- **Time Complexity**: `O(|S| log |S|)`
- **Space Complexity**: `O(|S|)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int n = s.size();
    vector<int> suffix_m(n + 1, 0);
    for (int i = n - 1; i >= 0; --i) {
        suffix_m[i] = suffix_m[i + 1] + (s[i] == 'M' ? 1 : 0);
    }

    vector<int> coeffs;
    for (int i = 0; i < n; ++i) {
        if (s[i] != 'M') {
            coeffs.push_back(suffix_m[i + 1]);
        }
    }

    sort(coeffs.begin(), coeffs.end());

    int k = coeffs.size();
    long long ans = 0;
    for (int i = 0; i < k / 2; ++i) {
        ans -= coeffs[i];
    }
    for (int i = k / 2; i < k; ++i) {
        ans += coeffs[i];
    }

    cout << ans << "\n";
    return 0;
}
```
