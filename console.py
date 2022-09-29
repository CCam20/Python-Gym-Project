import pdb 
from models.Class import Class
from models.enrollment import Enrollment
from models.member import Member

import repositories.class_repository as class_repository 
import repositories.member_repository as member_repository
import repositories.enrollment_repository as enrollment_repository

class_repository.delete_all()
member_repository.delete_all()
enrollment_repository.delete_all()

member1 = Member('Sharon', "Broderick", 43, "Standard")
member2 = Member('Steven', 'Ramage', 41, "Standard")
member3 = Member('Vernon', 'Grate', 31, 'Standard')
member4 = Member("Lisa","Tharp",36, 'Standard')
member5 = Member("Sean","Green",28, "Standard")
member6 = Member("Lloyd","Hillman",19, "Standard")
member7 = Member("Greta","Faust", 29, "Standard")
member8 = Member("Peter","Andrew",19, "Premium")
member9 = Member("Tiana","Crawford",25, "Premium")
member10 = Member("Kenzie","Hunter",34, "Premium")
member11 = Member("Lara","Millar",24, "Premium")
member12 = Member("Martin","McGregor",37, "Premium")
member_repository.save(member1)
member_repository.save(member2)
member_repository.save(member3)
member_repository.save(member4)
member_repository.save(member5)
member_repository.save(member6)
member_repository.save(member7)
member_repository.save(member8)
member_repository.save(member9)
member_repository.save(member10)
member_repository.save(member11)
member_repository.save(member12)



class1 = Class("Yoga 101", 'Yoga', '01/10/2022', 10)
class2 = Class("Lifting for Beginners", 'Weights', '01/10/2022', 5)
class3 = Class("Running for Dummies", 'Cardio','01/10/2022', 20)
class4 = Class("Wishful Shrinking", "Cardio", "01/10/2022", 10)
class5 = Class("Power Hour", "General", "02/10/2022" ,10)
class6 = Class("Ex-Press", "Weights", '02/10/2022', 5)
class7 = Class("Yin Meets Yang", "Yoga", "02/10/2022", 10)
class8 = Class("F-abs Fridays", "General", "02/10/2022", 10)
class9 = Class("Strike a Pose", "Yoga", "03/10/2022" ,10)
class10 = Class("Walk this Weigh", "Cardio", "03/10/2022", 20)
class_repository.save(class1)
class_repository.save(class2)
class_repository.save(class3)
class_repository.save(class4)
class_repository.save(class5)
class_repository.save(class6)
class_repository.save(class7)
class_repository.save(class8)
class_repository.save(class9)
class_repository.save(class10)



enrollment1 = Enrollment(member1, class1)
enrollment_repository.save(enrollment1)
enrollment2 = Enrollment(member1, class2)
enrollment_repository.save(enrollment2)
enrollment3 = Enrollment(member3, class3)
enrollment_repository.save(enrollment3)

