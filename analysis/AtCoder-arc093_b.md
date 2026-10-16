# Problem Analysis: AtCoder-arc093_b — Grid Components

**Problem ID**: `AtCoder-arc093_b`  
**Contest**: `abc092`  
**Rating / Difficulty**: 1445  
**URL**: https://atcoder.jp/contests/abc092/tasks/arc093_b  
**VJudge Tag**: `[problem:AtCoder-arc093_b]`  
**Category File**: [`../categories/basics/split_grid_dot_sprinkling.md`](../categories/basics/split_grid_dot_sprinkling.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Constructive Algorithms`  
- **Topic (Skill)**: `Split Half Grid with Isolated Dot Sprinkling`  

---

## 1. Problem Statement & Key Idea
Construct a grid of at most 100 x 100 with cells '#' (black) and '.' (white) such that the number of white connected components is A and black components is B (1 <= A, B <= 500).

**Key Insight**: Split a 100 x 100 grid into top half (all black) and bottom half (all white). Each half initially forms 1 connected component. Sprinkle isolated dots of the opposite color on alternate coordinates to increment the component count by 1 per dot.

## 2. Core Observation & Invariant
A 100x100 grid has 50 rows of black and 50 rows of white. Placing an isolated '.' at (r, c) with even r and even c inside the black half adds exactly 1 white component without connecting to any other dot. We can place up to 25 * 50 = 1250 dots, easily satisfying A, B <= 500.

## 3. Step-by-Step Algorithm
1. Initialize 100x100 grid: rows 0..49 with '#' and rows 50..99 with '.'.
2. To add (A - 1) white components: place '.' at (2 * r, 2 * c) in rows 0..48.
3. To add (B - 1) black components: place '#' at (51 + 2 * r, 2 * c) in rows 51..99.
4. Print dimensions 100 100, then print the grid rows.

## 4. Complexity Analysis
- **Time Complexity**: `O(H * W)`
- **Space Complexity**: `O(H * W)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b;
    if (!(cin >> a >> b)) return 0;

    int h = 100, w = 100;
    vector<string> grid(h, string(w, '.'));

    // Top half black, bottom half white
    for (int r = 0; r < 50; ++r) {
        grid[r] = string(w, '#');
    }

    // Add A - 1 white components into top half
    int white_needed = a - 1;
    for (int r = 0; r < 50 && white_needed > 0; r += 2) {
        for (int c = 0; c < w && white_needed > 0; c += 2) {
            grid[r][c] = '.';
            white_needed--;
        }
    }

    // Add B - 1 black components into bottom half
    int black_needed = b - 1;
    for (int r = 51; r < 100 && black_needed > 0; r += 2) {
        for (int c = 0; c < w && black_needed > 0; c += 2) {
            grid[r][c] = '#';
            black_needed--;
        }
    }

    cout << h << " " << w << "\n";
    for (int r = 0; r < h; ++r) {
        cout << grid[r] << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Independent component generation via alternating parity placement inside a complementary background.
- **Reusable Pattern**: `Grid Component Construction: Top half black + bottom half white, sprinkle isolated dots on (even, even) grid.`
