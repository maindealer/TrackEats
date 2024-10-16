# camera.py

import cv2
import pytesseract

class Camera:
    def __init__(self):
        # 카메라 초기화
        self.cap = cv2.VideoCapture(0)
    
    def capture_image(self):
        """카메라에서 이미지를 캡처하여 반환합니다."""
        ret, frame = self.cap.read()
        if not ret:
            raise ValueError("카메라로부터 이미지를 캡처할 수 없습니다.")
        return frame

    def release(self):
        """카메라 자원을 해제합니다."""
        self.cap.release()
        cv2.destroyAllWindows()

class ImageProcessor:
    def __init__(self):
        # Tesseract 경로 설정 (필요시 맞춤 설정)
        pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'  # 경로는 시스템에 맞게 설정

    def analyze_image(self, image):
        """이미지를 분석하여 텍스트와 로고를 인식합니다."""
        text = self.recognize_text(image)
        # 로고 인식 로직은 추가할 수 있습니다 (추후 딥러닝 모델 연계 가능)
        logo = self.detect_logo(image)
        return text, logo

    def recognize_text(self, image):
        """이미지에서 텍스트를 인식하여 반환합니다."""
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray_image)
        return text

    def detect_logo(self, image):
        """이미지에서 로고를 인식하는 로직을 추가할 수 있습니다. (임시로 None 반환)"""
        # 로고 인식 로직 (예: 딥러닝 모델을 사용한 이미지 분류)
        return None
