from lib.user_repository import UserRepository
from lib.user import User

"""
When we call all
We get a list of all user objects
"""
def test_list_all_users(db_connection):
    db_connection.seed("seeds/social_network.sql")
    user_repository = UserRepository(db_connection)
    users = user_repository.all()
    assert users == [
        User(1, 'natalie', 'natalie@email.com'),
        User(2, 'jayne', 'jayne@email.com'),
        User(3, 'matt', 'matt@email.com')
    ]

"""
When we call find with a user id
We get the User object of that id
"""
def test_find_user_with_id(db_connection):
    db_connection.seed("seeds/social_network.sql")
    user_repository = UserRepository(db_connection)
    user = user_repository.find(3)
    assert user == User(3, 'matt', 'matt@email.com')

"""
When we call UserRepository#create with a User object
That user is reflected in the list when we call UserRepository#all
"""
def test_create_user_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    user_repository = UserRepository(db_connection)
    user = User(None, "james", "james@email.com")
    assert user_repository.create(user) == None
    assert user_repository.all() == [
        User(1, 'natalie', 'natalie@email.com'),
        User(2, 'jayne', 'jayne@email.com'),
        User(3, 'matt', 'matt@email.com'),
        User(4, 'james', 'james@email.com')
    ]

"""
When we call UserRepository#delete with a user id
It is reflected in the list when we call UserRepository#all
"""
def test_delete_user_with_id(db_connection):
    db_connection.seed("seeds/social_network.sql")
    user_repository = UserRepository(db_connection)
    assert user_repository.delete(3) == None
    assert user_repository.all() == [
        User(1, 'natalie', 'natalie@email.com'),
        User(2, 'jayne', 'jayne@email.com')
    ]

"""
When we call UserRepository#update with a user object
It is reflected in the list when we call UserRepository#all
"""
def test_update_user_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    user_repository = UserRepository(db_connection)
    user = user_repository.find(1)
    user.username = "nataliec"
    user.email = "nclark@mail.co.uk"
    assert user_repository.update(user) == None
    assert user_repository.all() == [
        User(1, 'nataliec', 'nclark@mail.co.uk'),
        User(2, 'jayne', 'jayne@email.com'),
        User(3, 'matt', 'matt@email.com')
    ]

