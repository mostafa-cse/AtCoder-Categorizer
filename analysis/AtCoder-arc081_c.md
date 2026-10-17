# Problem Analysis: AtCoder-arc081_c — Don't Be a Subsequence

**Problem ID**: `AtCoder-arc081_c`  
**Contest**: `arc081`  
**Rating / Difficulty**: 2072  
**URL**: https://atcoder.jp/contests/arc081/tasks/arc081_c  
**VJudge Tag**: `[problem:AtCoder-arc081_c]`  
**Category File**: [`../categories/dynamic_programming/shortest_non_subsequence_dp.md`](../categories/dynamic_programming/shortest_non_subsequence_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Automaton Transition DAG Shortest Non-Subsequence DP with Lexicographical Greedy Reconstruction`  

---

## 1. Problem Statement & Key Idea
Given a lowercase string A. Find the shortest string that is not a subsequence of A. If multiple such strings exist, find the lexicographically smallest one.

**Key Idea**: Subsequence matching operates as a transition DAG where from index i, choosing character c jumps to the first occurrence j = next_pos(i, c) >= i. Let dp[i] be the minimum length of a non-subsequence of the suffix A[i..|A|]. From index i, if character c does not appear, length is 1; otherwise length is 1 + dp[next_pos(i, c) + 1]. Computing dp backwards in O(26 |A|) gives optimal lengths. We then greedily reconstruct the lexicographically smallest string by picking the smallest character c achieving dp[i].

## 2. Core Observation & Invariant
Subsequence rejection on a string DAG corresponds to the shortest path to an exit state, with lexicographical ties broken greedily from 'a' to 'z'.

## 3. Step-by-Step Algorithm
1. Compute nxt[i][c] = next occurrence of character c at or after position i, working backwards from |A| down to 1.
2. Initialize dp[|A| + 1] = 1.
3. For i from |A| down to 1: dp[i] = min_{c} (1 if nxt[i][c] not found else 1 + dp[nxt[i][c] + 1]).
4. Reconstruct answer: start at cur = 1; while cur <= |A|+1, test c from 'a' to 'z' and pick first c where transition length matches dp[cur]. Advance cur = nxt[cur][c] + 1.
5. Output the reconstructed string.

## 4. Complexity Analysis
- **Time Complexity**: `O(26 * |A|)`
- **Space Complexity**: `O(26 * |A|)`

## 5. Core Algorithmic Skill & Learning Takeaway
Shortest path on a next-occurrence automaton DAG with lexicographical tie-breaking.

**Reusable Pattern**: Shortest non-subsequence: backward DP on character jump DAG followed by greedy forward reconstruction.

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

const int INF = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int n = s.size();
    vector<vector<int>> nxt(n + 2, vector<int>(26, n + 1));

    for (int i = n; i >= 1; --i) {
        for (int c = 0; c < 26; ++c) {
            nxt[i][c] = nxt[i + 1][c];
        }
        nxt[i][s[i - 1] - 'a'] = i;
    }

    vector<int> dp(n + 2, INF);
    dp[n + 1] = 1;

    for (int i = n; i >= 1; --i) {
        for (int c = 0; c < 26; ++c) {
            int p = nxt[i][c];
            if (p == n + 1) {
                dp[i] = 1;
            } else {
                dp[i] = min(dp[i], 1 + dp[p + 1]);
            }
        }
    }

    string ans = "";
    int cur = 1;
    while (cur <= n + 1) {
        for (int c = 0; c < 26; ++c) {
            int p = nxt[cur][c];
            int len = (p == n + 1 ? 1 : 1 + dp[p + 1]);
            if (len == dp[cur]) {
                ans += (char)('a' + c);
                cur = p + 1;
                break;
            }
        }
        if (cur > n) break;
    }

    cout << ans << "\n";
    return 0;
}
```
