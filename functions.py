def load_message(name):
    with open(' resourses/txt_files/'+name+'.txt', encoding='utf8') as file:
        return file.read()

