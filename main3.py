import random
from abc import ABC, abstractmethod


# Character 클래스 정의
class Character:
    def __init__(self, name, hp, attack, defense, speed):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense)
        self.hp = max(0, self.hp - actual_damage)
        return actual_damage

    def is_alive(self):
        return self.hp > 0


def __str__(self):
    return (f"{self.name} - HP: {self.hp}, 공격력 : {self.attack}, "
            f"방어력 : {self.defense}, 속도:{self.speed}")


# Equipment 클래스 정의
class Equipment:
    def __init__(self, name, grade, attack_bonus=0, defense_bonus=0):
        self.name = name
        self.grade = grade
        self.attack_bonus = attack_bonus
        self.defense_bonus = defense_bonus

    def __str__(self):
        return (f"장비: {self.name}, 등급:{self.grade}, "
                f"공격력 : {self.attack_bonus}, 방어력 : {self.defense_bonus}")


# Monster 추상 클래스 정의
class Monster(ABC, Character):
    def __init__(self, name, hp, attack, defense, speed, level):
        super().__init__(name, hp, attack, defense, speed)
        self.level = level

    @abstractmethod


def special_attack(self):
    pass


@abstractmethod
def description(self):
    pass


# Goblin, Orc, Dragon 몬스터 클래스 정의
class Goblin(Monster):
    def special_attack(self):
        return self.attack * 1.5  # 고블린의 특별 공격: 일반 공격의 1.5배


def description(self):
    return f"{self.name}은/는 작고 민첩한 괴물로, 빠른 공격을 한다."


class Orc(Monster):
    def special_attack(self):
        return self.attack * 2  # 오크의 특별 공격: 일반 공격의 2배


def description(self):
    return f"{self.name}은/는 강력한 힘을 가진 괴물로, 엄청난 공격을 한다."


class Dragon(Monster):
    def special_attack(self):
        return self.attack * 3  # 드래곤의 특별 공격: 일반 공격의 3배


def description(self):
    return f"{self.name}은/는 거대한 날개를 가진 드래곤으로, 강력한 불꽃을 뿜는다."


# Hero 클래스 정의
class Hero(Character):
    def __init__(self, name, hp, attack, defense, role, speed):
        super().__init__(name, hp, attack, defense, speed)
        self.role = role
        self.exp = 0


self.level = 1
self.weapon = None
self.armor = None


def equip(self, equipment):
    if equipment.attack_bonus > 0:
        self.weapon = equipment
    elif equipment.defense_bonus > 0:
        self.armor = equipment
    print(f"{self.name}가 {equipment.name}을 장착!")


def calculate_attack(self):
    return self.attack + (self.weapon.attack_bonus if self.weapon else 0)


def calculate_defense(self):
    return self.defense + (self.armor.defense_bonus if self.armor else 0)


def special_attack(self):
    if self.role == "전사":
        return self.attack + 5

elif self.role == "마법사":
return self.attack + 4
elif self.role == "궁수":
return self.attack + 3
else:
return self.attack + 1


def gain_exp(self, amount):
    self.exp += amount
    print(f"{self.name}의 경험치가 {amount}만큼 증가했습니다. 현재 경험치: {self.exp}")


def level_up(self):
    self.level += 1


self.exp = 0
if self.role == "전사":
    self.hp += 30
self.attack += 3
self.defense += 5
elif self.role == "마법사":
self.hp += 5
self.attack += 8
self.defense += 2
elif self.role == "궁수":
self.hp += 10
self.attack += 6
self.defense += 3


# Battle 클래스 정의
class Battle:
    def fight(self, hero, monster):
        print(f"{hero.name}과 {monster.name}의 전투가 시작되었습니다!")
        while hero.is_alive() and monster.is_alive():
            self.hero_turn(hero, monster)
            if monster.is_alive():
                self.monster_turn(hero, monster)
        self.end_fight(hero, monster)

    def hero_turn(self, hero, monster):
        damage = hero.calculate_attack()
        print(f"{hero.name}의 공격! {monster.name}에게 {damage}의 피해를 입혔습니다.")
        monster.take_damage(damage)

    def monster_turn(self, hero, monster):
        if random.random() < 0.5:  # 50% 확률로 특별 공격 사용


