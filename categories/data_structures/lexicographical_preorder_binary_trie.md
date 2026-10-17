# Trie on Strings and Bits

**Domain**: `Data Structures (DS)`  
**Subtopic**: `Trie`  

This workbook contains curated, high-quality competitive programming problems teaching **Trie on Strings and Bits**.

---

## Curated Problems

### `[problem:AtCoder-arc127_c]` — Binary String
- **Rating / Difficulty**: 2087
- **Contest**: `arc127`
- **Analysis**: [`analysis/AtCoder-arc127_c.md`](../../analysis/AtCoder-arc127_c.md)
- **Key Idea**: The set of valid non-empty binary strings not starting with '0' correspond to the preorder traversal of a complete binary trie rooted at prefix '1' of depth up to N. At any prefix of length L: 1) the prefix itself is visited first (1 string); 2) then all strings extending with '0' (a complete binary subtree of depth N - L - 1 having 2^{N-L} - 1 strings); 3) then all strings extending with '1'. To find the X-th string, we maintain X as a large binary integer. At each step, after visiting the node, we compare X with the size of the left branch (2^{N-L-1} strings). If X <= left_subtree_size, we append '0' and descend; otherwise, we subtract left_subtree_size from X, append '1', and descend.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    string s;
    if (!(cin >> n >> s)) return 0;

    // Convert s to binary array of size n+1 (big integer)
    vector<int> x(n + 1, 0);
    int len = s.size();
    for (int i = 0; i < len; ++i) {
        x[n - len + 1 + i] = s[i] - '0';
    }

    auto dec = [&]() {
        for (int i = n; i >= 1; --i) {
            if (x[i] == 1) {
                x[i] = 0;
                break;
            } else {
                x[i] = 1;
            }
        }
    };

    auto is_zero = [&]() {
        for (int i = 1; i <= n; ++i) {
            if (x[i] != 0) return false;
        }
        return true;
    };

    dec();
    string ans = "1";

    for (int l = 1; l < n; ++l) {
        if (is_zero()) break;

        // Compare X with 2^(n - l - 1)
        // Bit position is (n - l) from right, corresponding to x[l + 1]
        if (x[l + 1] == 1) {
            ans += '1';
            x[l + 1] = 0; // subtract 2^(n - l - 1)
            dec();
        } else {
            ans += '0';
            dec();
        }
    }

    cout << ans << "\n";
    return 0;
}
```
