class Notice:
    def __init__(self, id, title, content, created_at):
        self.id = id
        self.title = title
        self.content = content
        self.created_at = created_at

    def __repr__(self):
        return(
            "Notice("
            f"id={self.id},"
            f"Title={self.title},"
            f"Content={self.content},"
            f"Created_at={self.created_at}"
            ")"
        )