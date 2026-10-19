# Problem Analysis: AtCoder-abc296_h — Ex - Unite

**Problem ID**: `AtCoder-abc296_h`  
**Contest**: `abc296`  
**Rating / Difficulty**: 2822  
**URL**: https://atcoder.jp/contests/abc296/tasks/abc296_h  
**VJudge Tag**: `[problem:AtCoder-abc296_h]`  
**Category File**: [`../categories/miscellaneous/grid_connected_component_plug_profile_dp.md`](../categories/miscellaneous/grid_connected_component_plug_profile_dp.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `General`  
- **Topic (Skill)**: `Broken Profile DP / Plug DP`  

---

## 1. Problem Statement & Key Idea
Given an N x M grid (M <= 7) with black and white cells containing at least one black cell, find the minimum number of white cells to paint black so that all black cells form a single connected component.

## 2. Core Observation & Invariant
Because M <= 7, this is a canonical Broken Profile / Plug DP problem. When processing cell by cell (i, j), we maintain the connectivity profile of the frontier of length M+1 (the latest cell of each column). The partition of frontier black cells into connected components has at most B_7 = 877 states, which can be canonically renumbered. As cells are colored black or left white, components are merged or closed. A closed component cannot be abandoned if there are remaining original black cells.

## 3. Step-by-Step Algorithm
1. 1. Generate all canonical frontier partition states for each boundary cut j in 0..M-1.
2. 2. Initialize DP table dp[state] = 0 for empty frontier state.
3. 3. For each cell (i, j) in row-major order, transition to cell (i, j+1) by considering both decisions (keep white if allowed, or paint black):
4.    a. If keeping white, ensure no isolated black component in the frontier is prematurely abandoned if further black cells exist.
5.    b. If painting black, connect with adjacent left and top frontier plugs and renumber the partition.
6. 4. At the grid end, take the minimum cost among states with at most 1 connected component.
7. 5. Subtract the original number of black cells to obtain newly painted cells.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * M * States)`
- **Space Complexity**: `O(States)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

#define rep(i, n) for(int i = 0; i < (n); ++i)
#define M 7
#define INF (int)1e9

int n, m;
vector<vector<int>> state[M];
map<vector<int>, int> rev[M];
vector<int> tmp;

void make_state(int cut, int k, bool pre, int nxt) {
    if (k == m) {
        rev[cut][tmp] = state[cut].size();
        state[cut].push_back(tmp);
        return;
    }
    tmp.push_back(0);
    make_state(cut, k + 1, false, nxt);
    tmp.pop_back();
    if (pre && (k != cut)) {
        tmp.push_back(tmp[k]);
        make_state(cut, k + 1, true, nxt);
        tmp.pop_back();
    } else {
        rep(i, nxt) {
            tmp.push_back(i + 1);
            make_state(cut, k + 1, true, max(nxt, i + 2));
            tmp.pop_back();
        }
    }
}

void renumbering() {
    int sz = tmp.size();
    int c[10], nxt = 1;
    rep(i, 10) c[i] = 0;
    rep(i, sz) {
        if (tmp[i] > 0) {
            if (c[tmp[i]] == 0) {
                c[tmp[i]] = nxt;
                nxt++;
            }
            tmp[i] = c[tmp[i]];
        }
    }
}

int judge(int k) {
    int sz = tmp.size();
    int cnt = 0, mx = 0;
    rep(i, sz) {
        mx = max(mx, tmp[i]);
        if (tmp[i] == tmp[k]) cnt++;
    }
    if (cnt > 1) return 0;
    if (mx > 1) return -1;
    return 1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> n >> m)) return 0;

    vector<string> s(n);
    int mx = 0;
    int cnt = 0;
    int ans = INF;

    rep(i, n) {
        cin >> s[i];
        rep(j, m) {
            if (s[i][j] == '#') {
                mx = max(mx, i * m + j);
                cnt++;
            }
        }
    }

    tmp.push_back(0);
    rep(j, m) make_state(j, 0, false, 1);

    int sz = state[0].size();
    vector<int> dp(sz, INF), dp2;
    dp[0] = 0;

    rep(i, n) {
        rep(j, m) {
            int nxt_sz = state[(j + 1) % m].size();
            dp2.assign(nxt_sz, INF);
            sz = state[j].size();
            rep(idx, sz) {
                if (dp[idx] >= INF) continue;
                tmp = state[j][idx];
                if ((tmp[j] == 0) && (tmp[j + 1] == 0)) {
                    if (s[i][j] == '.') {
                        int to = rev[(j + 1) % m][tmp];
                        dp2[to] = min(dp2[to], dp[idx]);
                    }
                    tmp[j + 1] = 9;
                    renumbering();
                    int to = rev[(j + 1) % m][tmp];
                    dp2[to] = min(dp2[to], dp[idx] + 1);
                } else if ((tmp[j] == 0) && (tmp[j + 1] > 0)) {
                    if (s[i][j] == '.') {
                        int x = judge(j + 1);
                        if (x == 0) {
                            tmp[j + 1] = 0;
                            renumbering();
                            int to = rev[(j + 1) % m][tmp];
                            dp2[to] = min(dp2[to], dp[idx]);
                        }
                        if ((x == 1) && ((i * m + j) >= mx)) {
                            ans = min(ans, dp[idx]);
                        }
                    }
                    tmp = state[j][idx];
                    int to = rev[(j + 1) % m][tmp];
                    dp2[to] = min(dp2[to], dp[idx] + 1);
                } else if ((tmp[j] > 0) && (tmp[j + 1] == 0)) {
                    if (s[i][j] == '.') {
                        int to = rev[(j + 1) % m][tmp];
                        dp2[to] = min(dp2[to], dp[idx]);
                    }
                    tmp[j + 1] = tmp[j];
                    int to = rev[(j + 1) % m][tmp];
                    dp2[to] = min(dp2[to], dp[idx] + 1);
                } else if (tmp[j] == tmp[j + 1]) {
                    if (s[i][j] == '.') {
                        tmp[j + 1] = 0;
                        int to = rev[(j + 1) % m][tmp];
                        dp2[to] = min(dp2[to], dp[idx]);
                    }
                    tmp = state[j][idx];
                    int to = rev[(j + 1) % m][tmp];
                    dp2[to] = min(dp2[to], dp[idx] + 1);
                } else {
                    if (s[i][j] == '.') {
                        int x = judge(j + 1);
                        if (x == 0) {
                            tmp[j + 1] = 0;
                            renumbering();
                            int to = rev[(j + 1) % m][tmp];
                            dp2[to] = min(dp2[to], dp[idx]);
                        }
                        if ((x == 1) && ((i * m + j) >= mx)) {
                            ans = min(ans, dp[idx]);
                        }
                    }
                    tmp = state[j][idx];
                    int x = tmp[j + 1];
                    rep(ii, m + 1) {
                        if (tmp[ii] == x) tmp[ii] = tmp[j];
                    }
                    renumbering();
                    int to = rev[(j + 1) % m][tmp];
                    dp2[to] = min(dp2[to], dp[idx] + 1);
                }
            }
            dp = move(dp2);
        }
    }

    sz = dp.size();
    rep(idx, sz) {
        if (dp[idx] >= INF) continue;
        int x = 0;
        rep(j, m + 1) x = max(x, state[0][idx][j]);
        if (x <= 1) {
            ans = min(ans, dp[idx]);
        }
    }

    cout << (ans - cnt) << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
