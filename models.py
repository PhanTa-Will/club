import gc

mem_list =[]

class club_members :
    def __init__(self,first_name,last_name,idd,status):
        self.first_name =first_name
        self.last_name = last_name
        self.idd = idd
        self.status=status

def has_instance(cls):
    return any(isinstance(obj, cls) for obj in gc.get_objects())

    