if wall_from_left():
    fill_cell()
for i in range(13):
    move_down()
    move_left()
    move_up()
    if wall_from_left() or wall_from_right():
        fill_cell()
move_down()
move_left()
move_up()
if wall_from_right():
    fill_cell()
move_down()
