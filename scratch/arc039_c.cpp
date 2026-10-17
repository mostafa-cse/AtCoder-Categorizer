#include <iostream>
#include <map>
#include <string>
#include <array>

using namespace std;

// Directions: 0: L, 1: R, 2: D, 3: U
const int DX[4] = {0, 0, -1, 1};
const int DY[4] = {-1, 1, 0, 0};
const int OPP[4] = {1, 0, 3, 2};

map<pair<int, int>, array<pair<int, int>, 4>> nxt;

pair<int, int> get_ptr(pair<int, int> pos, int dir) {
    auto it = nxt.find(pos);
    if (it != nxt.end()) {
        return it->second[dir];
    }
    return {pos.first + DX[dir], pos.second + DY[dir]};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (!(cin >> k)) return 0;
    string s;
    cin >> s;

    pair<int, int> cur = {0, 0};
    // Initialize (0, 0)
    array<pair<int, int>, 4> init_ptrs;
    for (int d = 0; d < 4; ++d) {
        init_ptrs[d] = {cur.first + DX[d], cur.second + DY[d]};
    }
    nxt[cur] = init_ptrs;

    for (char c : s) {
        int dir;
        if (c == 'L') dir = 0;
        else if (c == 'R') dir = 1;
        else if (c == 'D') dir = 2;
        else dir = 3;

        pair<int, int> target = get_ptr(cur, dir);

        // Target is now visited, determine its 4 neighbors
        array<pair<int, int>, 4> target_ptrs;
        for (int d = 0; d < 4; ++d) {
            target_ptrs[d] = get_ptr(target, d);
        }
        nxt[target] = target_ptrs;

        // Bypass target in all 4 neighbors
        for (int d = 0; d < 4; ++d) {
            pair<int, int> neighbor = target_ptrs[d];
            int opp_dir = OPP[d];
            // Ensure neighbor is instantiated in map
            if (nxt.find(neighbor) == nxt.end()) {
                array<pair<int, int>, 4> n_ptrs;
                for (int dd = 0; dd < 4; ++dd) {
                    n_ptrs[dd] = {neighbor.first + DX[dd], neighbor.second + DY[dd]};
                }
                nxt[neighbor] = n_ptrs;
            }
            nxt[neighbor][opp_dir] = target_ptrs[opp_dir];
        }

        cur = target;
    }

    // Problem asks for (X, Y) where X is east (second coord), Y is north (first coord)
    cout << cur.second << " " << cur.first << "\n";
    return 0;
}
