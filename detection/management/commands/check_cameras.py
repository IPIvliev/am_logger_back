from django.core.management import BaseCommand
from detection.models import Camera, DetectionSettings, Recognition
from detection.services.recognition import process_frame
import cv2
from datetime import datetime, timedelta, timezone
import os
from pathlib import Path
from django.core.files.base import ContentFile

class Command(BaseCommand):
    help = 'Опрашиваем камеры и определяем номера, если обнаружили рамку номера автомобиля'

    def add_arguments(self, parser):
        parser.add_argument('--test', type=str)

    def handle(self, *args, **kwargs):
        test = kwargs['test']

        settings = DetectionSettings.load()
        CONFIDENCE_THRESHOLD = settings.confidence_threshold

        cameras = Camera.objects.filter(status = True)
        
        for camera in cameras:
            if test:
                BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent.parent
                static_dir = os.path.join(BASE_DIR, 'static')
                filepath = static_dir + '/test_1.jpg'
                frame = cv2.imread(filepath)
            else:
                cap = cv2.VideoCapture(camera.url)
                ret, frame = cap.read()

            # Обрабатываем изображение
            frame, coordinates, plate_text, plate_img, symbols_ratio = process_frame(frame, camera.name, CONFIDENCE_THRESHOLD)

            if plate_text:
                # ДЛЯ ТЕСТОВ
                # print(f'Распознан номер {plate_text} по координатам {coordinates} с вероятностью {symbols_ratio}')

                time_now = datetime.today()    
                recognition_delay = time_now - timedelta(seconds = settings.delay)

                record_in_bd = Recognition.objects.filter(plate_text=plate_text).filter(created_at__gt = recognition_delay)
                
                """Сохраняет изображения и данные для датасета."""
                timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
                car_image_filename = f"{timestamp}_{plate_text}.jpg"
                plate_image_filename = f"{timestamp}_{plate_text}_plate.jpg"

                ret, buf = cv2.imencode('.jpg', plate_img)
                plate_img = ContentFile(buf.tobytes())

                ret, buf = cv2.imencode('.jpg', frame)
                car_image = ContentFile(buf.tobytes())

                if not record_in_bd:
                    record = Recognition.objects.create(
                        plate_text = plate_text,
                        source = camera,
                        ratio = symbols_ratio
                    )
                    record.plate_image.save(plate_image_filename, plate_img)
                    record.car_image.save(car_image_filename, car_image)
            else:
                print("Номер не найден на видео")

            
            


