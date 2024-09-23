from django.views.decorators.http import require_POST
from main.utils.logger import log_trigger
from main.utils.packet import unpacking
from django.http import JsonResponse
from main.apps.central_operation.services.file_metadata import ModelMetadataWriter
from main.apps.central_operation.services.agent_operation import ModelFileManager
from main.apps.central_operation.services.agent_operation import InferenceFileManager
from main.apps.central_operation.services.file_operation import FileManager
import os
import zipfile
from io import BytesIO

@log_trigger("INFO")
@require_POST
def download(request):
    data_dict = unpacking(request)

    model_uid_str = data_dict['model_uid']
    payload_dict = {"uid": model_uid_str}
    model_metadata_dict = ModelMetadataWriter.retrieve(payload_dict)

    model_uid_str = model_metadata_dict['uid']
    inference_template_uid_str = model_metadata_dict['inference_template_uid']

    current_dir_str = os.getcwd()
    previous_dir_str = os.path.dirname(current_dir_str)
    # folder_path_str = previous_dir_str + '/inference_file_system/' + model_uid_str
    folder_path_str = '/inference_file_system/' + model_uid_str
    file_path_str = folder_path_str + '/template'

    payload_dict = {"file_path": file_path_str}
    exist_bol = FileManager.check(payload_dict)

    if not exist_bol:
        payload_dict = {'inference_uid': inference_template_uid_str}
        file = InferenceFileManager.download(payload_dict)
        print("file: ",file)

        download_zip_path = '/tmp/download_folder.zip'
        with open(download_zip_path, 'wb') as f:
            f.write(file.getvalue())

   
        with open(download_zip_path, 'rb') as f:
            payload_dict = {
                'file': f,
                'folder_path': file_path_str
            }
            FileManager.save(payload_dict)
        
        #----刪除暫存的zip檔------
        os.remove(download_zip_path)

    response_dict = {"detail":"File downloaded successfully"}
    return JsonResponse(response_dict, status=200)

