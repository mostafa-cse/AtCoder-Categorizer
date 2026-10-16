# Digit String Length Partition Search

**Domain**: `Basics`  
**Subtopic**: `Exhaustive Search`  

This workbook contains curated, high-quality competitive programming problems teaching **Digit String Length Partition Search**.

---

## Curated Problems

### `[problem:AtCoder-abc031_d]` — Goroawase
- **Rating / Difficulty**: 1688
- **Contest**: `abc031`
- **Analysis**: [`analysis/AtCoder-abc031_d.md`](../../analysis/AtCoder-abc031_d.md)
- **Key Idea**: There are only K digits, and each digit has length in {1, 2, 3}. The search space of length assignments is at most 3^9 = 19,683! Exhaustively search all length combinations and verify against the N string equations.
- **Time Complexity**: `O(3^K * N * sum(|w|))`
- **Space Complexity**: `O(K)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int k, n;
vector<string> v_list, w_list;
int len[10];

bool check() {
    vector<string> ans(k + 1, "");
    for (int i = 0; i < n; ++i) {
        int expected_len = 0;
        for (char c : v_list[i]) {
            expected_len += len[c - '0'];
        }
        if (expected_len != (int)w_list[i].size()) return false;

        int pos = 0;
        for (char c : v_list[i]) {
            int d = c - '0';
            string sub = w_list[i].substr(pos, len[d]);
            pos += len[d];

            if (ans[d] == "") {
                ans[d] = sub;
            } else if (ans[d] != sub) {
                return false;
            }
        }
    }

    for (int d = 1; d <= k; ++d) {
        cout << ans[d] << "\n";
    }
    return true;
}

bool search_lens(int idx) {
    if (idx > k) {
        return check();
    }
    for (int l = 1; l <= 3; ++l) {
        len[idx] = l;
        if (search_lens(idx + 1)) return true;
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> k >> n)) return 0;

    v_list.resize(n);
    w_list.resize(n);
    for (int i = 0; i < n; ++i) {
        cin >> v_list[i] >> w_list[i];
    }

    search_lens(1);
    return 0;
}
```
