from commons.settings import * 
from math_lib.matrix import * 
from scripts.cube import *


class App():
    def __init__(self) -> None:
        pg.init()
        self.screen: pg.display = pg.display.set_mode((WIDTH, HEIGHT))
        self.screen.fill((0, 0, 0))
        self.display: pg.Surface = pg.Surface((WIDTH, HEIGHT))
        self.dt: float = 0
        self.total_time = 0
        self.clock: pg.time = pg.time.Clock()

        self.cube1 = Cube(self, cube_mesh)

        self.movement: list[bool] = [false, false, false, false]


    def render(self):
        self.display.fill(BLACK)
        self.total_time += 1


        self.cube1.render(self.display)


        self.screen.blit(self.display, (0,0))
        pg.display.flip()
        pg.display.update()

    def check_inputs(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_LEFT: self.movement[0] = true
                if e.key == pg.K_RIGHT: self.movement[1] = true
                if e.key == pg.K_UP: self.movement[2] = true
                if e.key == pg.K_DOWN: self.movement[3] = true
                if e.key == pg.K_SPACE:
                    self.player.jump()
  
            if e.type == pg.KEYUP:
                if e.key == pg.K_LEFT: self.movement[0] = false
                if e.key == pg.K_RIGHT: self.movement[1] = false
                if e.key == pg.K_UP: self.movement[2] = false
                if e.key == pg.K_DOWN: self.movement[3] = false

    def update(self):
        self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps()}')
        self.dt = self.clock.tick(FPS)
        self.dt /= 1000

    def run(self):
        while True:
            self.render()
            self.check_inputs()
            self.update()

if __name__ == '__main__':
    app = App()
    app.run()
