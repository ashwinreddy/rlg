from robot import Robot
class AtlasRobot(Robot):
    def __init__(self):
        Robot.__init__(self, 'atlas')
        
class AtlasVirtualRobot(Robot):
    def __init__(self):
        Robot.__init__(self, 'atlas_virtual')
