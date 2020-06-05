time = 0
dt = 0.00001

max_t = int(input())
fline = input().split(' ')
sline = input().split(' ')

a_x = float(fline[0])
a_y = float(fline[1])
a_v_x = float(fline[2])
a_v_y = float(fline[3])

b_x = float(sline[0])
b_y = float(sline[1])
b_v_x = float(sline[2])
b_v_y = float(sline[3])


while time <= max_t:
    alice_pos = (a_x + a_v_x * time, a_y + a_v_y * time)
    bob_pos = (b_x + b_v_x * time, b_y + b_v_y * time)

    distance = ((alice_pos[0]-bob_pos[0])
                ** 2 + (alice_pos[1] - bob_pos[1]) ** 2)**(1/2)
    if distance <= 2:
        print(time)
        break

    time += dt
else:
    print(-1)
