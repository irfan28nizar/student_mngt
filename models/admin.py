class Admin:
    def __init__(self,admin_id,username,password_hash):
        self.admin_id=admin_id
        self.username=username
        self.password_hash=password_hash
    def __repr__(self):
        return (
        f"Admin_id={self.admin_id},"
        f"Username={self.username})")
    