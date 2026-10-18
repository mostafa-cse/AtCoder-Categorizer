# Problem Analysis: AtCoder-abc175_f — F. Making Palindrome

**Problem ID**: `AtCoder-abc175_f`  
**Contest**: `abc175`  
**Rating / Difficulty**: 2512  
**URL**: https://atcoder.jp/contests/abc175/tasks/abc175_f  
**VJudge Tag**: `[problem:AtCoder-abc175_f]`  
**Category File**: [`../categories/graph_theory/making_palindrome_palindromic_residual_dijkstra.md`](../categories/graph_theory/making_palindrome_palindromic_residual_dijkstra.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Shortest Paths`  
- **Topic (Skill)**: `Dijkstra's Algorithm`  

---

## 1. Problem Statement & Key Idea
Find minimum cost to concatenate a sequence of strings from $S_1, \dots, S_N$ (with costs $C_i$) to form a palindrome. View palindrome formation as canceling characters inward from left and right boundaries. The state of the system is the unmatched residual string: either a suffix of $S_i$ remaining on the left, or a prefix of $S_i$ remaining on the right. Concatenating a string $S_k$ on the opposite side cancels matching characters and transitions to a new residual. Dijkstra's algorithm finds the shortest path from single-string initial states to any state whose residual is itself a palindrome.

## 2. Core Observation & Invariant
The residual is always a proper suffix or prefix of one of the original strings $S_i$. With $N \le 50$ and $|S_i| \le 20$, there are at most $2 \sum |S_i| \le 2000$ states. From each state, trying all $N$ transitions explores at most $10^5$ directed edges.

## 3. Step-by-Step Algorithm
1. 1. Represent states as `(side, i, j)` where `side = 0` is suffix $S_i[j \dots]$, and `side = 1` is prefix $S_i[\dots j]$.
2. 2. For each string $S_i$, if $S_i$ is a palindrome, initialize $ans = \min(ans, C_i)$.
3. 3. Push initial states `(0, i, 0)` with distance $C_i$ into priority queue.
4. 4. While priority queue is not empty:
5.    a. Pop `(d, side, i, j)`. If residual is a palindrome, update $ans = \min(ans, d)$.
6.    b. If `side == 0` (residual on left): try appending $S_k$ on the right. Match characters between $S_i[j \dots]$ and $S_k$ in reverse. If they match, transition to the new leftover suffix on left or prefix on right.
7.    c. If `side == 1` (residual on right): try prepending $S_k$ on the left. Match characters between $S_k$ and $S_i[\dots j]$ in reverse. If they match, transition to the new leftover prefix on right or suffix on left.
8. 5. Output $ans$ or -1 if unreachable.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \sum |S_i| \log(N \sum |S_i|))`
- **Space Complexity**: `O(N \sum |S_i|)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <tuple>
#include <algorithm>

using namespace std;

bool is_palindrome(const string& s) {
    int l = 0, r = (int)s.size() - 1;
    while (l < r) {
        if (s[l] != s[r]) return false;
        l++;
        r--;
    }
    return true;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<string> s(n);
    vector<long long> c(n);
    for (int i = 0; i < n; ++i) {
        cin >> s[i] >> c[i];
    }

    long long ans = -1;
    for (int i = 0; i < n; ++i) {
        if (is_palindrome(s[i])) {
            if (ans == -1 || c[i] < ans) {
                ans = c[i];
            }
        }
    }

    // State representation: side (0 = suffix left, 1 = prefix right), string index i, position j
    // dist: side -> i -> j -> dist
    // side 0: j from 0 to |S_i| - 1
    // side 1: j from 1 to |S_i|
    vector<vector<vector<long long>>> dist(2);
    dist[0].resize(n);
    dist[1].resize(n);
    for (int i = 0; i < n; ++i) {
        dist[0][i].assign(s[i].size() + 1, -1);
        dist[1][i].assign(s[i].size() + 1, -1);
    }

    typedef tuple<long long, int, int, int> State;
    priority_queue<State, vector<State>, greater<State>> pq;

    for (int i = 0; i < n; ++i) {
        dist[0][i][0] = c[i];
        pq.push({c[i], 0, i, 0});
    }

    while (!pq.empty()) {
        auto [d, side, i, j] = pq.top();
        pq.pop();

        if (d > dist[side][i][j]) continue;

        string rem = (side == 0) ? s[i].substr(j) : s[i].substr(0, j);
        if (is_palindrome(rem)) {
            if (ans == -1 || d < ans) {
                ans = d;
            }
        }

        if (side == 0) {
            // Remainder on left: s[i][j...]
            int rem_len = (int)s[i].size() - j;
            for (int k = 0; k < n; ++k) {
                int sk_len = s[k].size();
                int common = min(rem_len, sk_len);
                bool match = true;
                for (int t = 0; t < common; ++t) {
                    if (s[i][j + t] != s[k][sk_len - 1 - t]) {
                        match = false;
                        break;
                    }
                }
                if (!match) continue;

                if (rem_len >= sk_len) {
                    int nxt_side = 0;
                    int nxt_i = i;
                    int nxt_j = j + sk_len;
                    long long nd = d + c[k];
                    if (dist[nxt_side][nxt_i][nxt_j] == -1 || nd < dist[nxt_side][nxt_i][nxt_j]) {
                        dist[nxt_side][nxt_i][nxt_j] = nd;
                        pq.push({nd, nxt_side, nxt_i, nxt_j});
                    }
                } else {
                    int nxt_side = 1;
                    int nxt_i = k;
                    int nxt_j = sk_len - rem_len;
                    long long nd = d + c[k];
                    if (dist[nxt_side][nxt_i][nxt_j] == -1 || nd < dist[nxt_side][nxt_i][nxt_j]) {
                        dist[nxt_side][nxt_i][nxt_j] = nd;
                        pq.push({nd, nxt_side, nxt_i, nxt_j});
                    }
                }
            }
        } else {
            // Remainder on right: s[i][0...j-1]
            int rem_len = j;
            for (int k = 0; k < n; ++k) {
                int sk_len = s[k].size();
                int common = min(rem_len, sk_len);
                bool match = true;
                for (int t = 0; t < common; ++t) {
                    if (s[k][t] != s[i][j - 1 - t]) {
                        match = false;
                        break;
                    }
                }
                if (!match) continue;

                if (rem_len >= sk_len) {
                    int nxt_side = 1;
                    int nxt_i = i;
                    int nxt_j = j - sk_len;
                    long long nd = d + c[k];
                    if (dist[nxt_side][nxt_i][nxt_j] == -1 || nd < dist[nxt_side][nxt_i][nxt_j]) {
                        dist[nxt_side][nxt_i][nxt_j] = nd;
                        pq.push({nd, nxt_side, nxt_i, nxt_j});
                    }
                } else {
                    int nxt_side = 0;
                    int nxt_i = k;
                    int nxt_j = rem_len;
                    long long nd = d + c[k];
                    if (dist[nxt_side][nxt_i][nxt_j] == -1 || nd < dist[nxt_side][nxt_i][nxt_j]) {
                        dist[nxt_side][nxt_i][nxt_j] = nd;
                        pq.push({nd, nxt_side, nxt_i, nxt_j});
                    }
                }
            }
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
