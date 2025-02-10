from openpyxl import load_workbook
import os
from pathlib import Path
import cv2
from ultralytics import YOLO
from detection.models import DetectionSettings

# Словарь для преобразования индексов классов в символы
CLASS_TO_SYMBOL = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: 'A', 11: 'B', 12: 'C', 13: 'E', 14: 'H', 15: 'K', 16: 'M', 17: 'O', 18: 'P', 19: 'T', 20: 'X', 21: 'Y'
}

settings = DetectionSettings.load()

plate_model = YOLO(settings.plate_file.path)
symbol_model = YOLO(settings.symbol_file.path)

def process_frame(frame, source_name, CONFIDENCE_THRESHOLD):
    """Обрабатывает кадр."""
    # Применение CLAHE для улучшения контраста
    lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)
    limg = cv2.merge((cl, a, b))
    frame = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

    plate_results = plate_model(frame)
    coordinates = []
    plate_text = ""  # Инициализация переменной plate_text
    plate_img = None  # Инициализация переменной plate_img
    symbols = []  # Инициализация переменной symbols
    symbols_ratio = 0.0

    for result in plate_results:
        boxes = result.boxes
        for box in boxes:
            confidence = box.conf[0]
            
            if confidence < CONFIDENCE_THRESHOLD:
                continue
            
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            plate_img = frame[y1:y2, x1:x2]

            # Распознавание текста с использованием модели YOLO для символов
            symbol_results = symbol_model(plate_img)
            symbols = []
            for symbol_result in symbol_results:
                symbol_boxes = symbol_result.boxes
                for symbol_box in symbol_boxes:
                    symbol_confidence = symbol_box.conf[0]
                    if symbol_confidence < CONFIDENCE_THRESHOLD:
                        continue
                    symbol_x1, symbol_y1, symbol_x2, symbol_y2 = map(int, symbol_box.xyxy[0])
                    symbol_label = int(symbol_box.cls[0].item())  # Извлечение индекса класса
                    symbols.append((symbol_label, symbol_confidence, symbol_x1))

            symbols_ratio = round((float(sum([symbol[1] for symbol in symbols]) / len(symbols))), 2)

            # Сортировка символов по координате x
            symbols.sort(key=lambda x: x[2])
            plate_text = ''.join([CLASS_TO_SYMBOL[symbol[0]] for symbol in symbols])

            # Проверка формата распознанного текста
            if is_valid_license_plate(plate_text):
                coordinates.append((x1, y1, x2, y2))
            else:
                plate_text = ""

    return frame, coordinates, plate_text, plate_img, symbols_ratio

def is_valid_license_plate(plate_text):
    """Проверяет, соответствует ли распознанный текст формату российского номерного знака."""
    if len(plate_text) not in [8, 9]:
        return False
    if not plate_text[0].isalpha() or not plate_text[1:4].isdigit() or not plate_text[4:6].isalpha():
        return False
    if len(plate_text) == 9 and not plate_text[6:9].isdigit():
        return False
    if len(plate_text) == 8 and not plate_text[6:8].isdigit():
        return False
    return True