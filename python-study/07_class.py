# 왜 클래스를 사용할까?
# 각 객체가 각자의 특성을 관리해야할때 - 객체 지향적

class Monster():
    hp = 100
    alive = True

    def demage(self, attack):
        self.hp = self.hp - attack
        if self.hp < 0:
            self.alive = False

    def status_check(self):
        if self.alive:
            print('살았다')
        else:
            print('죽었다')


m1 = Monster()
m1.demage(150)
m1.status_check()

m2 = Monster()
m2.demage(90)
m2.status_check()
