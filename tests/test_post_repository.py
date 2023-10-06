from lib.post_repository import PostRepository
from lib.post import Post

"""
When we call all
We get a list of all post objects
"""
def test_list_all_posts(db_connection):
    db_connection.seed("seeds/social_network.sql")
    post_repository = PostRepository(db_connection)
    posts = post_repository.all()
    assert posts == [
        Post(1, 'Title 1', 'Content 1', 576, 1),
        Post(2, 'Title 2', 'Content 2', 89, 2),
        Post(3, 'Title 3', 'Content 3', 123, 3)
    ]

"""
When we call find with a post id
We get the Post object of that id
"""
def test_find_post_with_id(db_connection):
    db_connection.seed("seeds/social_network.sql")
    post_repository = PostRepository(db_connection)
    post = post_repository.find(3)
    assert post == Post(3, 'Title 3', 'Content 3', 123, 3)

"""
When we call PostRepository#create with a Post object
That post is reflected in the list when we call PostRepository#all
"""
def test_create_post_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    post_repository = PostRepository(db_connection)
    post = Post(None, 'Title 4', 'Content 4', 14, 2)
    assert post_repository.create(post) == None
    assert post_repository.all() == [
        Post(1, 'Title 1', 'Content 1', 576, 1),
        Post(2, 'Title 2', 'Content 2', 89, 2),
        Post(3, 'Title 3', 'Content 3', 123, 3),
        Post(4, 'Title 4', 'Content 4', 14, 2)
    ]

"""
When we call PostRepository#delete with a post id
It is reflected in the list when we call PostRepository#all
"""
def test_delete_post_with_id(db_connection):
    db_connection.seed("seeds/social_network.sql")
    post_repository = PostRepository(db_connection)
    assert post_repository.delete(3) == None
    assert post_repository.all() == [
        Post(1, 'Title 1', 'Content 1', 576, 1),
        Post(2, 'Title 2', 'Content 2', 89, 2),
    ]

"""
When we call PostRepository#update with a post object
It is reflected in the list when we call PostRepository#all
"""
def test_update_post_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    post_repository = PostRepository(db_connection)
    post = post_repository.find(2)
    post.title = "Title Changed"
    post.content = "Content Changed"
    post.total_views = 35759
    assert post_repository.update(post) == None
    assert post_repository.all() == [
        Post(1, 'Title 1', 'Content 1', 576, 1),
        Post(2, 'Title Changed', 'Content Changed', 35759, 2),
        Post(3, 'Title 3', 'Content 3', 123, 3)
    ]

