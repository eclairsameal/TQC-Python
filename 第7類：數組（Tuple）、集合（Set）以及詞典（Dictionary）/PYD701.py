# TODO
list =[]
while True:
    x = int(input())
    if(x==-9999):
        break
    list.append(x)  # リストに要素を追加する
tuple_list = tuple(list) #リスト(list)をタプル(tuple)に変換する
print(tuple_list)
print('Length:', len(tuple_list))
print('Max:', max(tuple_list))
print('Min:', min(tuple_list))
print('Sum:', sum(tuple_list))
