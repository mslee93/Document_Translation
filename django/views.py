from .translate_main import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest
from .my_grpc import translate_pb2_grpc
from .my_grpc import translate_pb2
from .my_grpc.translate_stub import TRANSLATE_STUB
import os

@csrf_exempt
def TRANSLATE_API(request, _type):

    def __invalid(status, message):
        _response = HttpResponseBadRequest('')
        _response['status'] = status
        _response['message'] = message
        return _response

    if request.method == 'POST':
        if _type in ['xlsx', 'pptx']:
            data = request.POST.copy()
            job_id = data.get('job_id')
            src_lang = data.get('src_lang')
            tgt_lang = data.get('tgt_lang')
            eng = data.get('eng')
            file_data = request.FILES['file'].read()
            file_name = request.FILES['file'].name.replace('"', '')
            extension = os.path.splitext(os.path.basename(file_name))[-1].replace('.','')
            if file_data and file_name:

                if extension in ['pptx', 'xlsx']:
                    if job_id and src_lang and tgt_lang and eng:
                        # try:

                        grpc_request_parameter = translate_pb2.translateRequest(job_id=job_id, file_name=file_name, file_data=file_data, src_lang=src_lang, tgt_lang=tgt_lang, eng=eng)
                        response = TRANSLATE_STUB.translate(grpc_request_parameter)

                        if extension == 'pptx':
                            response = HttpResponse(response.file_data, content_type='application/vnd.openxmlformats-officedocument.presentationml.presentation')
                            response['Content-Disposition'] = 'attachment; filename="' + job_id + '.pptx"'
                        elif extension == 'xlsx':
                            response = HttpResponse(response.file_data, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                            response['Content-Disposition'] = 'attachment; filename="' + job_id + '.xlsx"'
                        response['status'] = '000'
                        response['message'] = 'Done'

                        return response
                        # except:
                        #     return __invalid('100', 'PPTX Engine Error')
                    else:
                        return __invalid('001', 'Input Error')
                else:
                    return __invalid('010', 'Invalid File Format')
            else:
                return __invalid('011', 'No File')
        else:
            return __invalid('300', 'Invalid URL')
    else:
        return __invalid('500', 'Invalid Request')


