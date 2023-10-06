from lib.database_connection import DatabaseConnection
from lib.user_repository import UserRepository
from lib.post_repository import PostRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# # Seed with some seed data
# connection.seed("seeds/social_network.sql")

# Create repository objects
user_repository = UserRepository(connection)
post_repository = PostRepository(connection)

# Print all users
for user in user_repository.all():
    print(user)

# Print all posts
for post in post_repository.all():
    print(post)
