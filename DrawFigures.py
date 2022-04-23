#Rectangle

height = 8

for x in range(0, height):
    for z in range(0, height):
        place(x, 0, z)

# Cube

height = 8
for x in range(0, height):
    for y in range(0, height):
        for z in range(0, height):
            if (x == 0 or x == height - 1):
                if (z == 0 or z == height - 1):
                    place(x, y, z)

            if y == 0 or y == height - 1:
                if x == 0 or x == height - 1:
                    place(x, y, z)

            if y == 0 or y == height - 1:
                if z == 0 or z == height - 1:
                    place(x, y, z)
   
         
      
#Circle     

height = 9  # радіус - змінна величина

SECTOR = height / 3  # розділення на 3 сектора
RIGHT_RAD_DECREASE_KOEF = - (height / 4)  # коефіцієнт зменшення радіуса
LEFT_RAD_DECREASE_KOEF = - (height / 4)  # коефіцієнт зменшення радіуса
RIGHT_CIRCLE_KOEF = 0.4  # коефіцієнт заокруглення
LEFT_CIRCLE_KOEF = 0.4  # коефіцієнт заокруглення
ROUNDIFY_STEP_KOEF = 0.8 # коефіцієнт заокруглення покроково 

for x in range(0, height + 1):
    if x < (SECTOR * 1):
        place(x, height - x + RIGHT_RAD_DECREASE_KOEF, 0)
        place(x, -(height - x + RIGHT_RAD_DECREASE_KOEF), 0)
        RIGHT_RAD_DECREASE_KOEF = RIGHT_RAD_DECREASE_KOEF + ROUNDIFY_STEP_KOEF
    if (SECTOR * 1) <= x <= (SECTOR * 2):
        place(x, height - x, 0)
        place(x, -(height - x), 0)
    if SECTOR * 2 < x <= (SECTOR * 3):
        place(x - RIGHT_CIRCLE_KOEF, height - x, 0)
        place(x - RIGHT_CIRCLE_KOEF, -(height - x), 0)
        RIGHT_CIRCLE_KOEF = RIGHT_CIRCLE_KOEF + ROUNDIFY_STEP_KOEF

for x in range(0, -(height + 1), -1):
    if x > -(SECTOR * 1):
        place(x, height + x + LEFT_RAD_DECREASE_KOEF, 0)
        place(x, -(height + x + LEFT_RAD_DECREASE_KOEF), 0)
        LEFT_RAD_DECREASE_KOEF = LEFT_RAD_DECREASE_KOEF + ROUNDIFY_STEP_KOEF
    if -(SECTOR * 1) >= x >= -(SECTOR * 2):
        place(x, height + x, 0)
        place(x, -(height + x), 0)
    if -(SECTOR * 2) > x >= -(SECTOR * 3):
        place(x + LEFT_CIRCLE_KOEF, height + x, 0)
        place(x + LEFT_CIRCLE_KOEF, -(height + x), 0)
        LEFT_CIRCLE_KOEF = LEFT_CIRCLE_KOEF + ROUNDIFY_STEP_KOEF     