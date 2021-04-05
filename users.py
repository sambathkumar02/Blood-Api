users={
    '1':{
        'name':'mani',
        'email':'mani@mail.com',
        'blood_group':'A+'
    },
    '2':{
        'name':'prem',
        'email':'prem@mail.com',
        'blood_group':'B+'
    }
}


def create(data,id):
    if id not in users.keys():
        users[str(id)]=data
    else:
        print('id already exist')

def update(data,id):
    for key in data.keys():
        if data[key] != None: # cahnging values only for the fields not containing None.
            users[id][key]=data[key]
