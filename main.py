# cube_amount = input("Klucīšu daudzums:")
cube_amount = 1404
local_cubes_amount = int(cube_amount)
i=0
pyramid_amount = 0
pyramid_sizes = []
while local_cubes_amount > 0:
    while local_cubes_amount >= 0:
        i+=1
        local_cubes_amount -= i
        print("cubes left:", local_cubes_amount,"pyramid layer", i)
    local_cubes_amount = local_cubes_amount+i
    pyramid_sizes.append(i-1)
    print("on cycle:", i-1,"pyramid ended cubes left: ", local_cubes_amount)  
    pyramid_amount += 1
    i=0
print(pyramid_amount)  
print(pyramid_sizes) 