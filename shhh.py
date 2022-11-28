from user.models import  *

с1 = Course.objects.get(id=2)
c1.get_end_date()