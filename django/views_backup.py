from .translate_main import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest
import os

@csrf_exempt
def TRANSLATE_API(request, _type):

    def __invalid(status, message):
        _response = HttpResponseBadRequest('')
        _response['status'] = status
        _response['message'] = message
        return _response

    if request.method == 'POST':
        data = request.POST.copy()
        job_id = data.get('job_id')
        src_lang = data.get('src_lang')
        tgt_lang = data.get('tgt_lang')
        eng = data.get('eng')
        file_data = request.FILES['file'].read()
        file_name = request.FILES['file'].name.replace('"', '')
        extension = os.path.splitext(os.path.basename(file_name))[-1].replace('.','')
        if file_data and file_name:
            if _type == 'pptx':
                if extension == 'pptx':
                    if job_id and src_lang and tgt_lang and eng:
                        # try:
                        task = PPTX(job_id, file_name, file_data, src_lang, tgt_lang, eng)
                        task.run()
                        response = HttpResponse(task.result(), content_type='application/vnd.openxmlformats-officedocument.presentationml.presentation')
                        response['Content-Disposition'] = 'attachment; filename="' + job_id + '.pptx"'
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
                return __invalid('300', 'Invalid URL')
        else:
            return __invalid('011', 'No File')
    else:
        return __invalid('500', 'Invalid Request')


