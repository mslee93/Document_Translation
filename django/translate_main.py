import os
import time
from . import translate_ppt

# exe_path = r'"C:\Program Files (x86)\ABBYY FineReader 12/FineCMD.exe"'
# input_folder_path = os.path.join(os.getcwd(), 'ocr', 'Input_Temp')
# output_folder_path = os.path.join(os.getcwd(), 'ocr', 'Output_Temp')


class FolderControl(object):
    # input_folder_path = "/python3env/bin/api/translate/Input_Temp"
    # output_folder_path = "/python3env/bin/api/translate/Output_Temp"
    input_folder_path = str(os.path.join(os.getcwd(), 'translate', 'Input_Temp'))
    output_folder_path = str(os.path.join(os.getcwd(), 'translate', 'Output_Temp'))

    @staticmethod
    def deleteOldFiles(days=1):
        now = time.time()
        for folder in [FolderControl.input_folder_path, FolderControl.output_folder_path]:
            for filename in os.listdir(folder):
                if os.path.getmtime(os.path.join(folder, filename)) < now - days * 86400:
                    if os.path.isfile(os.path.join(folder, filename)):
                        try:
                            os.remove(os.path.join(folder, filename))
                        except:
                            pass


class File(object):
    def __init__(self, job_id, file_name, file_data):
        self.job_id = job_id
        self.temp_file_name = str(job_id) + os.path.splitext(os.path.basename(file_name))[-1]
        # self.temp_file_name = str(uuid4()) + os.path.splitext(os.path.basename(file_name))[-1]
        self.file_data = file_data
        self.input_file_path = None
        self.__saveInputFile()
        FolderControl.deleteOldFiles()

    def __saveInputFile(self):
        input_file_path = str(os.path.join(FolderControl.input_folder_path, self.temp_file_name))
        with open(input_file_path, 'wb') as f:
            f.write(self.file_data)

        self.input_file_path = input_file_path

    def deleteInputFile(self):
        if self.input_file_path is not None:
            if os.path.exists(self.input_file_path):
                os.remove(self.input_file_path)
                self.input_file_path = None


class PPTX(File):
    def __init__(self, job_id, file_name, file_data, src_lang, tgt_lang, eng):
        super(PPTX, self).__init__(job_id, file_name, file_data)
        self.src_lang = src_lang
        self.tgt_lang = tgt_lang
        self.eng = eng
        self.output_file_path = None

    def run(self):
        temp_output_file_path = str(os.path.join(FolderControl.output_folder_path,
                                                 os.path.splitext(os.path.basename(self.temp_file_name))[0]+'.pptx'))
        translate_ppt.run(self.input_file_path, temp_output_file_path, self.src_lang, self.tgt_lang, self.eng)
        self.output_file_path = temp_output_file_path
        super(PPTX, self).deleteInputFile()

    def deleteOutputFile(self):
        if self.output_file_path is not None:
            if os.path.exists(self.output_file_path):
                os.remove(self.output_file_path)
                self.output_file_path = None

    def result(self):
        with open(self.output_file_path, "rb") as f:
            b = f.read()
        self.deleteOutputFile()

        return b


