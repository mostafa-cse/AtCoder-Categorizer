# Knapsack and Basic Dynamic Programming

**Domain**: `Dynamic Programming (DP)`  
**Subtopic**: `Intro to DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Knapsack and Basic Dynamic Programming**.

---

## Curated Problems

### `[problem:AtCoder-abc230_f]` — Predilection
- **Rating / Difficulty**: 2113
- **Contest**: `abc230`
- **Analysis**: [`analysis/AtCoder-abc230_f.md`](../../analysis/AtCoder-abc230_f.md)
- **Key Idea**: Merging adjacent elements partitions the prefix sums into a chosen subset of prefix sums S_1, S_2, ..., S_{N-1} (with S_N fixed as the total sum). Two partitions result in the exact same array if and only if they select the exact same subsequence of prefix sum values! Thus, the problem is isomorphic to counting the number of distinct subsequences of the prefix sum sequence S[1..N-1]. This is solved via classic distinct subsequence DP using a hash map storing the last DP value for each prefix sum value.
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <map>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    vector<long long> pref(n + 1, 0);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        pref[i + 1] = pref[i] + a[i];
    }

    map<long long, long long> last_val_dp;
    long long total_subseq = 1;

    for (int i = 1; i < n; ++i) {
        long long val = pref[i];
        long long new_subseq = total_subseq;
        long long prev_for_val = last_val_dp[val];
        long long added = (new_subseq - prev_for_val + MOD) % MOD;
        total_subseq = (total_subseq + added) % MOD;
        last_val_dp[val] = new_subseq;
    }

    cout << total_subseq << "\n";
    return 0;
}
```
