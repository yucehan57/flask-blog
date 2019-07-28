# A micro blog that is being developed using Flask

### Still under construction:

End goal is to build a micro blog using Flask micro framework. Blog
will provide User authentication system (register & login), privilige to add, delete, and edit posts to authenticated users, and allow these users to create & update their profile pages.

### Likely future functionalities:
Comment functionality for users, extended user profile page, 'fetch random blog post functionality'...

### Who are our target audience?
The blog will try to cater to finance, business, programming lovers.
Available sections may vary as development proceeds further.


### Installation

Clone the repo, create virtual environment:

    $ git clone https://github.com/yucehan57/flask-blog.git
    $ virtualenv env
    $ source/env/bin/activate
    
Create database in shell:

    $ python
    > db.create_all()
    
And, run the server:

    $ python blog.py
