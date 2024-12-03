import pyautogui


game_on = True
light_mode_obstacle_color = (83, 83, 83)
dark_mode_obstacle_color = (172, 172, 172)
obstacle_x = 350
low_obstacle_y = 690
high_obstacle_y = 600



while game_on:
        # Check for cactus (low obstacle)
        if (pyautogui.pixelMatchesColor(obstacle_x, low_obstacle_y, light_mode_obstacle_color) or
                pyautogui.pixelMatchesColor(obstacle_x, low_obstacle_y, dark_mode_obstacle_color)):

                pyautogui.press('space')


        # Check for bird (high obstacle)
        if (pyautogui.pixelMatchesColor(obstacle_x, high_obstacle_y, light_mode_obstacle_color) or
                pyautogui.pixelMatchesColor(obstacle_x, high_obstacle_y, dark_mode_obstacle_color)):
            pyautogui.press('down')
