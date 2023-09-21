from req_module import *

db=Request_Firebase(project_id='requestfirebase108')



#db.input_data(path=f'10_06_2023',data={99998:{'name':'t iqbal','proffession':'house wife','dieasese':'kidney','doctor name':'ziauddin'}})
#datas=db.show_data()
#print(datas['10_06_2023']['99998']['name'])
#db.delete_data(path=f"{151110+i}")


sdb=Request_Firebase_Storage()

#sdb.upload_file(path='py',attribute='condition',random_name_extention=False,file_name='demo2.py')
#sdb.download_files(path='js',attribute='condition')
#sdb.delete_files(path='py',attribute='name')
#sdb.delete_files(path='py',delete_path=True)

#my_db_folders=sdb.folder_list()
#print(my_db_folders)
