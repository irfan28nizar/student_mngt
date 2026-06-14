class Notice:
    def __init__(self, id, title, content, created_at,is_deleted):
        self.id = id
        self.title = title
        self.content = content
        self.created_at = created_at
        self.is_deleted = is_deleted

    def __repr__(self):
        return(
            "Notice("
            f"id={self.id},"
            f"Title={self.title},"
            f"Content={self.content},"
            f"Created_at={self.created_at}"
            f"is_deleted={self.is_deleted}"
            ")"
        )
    
    def notice_to_dict(self):
        return{
            "id":self.id,
            "title":self.title,
            "content":self.content,
            "created_at":self.created_at
        }