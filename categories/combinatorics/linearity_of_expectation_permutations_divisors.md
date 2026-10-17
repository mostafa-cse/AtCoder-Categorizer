# Linearity of Expectation over Permutations via Divisor Relative Rank

**Domain**: `Combinatorics`  
**Subtopic**: `Linearity of Expectation`  

This workbook contains curated, high-quality competitive programming problems teaching **Linearity of Expectation over Permutations via Divisor Relative Rank**.

---

## Curated Problems

### `[problem:AtCoder-abc008_3]` — コイン
- **Rating / Difficulty**: 1836
- **Contest**: `abc008`
- **Analysis**: [`analysis/AtCoder-abc008_3.md`](../../analysis/AtCoder-abc008_3.md)
- **Key Idea**: By Linearity of Expectation, E[heads] = sum_{i=1}^N P(coin i is heads). For coin i, let k be the number of other coins that divide C_i. The state of coin i depends solely on its relative order among these k + 1 coins.
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> c(n);
    for (int i = 0; i < n; ++i) cin >> c[i];

    double expected_heads = 0.0;

    for (int i = 0; i < n; ++i) {
        int k = 0;
        for (int j = 0; j < n; ++j) {
            if (i != j && c[i] % c[j] == 0) {
                k++;
            }
        }

        double prob = (double)(k / 2 + 1) / (k + 1);
        expected_heads += prob;
    }

    cout << fixed << setprecision(12) << expected_heads << "\n";
    return 0;
}
```
