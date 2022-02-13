def set_speed(speed_menu):
    if speed_menu.get() == 'Slow':
        return 0.3
    elif speed_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.001