from datetime import date

from high_level_step_objects.data.user import User, Gender, Hobby

student = User(
    first_name='First Name',
    last_name='Last Name',
    email='email@test.qa',
    gender=Gender.FEMALE,
    phone='1234567890',
    date_of_birth=date(1999, 9, 1),
    subjects='Maths',
    hobbies=(Hobby.READING,),
    picture='test_image.png',
    address='test address',
    state='Haryana',
    city='Karnal'
)