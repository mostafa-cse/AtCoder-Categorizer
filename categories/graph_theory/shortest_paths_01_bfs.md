# 📖 0-1 BFS with State Direction / Minimum Turn Path

- **Tag / Domain**: `Graph Theory`
- **Subtopic**: `Shortest Paths`

---

## 💡 Topic Overview
High-value competitive programming techniques for **0-1 BFS with State Direction / Minimum Turn Path**.

---

## 🏆 Curated High-Value Problems

### Maze Challenge with Lack of Sleep (`[problem:AtCoder-typical90_aq]`)

- **Role**: *0-1 BFS with State Direction / Minimum Turn Path*
- **Rating**: `1350` (★4) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_aq)
- **Full Analysis**: [AtCoder-typical90_aq Analysis](../../analysis/AtCoder-typical90_aq.md)

#### Problem Statement & Task
H x W grid with walls. Start at (r_s, c_s), goal at (r_t, c_t). Moving in the same direction costs 0 turns; changing direction costs 1 turn. Find minimum turns to reach goal.

#### Core Invariant & Observation
Because edge weights are strictly {0, 1}, pushing weight-0 edges to the front and weight-1 edges to the back of a deque guarantees monotonic distance processing in O(HW) linear time.

#### Algorithmic Formulation
1. dist[H][W][4] initialized to INF.
2. Push initial 4 directions from start into deque with dist = 0.
3. While deque not empty: pop (r, c, dir):
   - Straight step: (nr, nc) in same dir has cost 0 -> push_front.
   - Turn in place: other directions have cost 1 -> push_back.
4. Output min over all 4 directions at goal.

**Complexity**: `Time: O(H * W), Space: O(H * W).`  
**Editorial Alignment**: 0-1 BFS state graph with directional orientation.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: 0-1 BFS with std::deque, directional orientation in grid states, and linear time turn minimization.
- **Reusable Pattern**: `0-1 BFS on State Grid.`

---

[Back to Master Categories](../../README.md)
