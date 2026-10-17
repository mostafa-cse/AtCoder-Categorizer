# Problem Analysis: AtCoder-arc170_d — D. Triangle Card Game

**Problem ID**: `AtCoder-arc170_d`  
**Contest**: `arc170`  
**Rating / Difficulty**: 2279  
**URL**: https://atcoder.jp/contests/arc170/tasks/arc170_d  
**VJudge Tag**: `[problem:AtCoder-arc170_d]`  
**Category File**: [`../categories/game_theory/triangle_card_game_minimax_distance_gap_search.md`](../categories/game_theory/triangle_card_game_minimax_distance_gap_search.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Grundy Number / Nim`  
- **Topic (Skill)**: `Grundy Number and Basic Game Theory`  

---

## 1. Problem Statement & Key Idea
Alice chooses a card $A_i$, then Bob chooses $B_j$, then Alice chooses $A_k$ ($k \neq i$). Alice wins if the three lengths form a non-degenerate triangle. Determine if Alice can guarantee a win with optimal play.

## 2. Core Observation & Invariant
For an opening card $a \in A$, Bob can win if and only if either playing $B_{\min}$ prevents any triangle ($|a - B_{\min}| < c < a + B_{\min}$ has count 0 in $A \setminus \{a\}$), or there exists $b \in B$ whose distance to $A \setminus \{a\}$ is at least $a$. Alice wins if she has any opening move where Bob cannot win.

## 3. Step-by-Step Algorithm
1. 1. Triangle condition for $(a, b, c)$ is $|a - b| < c < a + b$. Alice chooses $a$, Bob chooses $b$, then Alice chooses $c \in A \setminus \{a\}$. Alice wins if she can find any valid $c$.\n2. For Bob to win against $a$: Bob must pick $b$ such that NO $c \in A \setminus \{a\}$ satisfies $|a - b| < c < a + b$. If $b < a$, Bob is always best off playing his minimum card $b = B_{\min}$. Thus condition 1 is: no $c \in A \setminus \{a\}$ lies in $(|a - B_{\min}|, a + B_{\min})$.\n3. If $b \ge a$, Bob wins if $\min_{c \in A \setminus \{a\}} |b - c| \ge a$. Let $d_1(b)$ be the distance from $b$ to its closest neighbor in $A$, and $d_2(b)$ to its second closest neighbor.\n4. The maximum distance in $A \setminus \{a\}$ is $\max(global\_mx, max\_d2[a])$, where $global\_mx = \max_{b} d_1(b)$ and $max\_d2[a]$ is the maximum $d_2(b)$ over $b$ whose unique closest neighbor is $a$.\n5. Bob wins against $a$ if condition 1 or condition 2 holds. If there is any $a$ where Bob loses both, Alice wins. Time complexity per test case is $O(N \log N)$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

void solve_test() {
    int n;
    if (!(cin >> n)) return;

    vector<long long> a(n), b(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < n; i++) cin >> b[i];

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    long long b_min = b[0];

    long long global_mx = 0;
    vector<long long> max_d2(n, 0);

    for (int i = 0; i < n; i++) {
        long long val = b[i];
        int pos = lower_bound(a.begin(), a.end(), val) - a.begin();

        vector<pair<long long, int>> cands;
        for (int offset = -2; offset <= 2; offset++) {
            int idx = pos + offset;
            if (idx >= 0 && idx < n) {
                cands.push_back({abs(val - a[idx]), idx});
            }
        }
        sort(cands.begin(), cands.end());

        long long d1 = cands[0].first;
        int idx1 = cands[0].second;
        long long d2 = (cands.size() > 1 ? cands[1].first : d1);

        global_mx = max(global_mx, d1);
        max_d2[idx1] = max(max_d2[idx1], d2);
    }

    bool alice_wins = false;

    for (int i = 0; i < n; i++) {
        long long cur_a = a[i];

        long long low = abs(cur_a - b_min);
        long long high = cur_a + b_min;

        int cnt = upper_bound(a.begin(), a.end(), high - 1) - upper_bound(a.begin(), a.end(), low);
        if (low < cur_a && cur_a < high) {
            cnt--;
        }

        bool bob_wins_cond1 = (cnt == 0);
        long long max_dist = max(global_mx, max_d2[i]);
        bool bob_wins_cond2 = (max_dist >= cur_a);

        if (!bob_wins_cond1 && !bob_wins_cond2) {
            alice_wins = true;
            break;
        }
    }

    if (alice_wins) {
        cout << "Alice\n";
    } else {
        cout << "Bob\n";
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    if (cin >> t) {
        while (t--) {
            solve_test();
        }
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
