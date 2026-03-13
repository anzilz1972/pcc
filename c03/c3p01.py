##########################################
####author:Anzilz1972
####date: 2026-3-13
####Python编程：从入门到实践   chapter 3
##########################################

Transportation = ['bus','motor','plane','train','subway']
for vehicle in Transportation:
    print(f'I would like to own a {vehicle} .')

guests = ['Dinjian','Liyan','WeiXin','Ranqiwan','Zhengjianfeng','Zhoulingxiu','Wangdong','Zhangzhenchao']

for guest in guests:
    print(guest, ' ')

for guest in guests:
    print(f'Good morning! {guest}!')

guests[-2] = 'Lilu'
guests.insert(0, 'Panshicheng')
guests.insert(4, 'Zhaojun')
guests.append('Wangyajin')

for guest in guests:
    print(f'Hi,{guest}! Please have a dinner with me tommorow!')


guests_list = guests
print(guests_list)
while len(guests_list) > 2:
    guests_list.pop()
print(guests_list)

del guests_list[0]
print(guests_list)
del guests_list[0]
print(guests_list)



















