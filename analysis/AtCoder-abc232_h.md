# Problem Analysis: AtCoder-abc232_h — H - King's Tour

**Problem ID**: `AtCoder-abc232_h`  
**Contest**: `abc232`  
**Rating / Difficulty**: 2780  
**URL**: https://atcoder.jp/contests/abc232/tasks/abc232_h  
**VJudge Tag**: `[problem:AtCoder-abc232_h]`  
**Category File**: [`../categories/basics/king_tour_chessboard_constructive_induction.md`](../categories/basics/king_tour_chessboard_constructive_induction.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Constructive Algorithms`  

---

## 1. Problem Statement & Key Idea
Construct a King's tour on an H x W chessboard that starts at (1, 1), ends at a given target square (A, B), and visits every single square exactly once.

## 2. Core Observation & Invariant
A King can move to any of the 8 adjacent squares. By induction on grid dimensions, we can peel off perimeter rows or columns. For example, if the target (A, B) does not lie in the first column, we can traverse column 1 completely from (1, 1) down to (H, 1), step into (H, 2), and recursively solve on the remaining H x (W - 1) grid. By symmetry (transposing when H > W or reflecting boundaries), we reduce the problem to base cases where H = 2 or H = 3, which admit direct serpentine constructions.

## 3. Step-by-Step Algorithm
1. 1. Implement a recursive solver solve(H, W, A, B) that returns the sequence of visited squares.
2. 2. Ensure H <= W by transposing coordinates if needed.
3. 3. If B > 2, traverse the first column: (1, 1) -> (2, 1) -> ... -> (H, 1), transition to (H, 2), and recurse on the remaining H x (W - 1) board.
4. 4. If B == 2 and A > 2, peel off the first row similarly.
5. 5. When reduced to 2 x W or 3 x 3, use explicit serpentine / zig-zag templates designed to finish at the target square.
6. 6. Transform coordinates back and print the H * W visited squares.

## 4. Complexity Analysis
- **Time Complexity**: `O(H * W)`
- **Space Complexity**: `O(H * W)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

typedef pair<int, int> P;

vector<P> solve(int h, int w, int a, int b) {
    vector<P> ret;
    if (h == 2) {
        for (int i = 1; i <= b - 1; i++) {
            ret.push_back(P(1, i));
            ret.push_back(P(2, i));
        }
        ret.push_back(P(3 - a, b));
        for (int i = b + 1; i <= w; i++) ret.push_back(P(1, i));
        for (int i = w; i >= b + 1; i--) ret.push_back(P(2, i));
        ret.push_back(P(a, b));
    }
    else if ((h > 2 && w == 2) || b == 1 || (a == h && b == 2)) {
        ret = solve(w, h, b, a);
        for (auto &p : ret) swap(p.first, p.second);
    }
    else {
        for (int i = 1; i <= h; i++) ret.push_back(P(i, 1));
        vector<P> res = solve(h, w - 1, h + 1 - a, b - 1);
        for (auto &p : res) {
            p.first = h + 1 - p.first;
            p.second++;
        }
        ret.insert(ret.end(), res.begin(), res.end());
    }
    return ret;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int h, w, a, b;
    if (cin >> h >> w >> a >> b) {
        vector<P> ans = solve(h, w, a, b);
        for (auto p : ans) {
            cout << p.first << " " << p.second << "\n";
        }
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
