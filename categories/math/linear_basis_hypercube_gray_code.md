# Vector Space and XOR Basis

**Domain**: `Math`  
**Subtopic**: `Linear Algebra`  

This workbook contains curated, high-quality competitive programming problems teaching **Vector Space and XOR Basis**.

---

## Curated Problems

### `[problem:AtCoder-arc138_d]` — Differ by K bits
- **Rating / Difficulty**: 2080
- **Contest**: `arc138`
- **Analysis**: [`analysis/AtCoder-arc138_d.md`](../../analysis/AtCoder-arc138_d.md)
- **Key Idea**: A cycle of length 2^N where each step flips K bits is a Hamiltonian cycle on a generalized hypercube graph. The parity of the number of 1s in the binary representation changes by K mod 2 at each step. Since 2^N is even, visiting all vertices and returning to 0 requires an even number of steps, but if K is even, the parity of the number of set bits never changes, making it bipartite-partitioned and impossible to visit odd-weight states! Thus K must be odd and 1 <= K < N. When K is odd, we can find N linearly independent vectors v_1, ..., v_N in (F_2)^N each having popcount K. Using the standard reflected binary Gray code G_i, we map each element to sum_{j=0}^{N-1} ((G_i >> j) & 1) * v_j.
- **Time Complexity**: `O(N * 2^N)`
- **Space Complexity**: `O(2^N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

int count_bits(int x) {
    return __builtin_popcount(x);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    if (k % 2 == 0 || k > n) {
        cout << "No\n";
        return 0;
    }

    if (k == n) {
        if (n == 1) {
            cout << "Yes\n0 1\n";
        } else {
            cout << "No\n";
        }
        return 0;
    }

    vector<int> basis;
    vector<int> original;

    for (int mask = 1; mask < (1 << n); ++mask) {
        if (count_bits(mask) == k) {
            int cur = mask;
            for (int b : basis) {
                cur = min(cur, cur ^ b);
            }
            if (cur > 0) {
                basis.push_back(cur);
                original.push_back(mask);
                // Maintain reduced basis
                for (int i = (int)basis.size() - 1; i > 0; --i) {
                    if (basis[i] > basis[i - 1]) {
                        swap(basis[i], basis[i - 1]);
                    }
                }
                if ((int)original.size() == n) break;
            }
        }
    }

    if ((int)original.size() < n) {
        cout << "No\n";
        return 0;
    }

    cout << "Yes\n";
    int total = 1 << n;
    for (int i = 0; i < total; ++i) {
        int gray = i ^ (i >> 1);
        int val = 0;
        for (int j = 0; j < n; ++j) {
            if ((gray >> j) & 1) {
                val ^= original[j];
            }
        }
        cout << val << (i + 1 == total ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```