damage = monster.special_attack()
print(f"{monster.name}의 특별 공격! {hero.name}에게 {damage}의 피해를 입혔습니다.")
else:
damage = monster.attack
print(f"{monster.name}의 일반 공격! {hero.name}에게 {damage}의 피해를 입혔습니다.")
hero.take_damage(damage)


def end_fight(self, hero, monster):
    if hero.is_alive():
        print(f"{hero.name}이(가) 승리했습니다!")
        hero.gain_exp(monster.level * 20)
        print(f"{hero.name}의 경험치: {hero.exp}")
    else:
        print(f"{hero.name}이(가) 패배했습니다.")


# 메인 함수
def main():
    name = input("영웅의 이름을 입력하세요: ")
    role = input("직업을 입력하세요 (전사/마법사/궁수): ")
    hero = Hero(name, 100, 20, 5, role, 12)
    print(hero)

    monster_choice = random.choice([Goblin("고블린", 30, 10, 5, 10, 1),
                                    Orc("오크", 50, 20, 10, 8, 2),
                                    Dragon("드래곤", 100, 40, 20, 15, 3)])
    print(monster_choice.description())

    battle = Battle()
    battle.fight(hero, monster_choice)

    if hero.is_alive():
        print(f"최종 영웅 상태: {hero}")
    else:
        print(f"{hero.name}은/는 게임 오버!")


if __name__ == "__main__":
    main()


class Battle:
    def fight(self, hero, monster):
        print(f"\n{hero.name}와 {monster.name}의 전투 시작!")

        while hero.is_alive() and monster.is_alive():
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


# 몬스터는 랜덤하게 일반 공격 혹은 특별 공격을 사용
if random.random() < 0.5:  # 50% 확률로 특별 공격
    damage = monster.special_attack()
print(f"{monster.name}의 특별 공격! {hero.name}에게 {damage}의 피해를 입혔습니다.")
else:
damage = monster.attack
print(f"{monster.name}의 일반 공격! {hero.name}에게 {damage}의 피해를 입혔습니다.")
hero.take_damage(damage)

import random
from character import Hero, Goblin, Orc, Dragon  # 필요한 클래스들 가져오기
from battle import Battle


def main():
    print("=== RPG 게임 시작 ===")
    name = input("영웅의 이름을 입력하세요: ")
    role = input("직업을 선택하세요 (전사/마법사/궁수): ")

    # 영웅 초기화


hero = Hero(name, 100, 20, 5, role, speed=12)
print(hero)

# 전투 객체 생성
battle = Battle()
battle_count = 0

# 5번 연속 전투
while hero.is_alive() and battle_count < 5:
# 몬스터 랜덤 선택 (레벨 1부터 시작)
monster_type = random.choice([Goblin, Orc, Dragon])
monster = monster_type(f"{monster_type.__name__} 몬스터", 30, 10, 2, speed=10, level=1)

print(f"\n===== {battle_count + 1}번째 전투 시작 =====")
print(f"{monster.name} (레벨: {monster.level})와의 전투!")

# 전투 시작
battle.fight(hero, monster)

if hero.is_alive():
# 전투 후 몬스터 레벨 업
monster.level += 1
print(f"{monster.name}의 레벨이 상승했습니다! 현재 레벨: {monster.level}")
battle_count += 1  # 전투 횟수 증가
else:
break  # 영웅이 죽으면 전투 종료

# 전투 종료 후 결과 출력
if hero.is_alive():
    print(f"\n{hero.name}은/는 5번의 전투를 모두 승리했습니다!")
    print(f"최종 영웅 상태: {hero}")
else:
    print(f"{hero.name}이(가) 전투 중 죽었습니다. 게임 오버!")

if __name__ == "__main__":
    main()