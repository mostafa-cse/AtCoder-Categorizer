# Problem Analysis: AtCoder-arc038_c — C. 茶碗と豆 (Bowls and Beans)

**Problem ID**: `AtCoder-arc038_c`  
**Contest**: `arc038`  
**Rating / Difficulty**: 2531  
**URL**: https://atcoder.jp/contests/arc038/tasks/arc038_c  
**VJudge Tag**: `[problem:AtCoder-arc038_c]`  
**Category File**: [`../categories/game_theory/bowls_and_beans_grundy_segment_tree.md`](../categories/game_theory/bowls_and_beans_grundy_segment_tree.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Grundy Number / Nim`  
- **Topic (Skill)**: `Grundy Number and Basic Game Theory`  

---

## 1. Problem Statement & Key Idea
We are given N bowls containing beans. A bean at bowl i can be moved to bowl i - j (1 <= j <= C_i) with at most A_i beans moved in total from bowl i. Determine if the first player has a winning strategy in this impartial game.

## 2. Core Observation & Invariant
Each bean in bowl i moves independently according to the rules of an impartial game, so the game is equivalent to Nim by Sprague-Grundy theorem. The Grundy value g(i) of a bean at bowl i is the mex of Grundy values of bowls reachable in one step: g(i) = mex { g(i - j) | 1 <= j <= C_i }. A bean at bowl i contributes g(i) to the XOR sum if moved an odd number of times; specifically, since beans move independently, bowl i contributes (B_i mod 2) * g(i) to the global Nim sum. To compute g(i) in O(log N) time, maintain the latest occurrence index of each Grundy value in a segment tree, and find the minimum value whose last occurrence is < i - C_i.

## 3. Step-by-Step Algorithm
1. Initialize a segment tree of size N+1 where seg[v] stores the latest index pos where Grundy value v was assigned (initially -1).
2. For i = 1 to N-1: query the segment tree for the minimum Grundy value v whose latest index is strictly less than i - C_i. Set g(i) = v, and update seg[v] = i.
3. Compute total Nim sum as XOR sum of (B_i mod 2) * g(i).
4. If total XOR sum is non-zero, output First; otherwise output Second.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAXV = 100005;
int tree_min[4 * MAXV];

void build(int node, int l, int r) {
    tree_min[node] = -1;
    if (l == r) return;
    int mid = (l + r) / 2;
    build(2 * node, l, mid);
    build(2 * node + 1, mid + 1, r);
}

void update(int node, int l, int r, int idx, int val) {
    if (l == r) {
        tree_min[node] = val;
        return;
    }
    int mid = (l + r) / 2;
    if (idx <= mid) update(2 * node, l, mid, idx, val);
    else update(2 * node + 1, mid + 1, r, idx, val);
    tree_min[node] = min(tree_min[2 * node], tree_min[2 * node + 1]);
}

int query_mex(int node, int l, int r, int threshold) {
    if (l == r) return l;
    int mid = (l + r) / 2;
    if (tree_min[2 * node] < threshold) {
        return query_mex(2 * node, l, mid, threshold);
    } else {
        return query_mex(2 * node + 1, mid + 1, r, threshold);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;

    build(1, 0, N);
    update(1, 0, N, 0, 0); // G(0) = 0 at position 0

    int xor_sum = 0;
    for (int i = 1; i < N; i++) {
        int c;
        long long a;
        cin >> c >> a;
        int threshold = i - c;
        int g_i = query_mex(1, 0, N, threshold);
        update(1, 0, N, g_i, i);
        if (a % 2 == 1) {
            xor_sum ^= g_i;
        }
    }

    if (xor_sum != 0) {
        cout << "First\n";
    } else {
        cout << "Second\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
