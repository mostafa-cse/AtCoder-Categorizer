# Bitmask Horizontal Cuts with Greedy Vertical Sweeping

**Domain**: `Basics`  
**Subtopic**: `Bitmask Search`  

This workbook contains curated, high-quality competitive programming problems teaching **Bitmask Horizontal Cuts with Greedy Vertical Sweeping**.

---

## Curated Problems

### `[problem:AtCoder-abc159_e]` — Dividing Chocolate
- **Rating / Difficulty**: 1450
- **Contest**: `abc159`
- **Analysis**: [`analysis/AtCoder-abc159_e.md`](../../analysis/AtCoder-abc159_e.md)
- **Key Idea**: Because H <= 10, enumerate all 2^(H-1) subsets of horizontal cuts. For each fixed horizontal cut mask, greedily sweep columns from left to right, making a vertical cut whenever any horizontal slice would exceed K chips.
- **Time Complexity**: `O(2^(H-1) * H * W)`
- **Space Complexity**: `O(H * W)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w, k;
    if (!(cin >> h >> w >> k)) return 0;

    vector<string> s(h);
    for (int i = 0; i < h; ++i) {
        cin >> s[i];
    }

    int ans = 1e9;
    int total_masks = 1 << (h - 1);

    for (int mask = 0; mask < total_masks; ++mask) {
        // Map rows to group indices
        vector<int> group_id(h, 0);
        int g = 0;
        for (int r = 0; r < h - 1; ++r) {
            if (mask & (1 << r)) g++;
            group_id[r + 1] = g;
        }
        int num_groups = g + 1;

        int cuts = __builtin_popcount(mask);
        vector<int> current_chips(num_groups, 0);
        bool valid = true;

        for (int c = 0; c < w; ++c) {
            vector<int> col_chips(num_groups, 0);
            for (int r = 0; r < h; ++r) {
                if (s[r][c] == '1') {
                    col_chips[group_id[r]]++;
                }
            }

            // If a single column exceeds K in any group, this mask is impossible
            for (int i = 0; i < num_groups; ++i) {
                if (col_chips[i] > k) {
                    valid = false;
                    break;
                }
            }
            if (!valid) break;

            // Check if adding this column forces a cut
            bool need_cut = false;
            for (int i = 0; i < num_groups; ++i) {
                if (current_chips[i] + col_chips[i] > k) {
                    need_cut = true;
                    break;
                }
            }

            if (need_cut) {
                cuts++;
                current_chips = col_chips;
            } else {
                for (int i = 0; i < num_groups; ++i) {
                    current_chips[i] += col_chips[i];
                }
            }
        }

        if (valid) {
            ans = min(ans, cuts);
        }
    }

    cout << ans << "\n";
    return 0;
}
```
