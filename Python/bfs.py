from collections import deque
import time

#N이 증가하면서 이동횟수는 임의로 변경

# Define the BFS algorithm
def bfs(initial_state, goal_state, n):
  visited = set()
  queue = deque([(0, initial_state)])  # (moves, state)
  while queue:
    moves, state = queue.popleft()
    if state == goal_state:
      return moves
    if tuple(state) not in visited:
      visited.add(tuple(state))
      blank_index = state.index(0)
      for move in [-n, -1, 1, n]:
        new_index = blank_index + move
        if 0 <= new_index < n**2 and (new_index // n == blank_index // n
                                      or new_index % n == blank_index % n):
          new_state = state.copy()
          new_state[blank_index], new_state[new_index] = new_state[
            new_index], new_state[blank_index]
          queue.append((moves + 1, new_state))

  return -1


n = 17
# Define the goal state and the initial state
goal_state = list(range(1, n**2)) + [0]

initial_state=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 203, 220, 0, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 219, 202, 221, 204, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 218, 235, 236, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 237, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 254, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 271, 288]
start = time.time()
print(bfs(initial_state, goal_state, n))
end = time.time()
print(end - start)

#print("{:.10f}".format(end - start))

