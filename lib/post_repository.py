from lib.post import Post

class PostRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute(
            "SELECT * FROM posts ORDER BY id ASC"
        )
        posts = []
        for row in rows:
            post = Post(
                row["id"], row["title"], row["content"], row["total_views"], row["user_id"]
            )
            posts.append(post)
        return posts
    
    def find(self, post_id):
        rows = self._connection.execute(
            "SELECT * FROM posts WHERE id = %s", 
            [post_id]
        )
        row = rows[0]
        return Post(
            row["id"], row["title"], row["content"], row["total_views"], row["user_id"]
        )
    
    def create(self, post):
        self._connection.execute(
            "INSERT INTO posts (title, content, total_views, user_id) VALUES (%s, %s, %s, %s)", 
            [post.title, post.content, post.total_views, post.user_id]
        )
        return None
    
    def delete(self, post_id):
        self._connection.execute(
            "DELETE FROM posts WHERE id = %s", 
            [post_id]
        )
        return None
    
    def update(self, post):
        self._connection.execute(
            "UPDATE posts SET title = %s, content = %s, total_views = %s, user_id = %s WHERE id = %s",
            [post.title, post.content, post.total_views, post.user_id, post.id]
        )
        return None