"""
11. 
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.


"""


def area(w,h):
    return w*h


def search_each_pair(my_list,final_area=0):
    for left_index, value  in enumerate(my_list):
        tem_list = my_list[left_index+1:].copy()
        print("my_list  -> tem_list ",my_list, tem_list)
        width = 0
        for right_index, right_value in enumerate(tem_list):
            width += 1
            print("left index ",left_index, "right_index: ", right_index, "(value, value) =  ", value,right_value , "width = ",width, "aread = ", area(min(value,right_value), width))
            final_area = max(final_area, area(min(value, right_value), width))
    return final_area


def moving_dfs( l_p, r_p, my_list , current_max_area):
    left_height = my_list[l_p]
    right_height = my_list[r_p]
    h = min(left_height,right_height)
    w = r_p - l_p 
    current_max_area = max(area(w,h),current_max_area)
    
    print("(l_p, r_p, w , h, area)",l_p,r_p,w ,h,current_max_area)
    if left_height <= right_height:
        l_p += 1
        if l_p == r_p:
            return current_max_area
        else:
            return moving_dfs(l_p,r_p,my_list,current_max_area)
    else:
        r_p -= 1
        if l_p == r_p:
            return current_max_area
        else:
            return moving_dfs(l_p, r_p, my_list, current_max_area)


my_list = [1,8,6,2,5,4,8,3,7]
res = moving_dfs(0,(len(my_list)-1),my_list,0)
print("max area is ", res)





