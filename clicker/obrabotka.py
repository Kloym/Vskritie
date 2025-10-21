import pyautogui
import pytesseract
from PIL import ImageGrab, Image
import time

pytesseract.pytesseract.tesseract_cmd = r'D:\\Tesseract\\tesseract.exe'

# --- Настройки координат ---
first_patient = (984, 185)
patient_step = 19
patients_per_page = 30
total_patients = 261

# --- Координаты области диагноза ---
diagnosis_left = 1419
diagnosis_top = 178
diagnosis_right = 1481
diagnosis_bottom = 193
diagnosis_step = patient_step

# --- Прочие координаты и параметры (примерные, подправь под себя) ---
first_code = (990, 885)
code_step = 19
max_codes = 10

DELAY_SAVE = 1.5
DELAY = 0.6

# --- Получение диагноза для пациента ---
def get_diagnosis(patient_num):
    y_shift = patient_num * diagnosis_step
    img = ImageGrab.grab(bbox=(
        diagnosis_left,
        diagnosis_top + y_shift,
        diagnosis_right,
        diagnosis_bottom + y_shift
    ))
    img = img.resize((img.width * 3, img.height * 3), Image.LANCZOS)
    img = img.convert('L')
    text = pytesseract.image_to_string(img, lang='eng')
    return text.strip().lower()

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
    pyautogui.click(964, 841)
    time.sleep(DELAY)
    pyautogui.click(775, 841)
    time.sleep(DELAY)

def process_all_codes():
    for code_index in range(max_codes):
        process_code(code_index)

# --- Действия с картой пациента ---
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
    time.sleep(DELAY_SAVE * 1.7)

    pyautogui.press('f2')
    time.sleep(DELAY_SAVE * 1.7)

    pyautogui.press('esc')
    time.sleep(DELAY * 2)

# --- Основной цикл ---
def main():
    print("Старт через 5 секунд...")
    time.sleep(5)
    i = 0
    pagedown_count = 0
    while i < total_patients:
        for patient_on_screen in range(patients_per_page):
            if i >= total_patients:
                break
            patient_y = first_patient[1] + patient_on_screen * patient_step
            pyautogui.click(first_patient[0], patient_y)
            time.sleep(DELAY)
            diagnosis = get_diagnosis(patient_on_screen)
            print(f"Диагноз пациента {i+1}: {diagnosis}")
            if diagnosis and diagnosis[0] == 'c':
                process_all_codes()
            process_patient_card(patient_y)
            i += 1
            time.sleep(1)
        if i < total_patients:
            pyautogui.click(989, 736)
            time.sleep(1)
            pyautogui.press('pagedown')
            pagedown_count += 1
            time.sleep(1.5)
            pyautogui.press('down')
            time.sleep(1.5)
            pyautogui.click(first_patient[0], first_patient[1])
            time.sleep(1.5)

if __name__ == "__main__":
    main()