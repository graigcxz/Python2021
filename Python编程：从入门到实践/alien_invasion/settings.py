"""存储【Alien Invasion】中所有设置的类"""

class Settings:

    def __init__(self):
        """初始化游戏设置"""

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 0.5

        # 子弹的设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 0, 0)
        self.bullet_speed_factor = 0.3
        self.bullets_allowed = 3

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 0.2
        self.fleet_direction = 1