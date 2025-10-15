import pyautogui
import time

# --- Настройки ---
first_patient = (984, 185)
patient_step = 19
patients_per_page = 30
total_patients = 261

first_code = (990, 885)      # координаты первой строки с кодом услуги
code_step = 19               # расстояние между строками кодов
max_codes = 4             # максимальное количество кодов на пациента (подбери под себя)

DELAY_SAVE = 1.5
DELAY = 0.6

# --- Обработка одного кода услуги ---
def process_code(code_index):
    x = first_code[0]
    y = first_code[1] + code_index * code_step
    pyautogui.click(x, y)
    time.sleep(DELAY)

    pyautogui.doubleClick(932, 884)
    time.sleep(DELAY)
    pyautogui.click(1232, 538)
    time.sleep(DELAY)
    pyautogui.click(736, 299)
    time.sleep(DELAY)
    pyautogui.typewrite('1')
    time.sleep(DELAY)
    pyautogui.press('f2')
    time.sleep(DELAY_SAVE)
    pyautogui.click(903, 841)
    time.sleep(DELAY)
    # pass
    pyautogui.click(964, 841)
    time.sleep(DELAY)
    # pass
    pyautogui.click(775, 841)
    time.sleep(DELAY)

# Обработка всех кодов для пациента
def process_all_codes():
    for code_index in range(max_codes):
        process_code(code_index)

# Действия с картой пациента
def process_patient_card(patient_y):
    pyautogui.doubleClick(first_patient[0], patient_y)
    time.sleep(DELAY * 2)

    pyautogui.click(947, 795)
    time.sleep(DELAY)
    pyautogui.doubleClick(749, 299)
    time.sleep(DELAY)
    pyautogui.typewrite('1')
    time.sleep(DELAY)
    pyautogui.press('f2')
    time.sleep(DELAY_SAVE)

    pyautogui.click(947, 810)
    time.sleep(DELAY)
    pyautogui.doubleClick(749, 299)
    time.sleep(DELAY)
    pyautogui.typewrite('305')
    time.sleep(DELAY)
    pyautogui.press('f2')
    time.sleep(DELAY_SAVE)

    pyautogui.click(949, 828)
    time.sleep(DELAY)
    pyautogui.doubleClick(749, 299)
    time.sleep(DELAY)
    pyautogui.typewrite('301')
    time.sleep(DELAY)
    pyautogui.press('f2')
    time.sleep(DELAY_SAVE)

    pyautogui.click(949, 845)
    time.sleep(DELAY)
    pyautogui.doubleClick(749, 299)
    time.sleep(DELAY)
    pyautogui.typewrite('1')
    time.sleep(DELAY)
    pyautogui.press('f2')
    time.sleep(DELAY_SAVE)

    pyautogui.click(948, 863)
    time.sleep(DELAY)
    pyautogui.doubleClick(749, 299)
    time.sleep(DELAY)
    pyautogui.typewrite('2.6')
    time.sleep(DELAY)
    pyautogui.press('f2')
    time.sleep(DELAY_SAVE)

    pyautogui.press('f2')
    time.sleep(DELAY_SAVE)
    pyautogui.press('esc')
    time.sleep(DELAY_SAVE * 1.7)

# Основной цикл
def main():
    print("Старт через 5 секунд...")
    time.sleep(5)
    i = 0
    while i < total_patients:
        for patient_on_screen in range(patients_per_page):
            if i >= total_patients:
                break
            patient_y = first_patient[1] + patient_on_screen * patient_step
            pyautogui.click(first_patient[0], patient_y)
            time.sleep(DELAY)
            process_all_codes()
            process_patient_card(patient_y)
            i += 1
            time.sleep(1)

        if i < total_patients:
            pyautogui.click(989, 736)
            time.sleep(1)
            pyautogui.press('pagedown')
            time.sleep(1.5)
            pyautogui.press('down')
            time.sleep(1.5)

if __name__ == "__main__":
    main()