from lib.user import User

"""
When we construct a user with properties
We can get these properties back
"""
def test_constructs_user():
    user = User(1, "Ben", "ben@hotmail.com")
    assert user.id == 1
    assert user.username == "Ben"
    assert user.email == "ben@hotmail.com"

"""
When we have two identical user objects
They are considered equal
"""
def test_identical_user_objects_considered_equal():
    user_1 = User(1, "Ben", "ben@hotmail.com")
    user_2 = User(1, "Ben", "ben@hotmail.com")
    assert user_1 == user_2

"""
We can format to strings nicely
"""
def test_user_formats_nicely():
    user = User(1, "Ben", "ben@hotmail.com")
    assert str(user) == "User(1, Ben, ben@hotmail.com)"