# Store the user class in one module, and store the Privileges and Admin classes in a seperate module.
# In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.

from user import Users
from admin_priv import Admin, Privileges

my_admin = Admin('justin', 'williams', 11)
my_admin.privileges.show_privileges()