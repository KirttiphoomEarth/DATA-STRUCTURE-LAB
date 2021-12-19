def m_w(oder_list, box):
    if box == 1:
        return sum(oder_list)
    
    min_w = 999999999999999999999999999999999999999999999999999999999999999
    for index in range(len(oder_list)):
        if len(oder_list[index:]) < box -1:
            break
        
        this_box = sum(oder_list[:index])
        other_box = m_w(oder_list[index:], box - 1)
        min_w = min(max(this_box, other_box), min_w)
    return min_w


order, box = input('Enter Input : ').split('/')
order = list(map(int, order.split()))
print(f'Minimum weigth for {box} box(es) = {m_w(order, int(box))}')