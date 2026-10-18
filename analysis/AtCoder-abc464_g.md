# Problem Analysis: AtCoder-abc464_g — G. Celester 2

**Problem ID**: `AtCoder-abc464_g`  
**Contest**: `abc464`  
**Rating / Difficulty**: 2592  
**URL**: https://atcoder.jp/contests/abc464/tasks/abc464_g  
**VJudge Tag**: `[problem:AtCoder-abc464_g]`  
**Category File**: [`../categories/miscellaneous/celester_2_min_plus_convolution.md`](../categories/miscellaneous/celester_2_min_plus_convolution.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Min Plus Convolution`  
- **Topic (Skill)**: `Min Plus Convolution (Convex and Convex)`  

---

## 1. Problem Statement & Key Idea
Given a weather string S of length N ('S' or 'R'), we can flip at most k characters. Happiness is the number of "RS" substrings. For each k = 0, ..., N, find the maximum happiness achievable with at most k flips.

## 2. Core Observation & Invariant
Pad string as S' = 'S' + S + 'R'. Then happiness is (b - 1) / 2, where b is the number of adjacent character differences in S'. Mapping differences to a 01-sequence, flipping a character toggles two adjacent bits. Increasing the number of 1s corresponds to pairing up 0s. The minimum cost to increase happiness by 1 (creating two new 1s) from an array D of distances between adjacent 0s corresponds to choosing non-adjacent elements from D with minimal sum. The cost function is convex, allowing a min-plus convolution / regret greedy algorithm with priority queue and doubly-linked list (Candies algorithm) in O(N log N).

## 3. Step-by-Step Algorithm
1. Pad s = "S" + s + "R". Find all indices where s[i] == s[i+1] (the 0s in the difference array).
2. Compute distances D between adjacent 0s, with large sentinels at ends.
3. Initialize a doubly linked list and min-priority queue over elements in D.
4. Greedily extract the minimum element D[i]: add its cost to total flips, increment happiness by 1, replace D[i] with D[left[i]] + D[right[i]] - D[i], and delete left[i] and right[i] from the linked list.
5. Propagate prefix maximums over res array to answer for each k = 0, ..., N in O(1).
6. Output res[0], ..., res[N].

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;
using pi = pair<int, int>;

void solve() {
    int n;
    string s;
    if (!(cin >> n >> s)) return;
    s = "S" + s + "R";
    int val = 0;
    vector<int> sam;
    for (int i = 0; i <= n; i++) {
        if (s[i] == s[i + 1]) {
            sam.push_back(i);
        } else {
            val++;
        }
    }
    val /= 2;

    vector<int> d;
    d.push_back(1e8);
    d.push_back(1e8);
    for (size_t i = 1; i < sam.size(); i++) {
        d.push_back(sam[i] - sam[i - 1]);
    }
    d.push_back(1e8);
    d.push_back(1e8);

    int dl = d.size();
    priority_queue<pi, vector<pi>, greater<pi>> pq;
    vector<int> lef(dl), rig(dl);
    vector<int> alive(dl, 1);
    for (int i = 0; i < dl; i++) {
        lef[i] = i - 1;
        rig[i] = i + 1;
        pq.push({d[i], i});
    }

    vector<int> res(n + 1, 0);
    int hand = 0;
    res[hand] = val;

    while (val < (n / 2)) {
        if (pq.empty()) break;
        auto od = pq.top();
        pq.pop();
        if (alive[od.second] == 0) continue;
        if (od.first >= 1e7) break; // sentinel

        hand += od.first;
        val++;
        if (hand <= n) {
            res[hand] = max(res[hand], val);
        }

        int el = lef[od.second];
        int er = rig[od.second];
        if (el < 0 || er >= dl) continue;

        d[od.second] = d[el] + d[er] - d[od.second];
        pq.push({d[od.second], od.second});

        alive[el] = 0;
        int x = lef[el], y = rig[el];
        if (y < dl) lef[y] = x;
        if (x >= 0) rig[x] = y;

        alive[er] = 0;
        x = lef[er];
        y = rig[er];
        if (y < dl) lef[y] = x;
        if (x >= 0) rig[x] = y;
    }

    for (int i = 1; i <= n; i++) {
        res[i] = max(res[i], res[i - 1]);
    }
    for (int i = 0; i <= n; i++) {
        cout << res[i] << (i == n ? "" : " ");
    }
    cout << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    if (cin >> T) {
        while (T--) {
            solve();
        }
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
