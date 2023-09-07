import glm

class Camera:
    def __init__(self):
        self.position = glm.vec3(0.0, 0.0, 0.0)
        # self.target = glm.vec3(0.0, 0.0, 0.0)
        # self.direction = glm.normalize(self.position - self.target)
        self.world_up = glm.vec3(0.0, 1.0, 0.0)
        self.right = glm.normalize(glm.cross(self.world_up, self.target))
        self.up = glm.cross(self.direction, self.right)

        self.front = glm.vec3(0.0, 0.0, -1.0)

        self.view_matrix = glm.lookat(self.position, self.position + self.front, self.world_up)