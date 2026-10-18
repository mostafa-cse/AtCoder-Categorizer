# Problem Analysis: AtCoder-code_formula_2014_final_g — G. ノイハの塔 (Tower of Neuha)

**Problem ID**: `AtCoder-code_formula_2014_final_g`  
**Contest**: `code-formula-2014-final`  
**Rating / Difficulty**: 2588  
**URL**: https://atcoder.jp/contests/code-formula-2014-final/tasks/code_formula_2014_final_g  
**VJudge Tag**: `[problem:AtCoder-code_formula_2014_final_g]`  
**Category File**: [`../categories/basics/tower_of_neuha_divide_and_conquer.md`](../categories/basics/tower_of_neuha_divide_and_conquer.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Divide and Conquer`  
- **Topic (Skill)**: `Divide and Conquer`  

---

## 1. Problem Statement & Key Idea
Given 3 pegs and N disks (N <= 10,000) stacked on peg 1 in arbitrary order, move disks one at a time between pegs (any disk can be placed on top of any other) to sort all disks on any peg with largest at the bottom and smallest at the top, using at most 225,000 moves.

## 2. Core Observation & Invariant
This can be solved by divide-and-conquer on 3 stacks in O(N log N) moves. To sort a range of disks [L, R] currently on peg src onto peg dest (with largest at bottom): partition the disks around midpoint mid = (L + R) / 2 by popping them from src and routing disks <= mid to aux_small and disks > mid to aux_large. Then recursively sort the larger disks [mid + 1, R] from aux_large onto dest (they land at the bottom of dest). Finally, recursively sort the smaller disks [L, mid] from aux_small onto dest (they land on top of the larger disks). The total moves satisfy T(N) = 2 T(N/2) + N, which for N = 10,000 requires only ~139,000 moves, well below the 225,000 limit.

## 3. Step-by-Step Algorithm
1. Implement function sort_range(L, R, src, dest):
2. If L == R: if src != dest, move disk from src to dest; return.
3. Let mid = (L + R) / 2.
4. Identify the two auxiliary pegs p_small and p_large (the two pegs distinct from src). If p_small == dest, swap(p_small, p_large) so larger disks route directly toward dest.
5. Pop R - L + 1 disks from src: if disk <= mid, move to p_small; else move to p_large.
6. Recursively call sort_range(mid + 1, R, p_large, dest) to sort larger disks onto dest.
7. Recursively call sort_range(L, mid, p_small, dest) to sort smaller disks on top of them on dest.
8. Initially call sort_range(1, N, 1, 1).
9. Output move count M followed by all (u, v) pairs.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N) moves and time (~139,000 moves)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

vector<int> pegs[4];
vector<pair<int, int>> moves;

void do_move(int u, int v) {
    int disk = pegs[u].back();
    pegs[u].pop_back();
    pegs[v].push_back(disk);
    moves.push_back({u, v});
}

void sort_range(int L, int R, int src, int dest) {
    if (L == R) {
        if (src != dest) {
            do_move(src, dest);
        }
        return;
    }

    int mid = L + (R - L) / 2;

    int p_small = -1, p_large = -1;
    for (int p = 1; p <= 3; p++) {
        if (p != src) {
            if (p_small == -1) p_small = p;
            else p_large = p;
        }
    }

    if (p_small == dest) {
        swap(p_small, p_large);
    }

    int count = R - L + 1;
    for (int i = 0; i < count; i++) {
        int disk = pegs[src].back();
        if (disk <= mid) {
            do_move(src, p_small);
        } else {
            do_move(src, p_large);
        }
    }

    sort_range(mid + 1, R, p_large, dest);
    sort_range(L, mid, p_small, dest);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;

    pegs[1].resize(N);
    for (int i = 0; i < N; i++) {
        cin >> pegs[1][i];
    }

    moves.reserve(230000);
    sort_range(1, N, 1, 1);

    cout << moves.size() << "\n";
    for (const auto& m : moves) {
        cout << m.first << " " << m.second << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
