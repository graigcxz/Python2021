"""存储【Alien Invasion】中所有设置的类"""

class Settings:

    def __init__(self):
        """初始化游戏设置"""

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 0.5