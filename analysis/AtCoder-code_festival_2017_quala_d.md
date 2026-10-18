# Problem Analysis: AtCoder-code_festival_2017_quala_d — D. Four Coloring

**Problem ID**: `AtCoder-code_festival_2017_quala_d`  
**Contest**: `code-festival-2017-quala`  
**Rating / Difficulty**: 2445  
**URL**: https://atcoder.jp/contests/code-festival-2017-quala/tasks/code_festival_2017_quala_d  
**VJudge Tag**: `[problem:AtCoder-code_festival_2017_quala_d]`  
**Category File**: [`../categories/miscellaneous/four_coloring_manhattan_chebyshev_rotation.md`](../categories/miscellaneous/four_coloring_manhattan_chebyshev_rotation.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Techniques`  
- **Topic (Skill)**: `Manhattan <> Chebyshev`  

---

## 1. Problem Statement & Key Idea
Color an $H \times W$ grid ($H, W \le 500$) with 4 colors such that no two squares at Manhattan distance $d$ have the same color. Rotating coordinates by 45 degrees transforms Manhattan distance $|i_1 - i_2| + |j_1 - j_2| = d$ into Chebyshev distance $\max(|u_1 - u_2|, |v_1 - v_2|) = d$, where $u = i + j$ and $v = i - j$. Tiling the $(u, v)$ plane into $d \times d$ squares colored periodically with a $2 \times 2$ pattern of 4 colors completely avoids distance $d$ within identical colors.

## 2. Core Observation & Invariant
Any two points sharing the same color must have $U_1 \equiv U_2 \pmod 2$ and $V_1 \equiv V_2 \pmod 2$, meaning $|u_1 - u_2|$ and $|v_1 - v_2|$ are never equal to $d$ (they are either $< d$ or $> d$).

## 3. Step-by-Step Algorithm
1. 1. For each square $(i, j)$ in the $H \times W$ grid, compute rotated coordinates $u = i + j$ and $v = i - j + 10^6 d$ (with offset to ensure positivity).
2. 2. Compute tile coordinates $U = \lfloor u / d \rfloor$ and $V = \lfloor v / d \rfloor$.
3. 3. Assign color index $c\_idx = (U \bmod 2) \times 2 + (V \bmod 2)$ mapped to {'R', 'Y', 'G', 'B'}.
4. 4. Output the resulting $H \times W$ character grid.

## 4. Complexity Analysis
- **Time Complexity**: `O(H W)`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int H, W, d;
    if (!(cin >> H >> W >> d)) return 0;

    const char colors[4] = {'R', 'Y', 'G', 'B'};
    long long OFFSET = 1000000LL * d;

    for (int i = 0; i < H; ++i) {
        string row = "";
        for (int j = 0; j < W; ++j) {
            long long u = i + j;
            long long v = i - j + OFFSET;
            int U = (u / d) % 2;
            int V = (v / d) % 2;
            int c_idx = U * 2 + V;
            row += colors[c_idx];
        }
        cout << row << "\n";
    }
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
