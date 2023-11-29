import pygame

# Инициализация Pygame
pygame.init()

# Задаем размеры окна
window_width = 400
window_height = 400

# Создаем окно
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Заметки")

# Задаем цвета для фона и текста
bg_color = (255, 255, 255)
text_color = (0, 0, 0)

# Создаем шрифт для отображения текста
font = pygame.font.Font(None, 20)

# Запрашиваем количество заметок
num_notes = int(input("Сколько заметок вы хотите создать? "))

# Создаем список для хранения заметок
notes = []

# Запрашиваем заметки у пользователя
for i in range(num_notes):
    note_input = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isprintable():
                    note_input += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    note_input = note_input[:-1]
                elif event.key == pygame.K_RETURN:
                    break

        # Заливаем фон окна
        screen.fill(bg_color)

        # Отображаем инструкцию на экране
        instructions_text = font.render("Введите заметку №{}:".format(i + 1), True, text_color)
        screen.blit(instructions_text, (20, 20))

        # Отображаем введенный текст на экране
        note_input_text = font.render(note_input, True, text_color)
        screen.blit(note_input_text, (20, 50))

        # Обновляем экран
        pygame.display.update()

    # Добавляем заметку в список
    notes.append(note_input)

# Отображаем заметки на экране
y = 90
for note in notes:
    text = font.render(note, True, text_color)
    screen.blit(text, (20, y))
    y += 20

# Запускаем основной цикл Pygame
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Заливаем фон окна
    screen.fill(bg_color)

    # Отображаем заметки на экране
    y = 90
    for note in notes:
        text = font.render(note, True, text_color)
        screen.blit(text, (20, y))
        y += 20

    # Обновляем экран
    pygame.display.update()
