def clear_oled(disp):
    disp.buffer = [0x00] * (disp.width * disp.height // 8)
    disp.show()
