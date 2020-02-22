# Make and Admin insatance, and call show_privileges() to show that everything is working correctly

import privileges as p

my_admin = p.Admin('justin', 'williams', 11)
my_admin.privileges.show_privileges()