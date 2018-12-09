class Settings():
	'''存储《外星人入侵》的所有设置的类'''
	def __init__(self):
		'''初始化游戏的静态设置'''
		#屏幕设置
		self.screen_width = 1000
		self.screen_height = 600
		self.bg_color = (230,230,230)
	
		# 子弹设置
		#self.bullet_speed_factor = 5
		self.bullet_width = 50
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 10

		# 外星人设置
		#self.alien_speed_factor = 10
		self.fleet_drop_speed = 100
		

		# 飞船设置
		#self.ship_speed_factor = 10
		self.ship_limit = 2

		# 以什么样的速度加快游戏节奏
		self.speedup_scale = 1.5
		# 外星人点数的提高速度
		self.score_scale = 1.5

		self.initialize_dynamic_settings()


	def initialize_dynamic_settings(self):
		"""初始化随游戏进行而变化的设置"""
		self.bullet_speed_factor = 10
		self.alien_speed_factor = 5
		self.ship_speed_factor = 10

		# 1表示右移，-1表示左移
		self.fleet_direction = 1

		# 记分
		self.alien_points = 50 

	def increase_speed(self):
		"""提高速度和外星人的点数"""
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.ship_speed_factor *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)















