import pdftables_api
import os
c = pdftables_api.Client('KEY')

dir="folder_tmp"
files=os.listdir(dir)
print(files)
for file in files:
    filename, file_extension = os.path.splitext("{}/{}".format(dir,file))
    print("Procesando {}".format(filename))
    c.xlsx('{}.pdf'.format(filename), '{}.xlsx'.format(filename))
