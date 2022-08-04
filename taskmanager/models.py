from taskmanager import db


class Category(db.Model):
    # scheme for the category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=True)
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True)


    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name


class Task(db.Model):
    # Scheme for the task model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String, primary_key=True)
    task_description = db.Column(db.String(50), unique=True, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )
