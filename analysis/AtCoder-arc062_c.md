# Problem Analysis: AtCoder-arc062_c — Building Cubes with AtCoDeer

**Problem ID**: `AtCoder-arc062_c`  
**Contest**: `arc062`  
**Rating / Difficulty**: 2655  
**URL**: https://atcoder.jp/contests/arc062/tasks/arc062_c  
**VJudge Tag**: `[problem:AtCoder-arc062_c]`  
**Category File**: [`../categories/miscellaneous/cube_coloring_3d_rotations.md`](../categories/miscellaneous/cube_coloring_3d_rotations.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `General`  
- **Topic (Skill)**: `Burnside's Lemma / Polya Enumeration Theorem`  

---

## 1. Problem Statement & Key Idea
Count distinct 3D cubes formed by 6 distinct oriented square tiles up to the 24 rotations of the octahedral group by canonically fixing the tile with the minimal index on the top face in standard orientation, uniquely fixing all remaining face requirements.

## 2. Core Observation & Invariant
In every valid cube of 6 distinct tiles, exactly one tile has the minimum index i. Rotating the cube so tile i is on the top face in rotation 0 is unique. Iterating over bottom tile j (with j > i) and its 4 rotations fixes the 4 corner colors of all 4 side faces. Side faces are counted independently via a precomputed frequency map of canonical tile rotations, yielding exact O(N^2) enumeration.

## 3. Step-by-Step Algorithm
1. 1. For each tile, determine its canonical rotation (lexicographically smallest cyclic shift) and rotation symmetry period (1, 2, or 4).
2. 2. For each tile i from 0 to N-1, build frequency map of canonical tiles with indices > i.
3. 3. For each bottom tile j > i and each of its 4 rotations, compute the 4 required side face 4-tuples.
4. 4. Multiply the number of available matching tiles for each required side face canonical class.
5. 5. Sum valid configurations across all pairs (i, j, r) and print the total.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <array>
#include <algorithm>
#include <unordered_map>
#include <cstdint>

using namespace std;

using Tile = array<int, 4>;

uint64_t encode(const Tile& t) {
    uint64_t res = 0;
    for (int i = 0; i < 4; ++i) {
        res = res * 1000ULL + t[i];
    }
    return res;
}

Tile canonical(const Tile& t) {
    Tile best = t;
    for (int k = 1; k < 4; ++k) {
        Tile cur = {t[k], t[(k + 1) % 4], t[(k + 2) % 4], t[(k + 3) % 4]};
        if (cur < best) best = cur;
    }
    return best;
}

int weight(const Tile& t) {
    Tile r1 = {t[1], t[2], t[3], t[0]};
    Tile r2 = {t[2], t[3], t[0], t[1]};
    Tile r3 = {t[3], t[0], t[1], t[2]};
    if (t == r1 && t == r2 && t == r3) return 4;
    if (t == r2 && r1 == r3) return 2;
    return 1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<Tile> tiles(N);
    vector<Tile> canon_tiles(N);
    vector<uint64_t> canon_ids(N);

    for (int i = 0; i < N; ++i) {
        for (int k = 0; k < 4; ++k) {
            cin >> tiles[i][k];
        }
        canon_tiles[i] = canonical(tiles[i]);
        canon_ids[i] = encode(canon_tiles[i]);
    }

    long long total_cubes = 0;

    for (int i = 0; i < N; ++i) {
        // Count available canonical tiles strictly with index > i
        unordered_map<uint64_t, int> canon_count;
        canon_count.reserve((N - 1 - i) * 2);
        for (int k = i + 1; k < N; ++k) {
            canon_count[canon_ids[k]]++;
        }

        const Tile& v = tiles[i];

        for (int j = i + 1; j < N; ++j) {
            const Tile& tj = tiles[j];
            uint64_t cj_id = canon_ids[j];

            for (int r = 0; r < 4; ++r) {
                int u0 = tj[r];
                int u3 = tj[(r + 1) % 4];
                int u2 = tj[(r + 2) % 4];
                int u1 = tj[(r + 3) % 4];

                array<Tile, 4> S = {
                    Tile{v[1], v[0], u0, u1},
                    Tile{v[2], v[1], u1, u2},
                    Tile{v[3], v[2], u2, u3},
                    Tile{v[0], v[3], u3, u0}
                };

                long long ways = 1;
                for (int k = 0; k < 4; ++k) {
                    ways *= weight(S[k]);
                }

                array<uint64_t, 4> C;
                for (int k = 0; k < 4; ++k) {
                    C[k] = encode(canonical(S[k]));
                }

                // Count frequencies of each needed canonical class
                // At most 4 distinct classes
                uint64_t distinct_C[4];
                int need[4] = {0, 0, 0, 0};
                int d_cnt = 0;

                for (int k = 0; k < 4; ++k) {
                    bool found = false;
                    for (int d = 0; d < d_cnt; ++d) {
                        if (distinct_C[d] == C[k]) {
                            need[d]++;
                            found = true;
                            break;
                        }
                    }
                    if (!found) {
                        distinct_C[d_cnt] = C[k];
                        need[d_cnt] = 1;
                        d_cnt++;
                    }
                }

                bool possible = true;
                for (int d = 0; d < d_cnt; ++d) {
                    auto it = canon_count.find(distinct_C[d]);
                    int avail = (it != canon_count.end()) ? it->second : 0;
                    if (cj_id == distinct_C[d]) {
                        avail--;
                    }
                    if (avail < need[d]) {
                        possible = false;
                        break;
                    }
                    for (int p = 0; p < need[d]; ++p) {
                        ways *= (avail - p);
                    }
                }

                if (possible) {
                    total_cubes += ways;
                }
            }
        }
    }

    cout << total_cubes << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
