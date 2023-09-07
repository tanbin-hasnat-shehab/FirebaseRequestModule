from req_module import *

db=Request_Firebase(project_id='requestfirebase108')



#db.input_data(path=f'10_06_2023',data={99998:{'name':'t iqbal','proffession':'house wife','dieasese':'kidney','doctor name':'ziauddin'}})
#datas=db.show_data()
#print(datas['10_06_2023']['99998']['name'])
#db.delete_data(path=f"{151110+i}")


sdb=Request_Firebase_Storage()

#sdb.upload_file(path='js',file_name='demo.html')
#sdb.download_files(path='js')
#sdb.delete_files(path='js')
#my_db_folders=sdb.folder_list()
#print(my_db_folders)