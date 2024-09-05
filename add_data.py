from app import db, Posts, app  # Importing db, Posts, and app instance from app.py

# Dummy data
My_dict = [
    {
        "name": "Alice Johnson",
        "title": "My First Blog Post",
        "post": "This is my first blog post! I'm excited to share my thoughts with the world."
    },
    {
        "name": "Bob Smith",
        "title": "Exploring Nature",
        "post": "Nature is full of beauty and adventure. I had a great hike last weekend!"
    },
    {
        "name": "Charlie Brown",
        "title": "Cooking 101",
        "post": "Today, I want to share my favorite pasta recipe. It's simple and delicious!"
    },
    {
        "name": "David Wilson",
        "title": "Traveling the World",
        "post": "Traveling is my passion. I've visited over 20 countries and loved every moment!"
    },
    {
        "name": "Emma Davis",
        "title": "Tech Innovations",
        "post": "The tech industry is evolving rapidly. Let's talk about the latest gadgets!"
    },
    {
        "name": "Fiona White",
        "title": "Health and Wellness",
        "post": "Taking care of our health is vital. Here are some tips for a healthier lifestyle."
    },
    {
        "name": "George Green",
        "title": "My Art Journey",
        "post": "Art has been a significant part of my life. I want to showcase some of my recent works."
    },
    {
        "name": "Hannah Blue",
        "title": "Book Recommendations",
        "post": "Reading is a fantastic escape. Here are my top 5 book recommendations!"
    },
    {
        "name": "Ian Black",
        "title": "The World of Sports",
        "post": "Sports bring people together. Let's discuss the latest in football!"
    },
    {
        "name": "Julia Red",
        "title": "Gardening Tips",
        "post": "Gardening can be incredibly rewarding. Here are some tips for beginners!"
    }
]

# Use application context to interact with the database
with app.app_context():
    # Clear existing data if necessary
    db.drop_all()  # Optional: Clear all existing tables
    db.create_all()  # Create all tables

    # Add each post from the dummy data
    for mypost in My_dict:
        post_instance = Posts(name=mypost['name'], title=mypost['title'], post=mypost['post'])
        db.session.add(post_instance)
    
    db.session.commit()  # Commit the session after adding all posts
    print("Dummy data added successfully!")
