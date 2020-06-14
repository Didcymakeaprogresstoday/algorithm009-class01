class Solution:
	def robotSim(self, commands:List, obstacles:List) -> int:
		#字典储存某个方向对应的[x方向移动，y方向移动，当前方向的左侧，当前方向的右侧]
		direction = {
					'up':[0, 1, 'left', 'right'],
					'down':[0, -1, 'right', 'left'],
					'left':[-1, 0, 'down', 'up'],
					'right':[1, 0, 'up', 'down']
		}
		x, y = 0, 0
		dir = 'up'
		ans = 0
		obstacles = set(map(tuple, obstacles)) 
		for command in commands:
			if command > 0:
				for _ in range(command):
					if (x + direction[dir][0], y + direction[dir][1]) not in obstacles:
						x += direction[dir][0]
						y += direction[dir][1]
						ans = max(ans, x ** 2 + y ** 2)
					else:
						break

			elif command == -1:
				dir = direction[dir][3]
			elif command == -2:
				dir = direction[dir][2]
		return ans