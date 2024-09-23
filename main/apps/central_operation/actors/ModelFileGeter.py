from django.views.decorators.http import require_POST
from main.utils.logger import log_trigger
from main.utils.packet import unpacking
from django.http import JsonResponse
from main.apps.central_operation.services.file_metadata import ModelMetadataWriter
from main.apps.central_operation.services.agent_operation import ModelFileManager
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
    
    source_str = model_metadata_dict['source']
    
    file_name_str = model_uid_str

    if not source_str:
        model_uid_str = source_str

    current_dir_str = os.getcwd()
    previous_dir_str = os.path.dirname(current_dir_str)
    # folder_path_str = previous_dir_str + '/inference_file_system/' + model_uid_str
    folder_path_str = '/inference_file_system/' + model_uid_str
    file_extension_str = model_metadata_dict['file_extension']
    file_path_str = folder_path_str + '/' + file_name_str + '.' + file_extension_str


    payload_dict = {"file_path": file_path_str}
    exist_bol = FileManager.check(payload_dict)

    if not exist_bol:
        model_access_token_str = model_metadata_dict['access_token']
        payload_dict = {
                        'model_uid': model_uid_str,
                        'model_access_token': model_access_token_str
                       }
        file = ModelFileManager.download(payload_dict)

        
        download_zip_path = '/tmp/download_folder.zip'
        with open(download_zip_path, 'wb') as f:
            f.write(file.getvalue())
        
        with open(download_zip_path, 'rb') as f:
            payload_dict = {
                'file': f,
                'folder_path': folder_path_str
            }
            FileManager.save(payload_dict)
        
        #----刪除暫存的zip檔------
        os.remove(download_zip_path)

    response_dict = {"detail":"File downloaded successfully"}
    return JsonResponse(response_dict, status=200)

