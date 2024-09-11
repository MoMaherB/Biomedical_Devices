from app import db, User, app  # Importing db, Posts, and app instance from app.py

# # Dummy data
My_dict = [
    {
        "user_name": "Maher",
        "password": "password",
    },
     {
        "user_name": "Fadel",
        "password": "password123",
    }
]

# Use application context to interact with the database
with app.app_context():
    db.drop_all()  # Optional: Clear all existing tables
    db.create_all()  # Create all 
    print("Datbase Created Succsessfully")

    # Add each post from the dummy data
    for mypost in My_dict:
        post_instance = User(user_name=mypost['user_name'], password=mypost['password'])
        db.session.add(post_instance)
    
    db.session.commit()  # Commit the session after adding all posts
    print(User.query.all())
    print(User.query.get(2))
    print(User.query.get(1))


