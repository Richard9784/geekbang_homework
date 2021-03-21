class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direction = ((0,1),(1,0),(0,-1),(-1,0))
        di, x, y = 0, 0, 0
        distance = 0
        obs_dict = {}
        for obs in obstacles:
            obs_dict[tuple(obs)] = 0
        for com in commands:
            if com == -2:
                di = (di+3) %4
            elif com == -1:
                di = (di+1) %4
            else:
                for j in range(com):
                    dx, dy = direction[di]
                    next_x = x + dx
                    next_y = y + dy
                    if (next_x,next_y) in obs_dict:
                        break
                    x, y = next_x, next_y
                    distance = max(distance,x*x + y*y)
        return distance
