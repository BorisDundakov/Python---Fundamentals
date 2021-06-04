class Weapon:
    def __init__(self, bullets):
        self.bullets = int(bullets)

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            return "shooting..."
        return "no bullets left"

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"


weapon = Weapon(2)
weapon.shoot()
weapon.shoot()
weapon.shoot()
print(weapon)
