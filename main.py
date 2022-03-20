def prints(*txt):
    for i in txt:
        print(txt)

prints("文本战争模拟器","TEXT_FIGHT_SIMULATOR","版本:DEMO",
"开源，随意学习，使用")

class Player:
    def __init__(self, name, hp, def_num, atk):
        self.hp = hp  # 血量
        self.def_num = def_num  # 防御力
        self.atk = atk  # 攻击力
        self.name = name  # 名称

    def give_player_item(self, *item):
        self.item = item

    @staticmethod
    def return_player():  # 返回玩家数据
        print(f"{p.name}剩余{p.hp}点血\n防御力为{p.def_num}\n攻击力为{p.atk}\n你身上有\n{get_player_all_item()}")

    def attacked(self):  # 玩家被攻击
        for i in range(len(enemy_list)):
            p.hp -= (enemy_list[i].atk - p.def_num)
            print(f'{enemy_list[i].name}对{p.name}造成了{enemy_list[i].atk}点伤害')
        print(f"{p.name}剩余{p.hp}点血量")


name = input("你叫什么？")
p = Player(name, 20, 0, 3)  # 实例化玩家


class item:
    def __init__(self, item_type, item_attack, yes_or_no_use, add_data_type, id, have_num):
        self.item_type = item_type  # 物品标签
        self.item_attack = item_attack  # 物品增加倍数
        self.is_use = yes_or_no_use  # 物品是否使用
        self.add_data_type = add_data_type  # 物品增加标签
        self.item_id = id  # 物品id
        self.have_num = have_num  # 物品数量

    def use(self):
        if self.item_type == "手枪" and self.is_use == False:  # 是否使用判断
            p.atk = p.atk * self.item_attack
            self.is_use = True
            print(f"使用了{self.item_type}，{self.add_data_type}*{self.item_attack}为{p.atk}")

        elif self.item_type == "操枪" and self.is_use == False:
            p.atk = p.atk * self.item_attack
            self.is_use = True
            print(f"使用了{self.item_type}，{self.add_data_type}*{self.item_attack}为{p.atk}")
        elif self.item_type == "帽子" and self.is_use == False:
            p.def_num = p.def_num + self.item_attack
            self.is_use = True
            print(f"使用了{self.item_type}，{self.add_data_type}+{self.item_attack}为{p.def_num}")
        elif self.item_type == "蛋糕" and self.is_use == False:
            print(f"使用了{self.item_type}，剩余{self.have_num}个，{self.add_data_type}+{self.item_attack}为{p.hp}")
            if self.have_num <= 0:
                self.is_use = True
            p.hp += self.item_attack
            self.have_num -= 1



        elif self.is_use == True:
            print(f"已经使用了{self.item_type}")
        else:
            print("物品未定义")

    def stop_use(self):
        if self.item_type == "手枪" and self.is_use == True:  # 是否使用判断
            p.atk = int(p.atk / self.item_attack)
            self.is_use = False
            print(f"停止使用了{self.item_type}，{self.add_data_type}/{self.item_attack}为{p.atk}")
        elif self.item_type == "操枪" and self.is_use == True:
            p.atk = int(p.atk / self.item_attack)
            self.is_use = False
            print(f"停止使用了{self.item_type}，{self.add_data_type}/{self.item_attack}为{p.atk}")
        elif self.item_type == "帽子" and self.is_use == True:
            p.def_num = p.def_num - self.item_attack
            self.is_use = False
            print(f"停止使用了{self.item_type}，{self.add_data_type}-{self.item_attack}为{p.hp}")

        elif self.is_use == False:
            print(f"没有使用{self.item_type}无法停止使用")
        else:
            print("未知物品")


gun = item("手枪", 2, False, "攻击", 0, 1)  # 实例化物品
Fuckgun = item("操枪", 30, False, "攻击", 1, 1)
hat = item("帽子", 2, False, "防御", 2, 1)
cake = item("蛋糕", 3, False, "血量", 3, 2)

p.give_player_item(gun, Fuckgun, hat, cake)  # 设置玩家物品栏


def get_player_one_item(idx):  # 获取玩家物品信息

    use_text = "可以使用"
    if not p.item[idx].is_use:
        use_text = "否"
    else:
        use_text = "是"
    return (f'是否使用：{use_text}，物品”{p.item[idx].item_type}“\n{p.item[idx].add_data_type}增加值：{p.item[idx].item_attack}\n')


def get_player_all_item():  # 返回玩家所有物品信息
    item_data = ""
    for i in range(len(p.item)):
        item_data += (f'{i},{get_player_one_item(i)}')
    return item_data


class Enemy:
    def __init__(self, id, name, hp, def_num, atk):
        self.id = id  # 敌人id
        self.name = name  # 敌人名称
        self.hp = hp  # 敌人血量
        self.atk = atk  # 攻击力
        self.def_num = def_num  # 敌人防御力

    def attacked(self):  # 敌人被攻击
        self.hp -= (p.atk - self.def_num)  # 伤害减去防御力
        print(f"{enemy_list[Player_input].name}被{p.name}造成了{p.atk - enemy_list[Player_input].def_num}点伤害")


# Enemy(0,"稻草人",10,1,1)
enemy_list = [Enemy(0, "稻草人", 10, 1, 1) for i in range(4)]  # 敌人列表


def get_one_enemy(i):  # 获取一个敌人信息
    return f'{enemy_list[i].name}\n血量：{enemy_list[i].hp}\n攻击力：{enemy_list[i].atk}\n防御：{enemy_list[i].def_num}\n'


def get_all_enemy():  # 获取所有敌人信息
    enemy_data = ""
    for i in range(len(enemy_list)):
        enemy_data += f'{i},{get_one_enemy(i)}\n'
    return enemy_data


def how_win():
    global run_game
    if p.hp <= 0:
        print("游戏结束，玩家失败")
        run_game = False
    elif len(enemy_list) <= 0:
        print("游戏结束，玩家胜利")
        run_game = False

def enemy_round():
    print("-" * 20, f"敌方回合")
    p.attacked()
    how_win()
    input()


run_game = True
while run_game:  # 攻击

    Player_input = input(f"去做什么，{p.name}\n1.刷怪\n:")

    if Player_input == "1":  # 战斗
        while run_game:
            print("-" * 20, f"玩家回合")
            print(get_all_enemy())
            Player_input = input("做什么\n1.攻击\n2.物品\n:")
            if Player_input == "1":
                Player_input = int(input("攻击谁\n:"))
                enemy_list[Player_input].attacked()
                if enemy_list[Player_input].hp <= 0:
                    del enemy_list[Player_input]
                enemy_round()
            elif Player_input == "2":
                Player_input = input("1.穿/使用\n2.脱\n:")
                if Player_input == "1":
                    print(get_player_all_item())
                    Player_input = int(input("使用哪个物品\n:"))
                    p.item[Player_input].use()
                elif Player_input == "2":
                    print(get_player_all_item())
                    Player_input = int(input("停止使用哪个物品\n:"))
                    p.item[Player_input].stop_use()
                else:
                    print("没有这个选项")
                enemy_round()
            else:
                enemy_round()
    else:
        print("暂时没有其他内容")