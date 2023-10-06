from lib.post import Post

"""
When we construct a post with properties
We can get these properties back
"""
def test_constructs_post():
    post = Post(1, "My Title", "My Content", 5809, 1)
    assert post.id == 1
    assert post.title == "My Title"
    assert post.content == "My Content"
    assert post.total_views == 5809
    assert post.user_id == 1

"""
When we have two identical post objects
They are considered equal
"""
def test_identical_post_objects_considered_equal():
    post_1 = Post(1, "My Title", "My Content", 5809, 1)
    post_2 = Post(1, "My Title", "My Content", 5809, 1)
    assert post_1 == post_2

"""
We can format to strings nicely
"""
def test_post_formats_nicely():
    post = Post(1, "My Title", "My Content", 5809, 1)
    assert str(post) == "Post(1, My Title, My Content, 5809, 1)"