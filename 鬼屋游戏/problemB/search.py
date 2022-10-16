from Ghost import Ghost
from Map import mapmat
import random

cost_list = []
face_list = []

def search(rob,gho1,gho2)->list[tuple]:
    '''搜索算法'''
    def cost():
        '''计算收益'''
        dis_to_start = abs(rob.map_x-1)+abs(rob.map_y-1)
        dis_to_end = abs(rob.map_x-6)+abs(rob.map_y-6)
        cold = rob.sensitor(gho1,gho2)
        return dis_to_start - dis_to_end - cold

    rob_loc = [(rob.start_x,rob.start_y)]
    gho1_loc = [(gho1.start_x,gho1.start_y)]
    gho2_loc = [(gho2.start_x,gho2.start_y)]

    g1_face_to = gho1.face_to
    g2_face_to = gho2.face_to
    g1_start_x = gho1.start_x
    g1_start_y = gho1.start_y
    g2_start_x = gho2.start_x
    g2_start_y = gho2.start_y
    r_start_x = rob.start_x
    r_start_y = rob.start_y
    r_map_x = rob.map_x
    r_map_y = rob.map_y

    for i in range(15):
        if g1_face_to == 1:
            if g1_start_x < 6:
                g1_start_x += 1
                gho1_loc.append((g1_start_x,g1_start_y))
            else:
                g1_face_to = 2
            
        if g1_face_to ==2:
            if g1_start_x > 1:
                g1_start_x -= 1
                gho1_loc.append((g1_start_x,g1_start_y))
            else:
                g1_face_to = 1

        if g1_face_to == 3:
            if g1_start_y >1:
                g1_start_y -= 1
                gho1_loc.append((g1_start_x,g1_start_y))
            else:
                g1_face_to = 4
            
        if g1_face_to ==4:
            if g1_start_y <6:
                g1_start_y += 1
                gho1_loc.append((g1_start_x,g1_start_y))
            else:
                g1_face_to = 3



        if g2_face_to == 1:
            if g2_start_x < 6:
                g2_start_x += 1
                gho2_loc.append((g2_start_x,g2_start_y))
            else:
                g2_face_to = 2
            
        if g2_face_to ==2:
            if g2_start_x > 1:
                g2_start_x -= 1
                gho2_loc.append((g2_start_x,g2_start_y))
            else:
                g2_face_to = 1

        if g2_face_to == 3:
            if g2_start_y > 1:
                g2_start_y -= 1
                gho2_loc.append((g2_start_x,g2_start_y))
            else:
                g2_face_to = 4
            
        if g2_face_to ==4:
            if g2_start_y <6:
                g2_start_y += 1
                gho2_loc.append((g2_start_x,g2_start_y))
            else:
                g2_face_to = 3

    i = 0
    while(r_start_x != 6 or r_start_y != 6):
        # print(len(mapmat.maplist[0]))
        if not mapmat.maplist[r_map_x][r_map_y+1] and mapmat.maplist[r_map_x-1][r_map_y]:
            face = 1
        elif not mapmat.maplist[r_map_x-1][r_map_y] and mapmat.maplist[r_map_x][r_map_y+1]:
            face = 2
        elif mapmat.maplist[r_map_x-1][r_map_y] and mapmat.maplist[r_map_x][r_map_y+1]:
            face = 3
        elif not mapmat.maplist[r_map_x][r_map_y+1] and not mapmat.maplist[r_map_x-1][r_map_y]:
            face = random.randint(1,2)
        # print(face)
        if face == 1:
            if (r_start_x + 1 == gho1_loc[i%10+2][0] and r_start_y == gho1_loc[i%10+2][1]) or (r_start_x + 1 == gho2_loc[i%10+2][0] and r_start_y == gho2_loc[i%10+2][1]):
                rob_loc.append((r_start_x,r_start_y))
                i+=1
            else:
                if r_start_x != 6:
                    r_start_x += 1
                    rob_loc.append((r_start_x,r_start_y))
                    i+=1
                    if r_map_y != 11:
                        r_map_y+=2
                    else:
                        break
                
                
        elif face == 2:
            if (r_start_x == gho1_loc[i%10+2][0] and r_start_y + 1 == gho1_loc[i%10+2][1]) or (r_start_x == gho2_loc[i%10+2][0] and r_start_y + 1 == gho2_loc[i%10+2][1]):
                rob_loc.append((r_start_x,r_start_y))
                i+=1
            else:
                if r_start_y != 6:
                    r_start_y += 1
                    rob_loc.append((r_start_x,r_start_y))
                    i+=1
                    if r_map_x != 1:
                        r_map_x-=2
                    else:
                        break


        elif face == 3:
            if (r_start_x-1 == gho1_loc[i%10+2][0] and r_start_y== gho1_loc[i%10+2][1]) or (r_start_x-1 == gho2_loc[i%10+2][0] and r_start_y == gho2_loc[i%10+2][1]):
                rob_loc.append((r_start_x,r_start_y))
                i+=1
            else:
                if r_start_x != 0:
                    r_start_x -= 1
                    rob_loc.append((r_start_x,r_start_y))
                    i+=1
                    if r_map_y != 1:
                        r_map_y-=2
                    else:
                        break
    return rob_loc


if __name__ == '__main__':
    gho1 = Ghost()
    gho2 = Ghost()
    





