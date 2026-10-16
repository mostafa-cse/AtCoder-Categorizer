# Split Half Grid with Isolated Dot Sprinkling

**Domain**: `Basics`  
**Subtopic**: `Constructive Algorithms`  

This workbook contains curated, high-quality competitive programming problems teaching **Split Half Grid with Isolated Dot Sprinkling**.

---

## Curated Problems

### `[problem:AtCoder-arc093_b]` — Grid Components
- **Rating / Difficulty**: 1445
- **Contest**: `abc092`
- **Analysis**: [`analysis/AtCoder-arc093_b.md`](../../analysis/AtCoder-arc093_b.md)
- **Key Idea**: Split a 100 x 100 grid into top half (all black) and bottom half (all white). Each half initially forms 1 connected component. Sprinkle isolated dots of the opposite color on alternate coordinates to increment the component count by 1 per dot.
- **Time Complexity**: `O(H * W)`
- **Space Complexity**: `O(H * W)`
- **Verified C++ Implementation**:
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
