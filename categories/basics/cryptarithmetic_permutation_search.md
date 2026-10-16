# Cryptarithmetic Permutation Search via std::next_permutation

**Domain**: `Basics`  
**Subtopic**: `Permutations`  

This workbook contains curated, high-quality competitive programming problems teaching **Cryptarithmetic Permutation Search via std::next_permutation**.

---

## Curated Problems

### [problem:AtCoder-abc198_d] — Send More Money
- **Contest**: `abc198`
- **Rating / Difficulty**: 1224
- **Specific Skill**: Cryptarithmetic Permutation Search via std::next_permutation
- **Individual Analysis**: [`../../analysis/AtCoder-abc198_d.md`](../../analysis/AtCoder-abc198_d.md)
- **Problem Statement Summary**: Given three strings S_1, S_2, S_3 representing words. Assign distinct digits 0..9 to each distinct letter such that S_1 + S_2 = S_3, with no leading zeros. If possible, output the numbers, else UNRESOLVABLE.
- **Core Insight**: With <= 10 letters, we can test all permutations of 10 digits assigned to the letters using std::next_permutation: P(10, k) <= 10! = 3,628,800. For each assignment, check if leading letters are non-zero and N_1 + N_2 == N_3.
- **Complexity**: Time: `O(10! / (10 - K)!)` | Space: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <numeric>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s1, s2, s3;
    if (!(cin >> s1 >> s2 >> s3)) return 0;

    set<char> letters_set;
    for (char c : s1) letters_set.insert(c);
    for (char c : s2) letters_set.insert(c);
    for (char c : s3) letters_set.insert(c);

    if (letters_set.size() > 10) {
        cout << "UNRESOLVABLE\n";
        return 0;
    }

    vector<char> letters(letters_set.begin(), letters_set.end());
    int k = letters.size();

    vector<int> p(10);
    iota(p.begin(), p.end(), 0);

    do {
        vector<int> char_to_digit(256, -1);
        for (int i = 0; i < k; ++i) {
            char_to_digit[(unsigned char)letters[i]] = p[i];
        }

        if (char_to_digit[(unsigned char)s1[0]] == 0 ||
            char_to_digit[(unsigned char)s2[0]] == 0 ||
            char_to_digit[(unsigned char)s3[0]] == 0) {
            continue;
        }

        long long n1 = 0, n2 = 0, n3 = 0;
        for (char c : s1) n1 = n1 * 10 + char_to_digit[(unsigned char)c];
        for (char c : s2) n2 = n2 * 10 + char_to_digit[(unsigned char)c];
        for (char c : s3) n3 = n3 * 10 + char_to_digit[(unsigned char)c];

        if (n1 + n2 == n3) {
            cout << n1 << "\n" << n2 << "\n" << n3 << "\n";
            return 0;
        }
    } while (next_permutation(p.begin(), p.end()));

    cout << "UNRESOLVABLE\n";
    return 0;
}
```
