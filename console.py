import pdb 
from models.Class import Class
from models.enrollment import Enrollment
from models.member import Member

import repositories.class_repository as class_repository 
import repositories.member_repository as member_repository
import repositories.enrollment_repository as enrollment_repository

class_repository.delete_all()
member_repository.delete_all()

member1 = Member('Vlad', "Von Carstein", 500, "standard")
member2 = Member('Isabella', 'Von Carstein', 400, "standard")
member_repository.save(member1)
member_repository.save(member2)

class1 = Class("Yoga 101", 'Yoga')
class2 = Class("Lifting for beginners", 'Weights')
class_repository.save(class1)
class_repository.save(class2)

enrollment1 = Enrollment(member1, class1)
enrollment_repository.save(enrollment1)


pdb.set_trace()