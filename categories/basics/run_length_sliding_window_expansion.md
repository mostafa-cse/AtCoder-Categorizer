# Run-Length Compression Sliding Window Expansion

**Domain**: `Basics`  
**Subtopic**: `Sliding Window`  

This workbook contains curated, high-quality competitive programming problems teaching **Run-Length Compression Sliding Window Expansion**.

---

## Curated Problems

### [problem:AtCoder-abc124_d] — Handstand
- **Contest**: `abc124`
- **Rating / Difficulty**: 1138
- **Specific Skill**: Run-Length Compression Sliding Window Expansion
- **Individual Analysis**: [`../../analysis/AtCoder-abc124_d.md`](../../analysis/AtCoder-abc124_d.md)
- **Problem Statement Summary**: Given a binary string S. In one operation, flip a contiguous segment of '0's into '1's. At most K operations. Maximize consecutive '1's in the resulting string.
- **Core Insight**: Flipping K segments of '0's allows taking a contiguous sequence of runs containing at most K '0'-runs and their intervening/adjacent '1'-runs. This corresponds to a sliding window of length at most 2*K + 1 on the alternating run-length array.
- **Complexity**: Time: `O(N)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct Block {
    char c;
    int len;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    string s;
    if (!(cin >> n >> k >> s)) return 0;

    vector<Block> blocks;
    for (int i = 0; i < n; ) {
        int j = i;
        while (j < n && s[j] == s[i]) j++;
        blocks.push_back({s[i], j - i});
        i = j;
    }

    int max_len = 0;
    int cur_len = 0;
    int zero_blocks = 0;
    int r = 0;

    for (int l = 0; l < (int)blocks.size(); ++l) {
        while (r < (int)blocks.size()) {
            if (blocks[r].c == '0' && zero_blocks == k) break;
            if (blocks[r].c == '0') zero_blocks++;
            cur_len += blocks[r].len;
            r++;
        }

        max_len = max(max_len, cur_len);

        if (blocks[l].c == '0') zero_blocks--;
        cur_len -= blocks[l].len;
    }

    cout << max_len << "\n";
    return 0;
}
```
