class UserService:
    def __init__(self, db):
        self.db = db

    def get_user(self, user_id):
        return self.db.query('SELECT * FROM users WHERE id = ?', user_id)
