def ips_between(start, end):   
    ip_range_one = start.split('.')
    ip_range_two = end.split('.')
    
    one   = int(ip_range_one[0]) - int(ip_range_two[0])
    two   = int(ip_range_one[1]) - int(ip_range_two[1])
    three = int(ip_range_one[2]) - int(ip_range_two[2])
    four  = int(ip_range_one[3]) - int(ip_range_two[3])
    
    if(three != 0):    
        temp = 0
        while three:
            if three < 0:
                temp -= 256
                three += 1
            else:
                temp += 256
                three -= 1
        three = temp
        
    if(two != 0):
        temp = 0
        while two:
            if two < 0:
                temp -= 256 * 256
                two += 1
            else:
                temp += 256 * 256
                two -= 1
        two = temp
        
        
    if(one != 0):
        temp = 0
        while one:
            if one < 0:
                temp -= 256 * 256 *256
                one += 1
            else:
                temp += 256 * 256 * 256
                one -= 1
        one = temp
    
    count_ip = four + three + two + one
    return count_ip * -1
    
    
 
print(ips_between("10.0.0.0", "10.0.0.50"))
# >>> 50
print(ips_between("20.0.0.10", "20.0.1.0"))
# >>> 246
print(ips_between("136.94.86.74", "136.97.244.154"))
# >>> 237136


 
