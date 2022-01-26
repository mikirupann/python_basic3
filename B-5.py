list = input("データを入力してください > ").split(" ")


def num_sum(app):
    tot = 0
    for rin in range(0, len(app)):
        tot = tot + int(app[rin])
    return tot


print(f"合計値: {num_sum(list)}")


def num_max(app):
    tot = 0
    for rin in range(1, len(app)):
        if int(app[tot]) < int(app[rin]):
            tot = rin
    return app[tot]


print(f"最大値: {num_max(list)}")


def num_min(app):
    tot = 0
    for rin in range(1, len(app)):
        if int(app[tot]) > int(app[rin]):
            tot = rin
    return app[tot]


print(f"最小値: {num_min(list)}")


def num_ave(app):
    tot = 0
    for rin in range(0, len(app)):
        tot = tot + int(app[rin])
    return tot


print(f"平均値: {int((num_ave(list)) / (len(list)))}")
