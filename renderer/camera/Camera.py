import glm
import math

class Camera:
    def __init__(self):
        self.position = glm.vec3(0.0, 0.0, 3.0)
        self.front = glm.vec3(0.0, 0.0, -1.0)
        self.world_up = glm.vec3(0.0, 1.0, 0.0)

        self.right = glm.normalize(glm.cross(self.world_up, self.front))
        self.up = glm.cross(self.front, self.right)

        self.yaw = -90.0
        self.pitch = 0.0

        self.view_matrix = glm.lookAt(self.position, self.position + self.front, self.world_up)

    def _calculate_vectors(self):
        self.right = glm.normalize(glm.cross(self.world_up, self.front))
        self.up = glm.cross(self.front, self.right)
        self.view_matrix = glm.lookAt(self.position, self.position + self.front, self.world_up)

    def move(self, amount):
        self.position += amount * self.front
        self._calculate_vectors()

    def strafe(self, amount):
        self.position += amount * self.right
        self._calculate_vectors()

    def lift(self, amount):
        self.position += amount * self.world_up
        self._calculate_vectors()

    def turn(self, yaw, pitch):
        self.yaw += yaw
        self.pitch += pitch

        if self.pitch > 89.0:
            self.pitch = 89.0
        if self.pitch < -89.0:
            self.pitch = -89.0

        direction = glm.vec3(
            math.cos(glm.radians(self.yaw)) * math.cos(glm.radians(self.pitch)),
            math.sin(glm.radians(self.pitch)),
            math.sin(glm.radians(self.yaw)) * math.cos(glm.radians(self.pitch))
        )

        self.front = glm.normalize(direction)

        self._calculate_vectors()

        

    def get_ogl_matrix(self):
        return(glm.value_ptr(self.view_matrix))