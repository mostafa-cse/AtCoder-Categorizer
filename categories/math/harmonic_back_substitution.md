# Reverse Multiples Harmonic Greedy / Back-Substitution

**Domain**: `Math`  
**Subtopic**: `Constructive Algorithms`  

This workbook contains curated, high-quality competitive programming problems teaching **Reverse Multiples Harmonic Greedy / Back-Substitution**.

---

## Curated Problems

### [problem:AtCoder-abc134_d] — Preparing Boxes
- **Contest**: `abc134`
- **Rating / Difficulty**: 926
- **Specific Skill**: Reverse Multiples Harmonic Greedy / Back-Substitution
- **Individual Analysis**: [`../../analysis/AtCoder-abc134_d.md`](../../analysis/AtCoder-abc134_d.md)
- **Problem Statement Summary**: N boxes numbered 1..N. Choose whether to place a ball in box i (b_i in {0, 1}). For each i, the total balls in boxes that are multiples of i must have parity a_i. Output a valid assignment.
- **Core Insight**: Determining b_i in decreasing order from N down to 1: when deciding b_i, all strict multiples 2i, 3i, 4i... have already been determined! Therefore, b_i is uniquely forced: b_i = (a_i XOR sum_{k >= 2} b_{k*i}) % 2. Total steps across all i is sum N/i = O(N log N).
- **Complexity**: Time: `O(N log N)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    vector<int> b(n + 1, 0);
    vector<int> chosen;

    for (int i = n; i >= 1; --i) {
        int sum = 0;
        for (int j = 2 * i; j <= n; j += i) {
            sum ^= b[j];
        }
        b[i] = a[i] ^ sum;
        if (b[i] == 1) {
            chosen.push_back(i);
        }
    }

    cout << chosen.size() << "\n";
    for (size_t i = 0; i < chosen.size(); ++i) {
        cout << chosen[i] << (i + 1 == chosen.size() ? '\n' : ' ');
    }

    return 0;
}
```
