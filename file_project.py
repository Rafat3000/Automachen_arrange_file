import os
import shutil


folder="data"

# open folder data
os.chdir(folder)  # change directory = folder

for file in os.listdir('.'):
    *file_name , file_extinsion = file.split('.')
    print(f'{file_name} : {file_extinsion}')

    if file_extinsion in ['png','jpg','jpeg']:
       
       if not os.path.exists('images'):
           os.mkdir("images") # Great folder  
    
       shutil.move(file,"images")
    
      # print(f'{file_name} : image')
    elif file_extinsion in ['word','txt','pdf','xslx','csv']:
         
        if not os.path.exists('documants'):

            os.mkdir("documants") # Great folder
        shutil.move(file,"documants") 
      
       # print(f'{file_name}: document')
    elif file_extinsion in ['py','html','css']:
         
        if not os.path.exists('code'):

            os.mkdir("code") # Great folder
        shutil.move(file,"code") 

    elif file_extinsion in ['mp4']:
         
        if not os.path.exists('vidio'):

            os.mkdir("vidio") # Great folder
        shutil.move(file,"vidio")

   
    else:
        if not os.path.isdir(file):
            if not os.path.exists('other'):
              

              os.mkdir("other") # Great folder
        shutil.move(file,"other")

         
        
    
