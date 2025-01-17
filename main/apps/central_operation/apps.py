from django.apps import AppConfig
import threading
import requests
import time
from main.apps.central_operation.services.central_operation import TopicSubscriber

class CentralOperationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main.apps.central_operation'
    
    # 初始重新訂閱中央topic
    def ready(self):
        # 確認只在 runserver 指令執行時執行邏輯
        import sys
        if len(sys.argv) > 1 and sys.argv[1] == "runserver":
            threading.Thread(target=self.run_custom_api, daemon=True).start()

    def run_custom_api(self):
        # 延遲以確保伺服器已啟動
        time.sleep(1)
        try:
            payload_dict = {}
            response_detail = TopicSubscriber.resubscribe(payload_dict)
            print("resubscribe detail: ", response_detail)
        except Exception as e:
            print(f"執行 API 時發生錯誤: {e}")
