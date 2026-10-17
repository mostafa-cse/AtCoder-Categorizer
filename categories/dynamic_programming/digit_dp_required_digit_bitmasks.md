# Digit DP

**Domain**: `Dynamic Programming (DP)`  
**Subtopic**: `Digit DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Digit DP**.

---

## Curated Problems

### `[problem:AtCoder-abc235_f]` — Variety of Digits
- **Rating / Difficulty**: 2129
- **Contest**: `abc235`
- **Analysis**: [`analysis/AtCoder-abc235_f.md`](../../analysis/AtCoder-abc235_f.md)
- **Key Idea**: Standard digit DP tracking both count of valid numbers and sum of their values. State: dp[mask][is_less][is_started], where mask is the 10-bit bitmask of distinct digits seen so far. When appending digit d, the count increases by prev_count, and the accumulated value increases by (prev_sum * 10 + prev_count * d). After processing all digits of N, sum the value contributions of all states where the required digit mask target_mask is completely covered.
- **Time Complexity**: `O(|N| * 2^{10} * 10)`
- **Space Complexity**: `O(2^{10})`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int MOD = 998244353;

struct State {
    long long cnt;
    long long sum;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    int m;
    if (!(cin >> s >> m)) return 0;

    int target_mask = 0;
    for (int i = 0; i < m; ++i) {
        int c;
        cin >> c;
        target_mask |= (1 << c);
    }

    int n = s.size();
    vector<vector<vector<State>>> cur(1024, vector<vector<State>>(2, vector<State>(2, {0, 0})));
    cur[0][0][0] = {1, 0};

    for (int i = 0; i < n; ++i) {
        vector<vector<vector<State>>> next_cur(1024, vector<vector<State>>(2, vector<State>(2, {0, 0})));
        int digit = s[i] - '0';

        for (int mask = 0; mask < 1024; ++mask) {
            for (int less = 0; less < 2; ++less) {
                for (int st = 0; st < 2; ++st) {
                    State cur_st = cur[mask][less][st];
                    if (!cur_st.cnt) continue;

                    int limit = less ? 9 : digit;
                    for (int d = 0; d <= limit; ++d) {
                        int nxt_less = less | (d < limit);
                        int nxt_st = st | (d > 0);
                        int nxt_mask = nxt_st ? (mask | (1 << d)) : 0;

                        State& target = next_cur[nxt_mask][nxt_less][nxt_st];
                        target.cnt = (target.cnt + cur_st.cnt) % MOD;
                        long long new_sum = (cur_st.sum * 10 + cur_st.cnt * d) % MOD;
                        target.sum = (target.sum + new_sum) % MOD;
                    }
                }
            }
        }
        cur = next_cur;
    }

    long long total_ans = 0;
    for (int mask = 0; mask < 1024; ++mask) {
        if ((mask & target_mask) == target_mask) {
            for (int less = 0; less < 2; ++less) {
                total_ans = (total_ans + cur[mask][less][1].sum) % MOD;
            }
        }
    }

    cout << total_ans << "\n";
    return 0;
}
```
