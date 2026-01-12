USER = "admin"

def admin_required(func):
    def wrap():
        if USER != "admin":
            raise PermissionError
        return func()
    return wrap

@admin_required
def dashboard():
    print("Admin Panel")

dashboard()