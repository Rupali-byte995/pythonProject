#self  keyword practice
class My_class:
    f_name=None
    l_name=None
    def print_my_name(self,l_name):
        print("Name is ",self.f_name,"l name",l_name)


pramod_obj=My_class()
rupali_obj=My_class()
pramod_obj.f_name='Pramod'

pramod_obj.print_my_name("PP")