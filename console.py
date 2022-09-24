import pdb 
from models.Class import Class
from models.member import Member

import reposirories.class_repository as class_repository 
import reposirories.member_repository as member_repository

class_repository.delete_all()
member_repository.delete_all()

member1 = Member('Vlad', "Von Carstein", 500, "standard")
member2 = Member('Isabella', 'Von Carstein', 400, "standard")
member_repository.save(member1, member2)
class1 = Class("Yoga 101", 'Yoga')
class_repository.save(class1)

pdb.set_trace()