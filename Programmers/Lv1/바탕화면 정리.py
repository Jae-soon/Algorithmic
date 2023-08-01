def solution(wallpaper):
    answer = []
    lux_list = []
    luy_list = []
    rdx_list = []
    rdy_list = []
    luy = 0
    for x in wallpaper:
        lux = 0
        for i in x:
            if i == "#":
                lux_list.append(lux)
                luy_list.append(luy)
                rdx_list.append(lux + 1)
                rdy_list.append(luy + 1)
            lux += 1
        luy += 1

    answer = [min(luy_list), min(lux_list), max(rdy_list), max(rdx_list)]
    return answer