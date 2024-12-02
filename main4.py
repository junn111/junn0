# character.py파일


class Hero(Character):
    def __init__(self, name, hp, attack, defense, speed, role):
        super().__init__(name, hp, attack, defense, speed)
        self.role = role
        self.exp = 0


self.level = 1
self.weapon = None
self.armor = None


def gain_exp(self, amount):
    self.exp += amount
    print(f"{self.name}이(가) {amount} 경험치를 얻었습니다. 총 경험치: {self.exp}")

    # 100 경험치마다 레벨업


while self.exp >= 100:
    self.level_up()
    self.exp -= 100  # 남은 경험치를 다음 레벨로 이월


def level_up(self):
    self.level += 1


self.hp += 20
self.attack += 5
self.defense += 3
self.speed += 2
print(f"축하합니다! {self.name}이(가) 레벨업했습니다! 현재 레벨: {self.level}")
print(f"능력치 증가 -> 체력: +20, 공격력: +5, 방어력: +3, 속도: +2")


def __str__(self):
    return f"{super().__str__()}, 직업: {self.role}, 경험치: {self.exp}, 레벨: {self.level}"


class Monster(Character):
    def __init__(self, name, hp, attack, defense, speed, level):
        super().__init__(name, hp, attack, defense, speed)

    self.level = level

    def exp_reward(self):
        return self.level * 20


def drop_loot(self):
    if random.random() < 0.5:
        item_type = "weapon" if random.random() < 0.5 else "armor"


grade = random.choices(["일반", "레어", "전설"], weights=[50, 30, 20])[0]
attack_bonus = random.randint(5, 15)
defense_bonus = random.randint(3, 10)
return Equipment(name=f"{grade} {item_type}", type=item_type, attack_bonus=attack_bonus, defense_bonus=defense_bonus)
return None


def __str__(self):
    return f"{super().__str__()}, 레벨: {self.level}"


class Equipment:
    def __init__(self, name, type, attack_bonus, defense_bonus):
        self.name = name

    self.type = type  # "weapon" or "armor"


self.attack_bonus = attack_bonus
self.defense_bonus = defense_bonus


def __str__(self):
    return f"{self.name} (공격력 보너스: {self.attack_bonus}, 방어력 보너스: {self.defense_bonus})"


# battle.py파일

from character import Hero, Monster


class Battle:
    def fight(self, hero, monster):
        print(f"\n{hero.name}와 {monster.name}의 전투 시작!")

        while hero.is_alive() and monster.is_alive():
    # 속도 비교로 선공 결정


if hero.speed >= monster.speed:
    self.hero_turn(hero, monster)
    if monster.is_alive():
        self.monster_turn(hero, monster)
else:
    self.monster_turn(hero, monster)
    if hero.is_alive():
        self.hero_turn(hero, monster)

print("\n전투 종료!")
if hero.is_alive():
    print(f"{hero.name}이(가) 전투에서 승리했습니다!")
    hero.gain_exp(monster.exp_reward())
    loot = monster.drop_loot()
    if loot:
        print(f"전리품으로 {loot}을(를) 획득했습니다!")
        hero.equip(loot)
else:
    print(f"{hero.name}이(가) 전투에서 패배했습니다.")


def hero_turn(self, hero, monster):
    damage = hero.calculate_attack()
    print(f"{hero.name}의 공격! {monster.name}에게 {damage}의 피해를 입혔습니다.")
    monster.take_damage(damage)


def monster_turn(self, hero, monster):
    damage = monster.attack
    print(f"{monster.name}의 공격! {hero.name}에게 {damage}의 피해를 입혔습니다.")
    hero.take_damage(damage)


# main.py파일

from character import Hero, Monster
from battle import Battle


def main():
    print("=== RPG 게임 ===")
    name = input("영웅의 이름을 입력하세요: ")
    role = input("직업을 선택하세요 (전사/마법사/궁수): ")

    hero = Hero(name=name, hp=100, attack=20, defense=10, speed=12, role=role)
    print(hero)

    # 초기 몬스터 생성


monster = Monster(name="고블린", hp=50, attack=15, defense=5, speed=10, level=1)
print(monster)

# 전투 루프
battle = Battle()
for i in range(5):
    print(f"\n===== {i + 1}번째 전투 =====")
    battle.fight(hero, monster)
    if hero.is_alive():
        monster.level += 1
monster.hp += 20
monster.attack += 5
monster.defense += 3
monster.speed += 2
print(f"{monster.name}이(가) 레벨업했습니다! 현재 레벨: {monster.level}")
else:
break

if __name__ == "__main__":
    main()