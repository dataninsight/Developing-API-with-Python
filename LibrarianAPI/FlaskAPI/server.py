# python -m venv venv
# ./venv/Scripts/activate
# pip install flask
# python -m pip install --upgrade pip
# pip3 install -r requirements.txt
# env | grep VIRTUAL_ENV


from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from random import randrange

app = Flask(__name__)
api = Api(app)

my_books = [{"title":"title1","content":"content1","id":1},
            {"title":"title2","content":"content2","id":2}]

librarian_put_args = reqparse.RequestParser()
librarian_put_args.add_argument("title", type=str, help="Name of the Book", required=True)
librarian_put_args.add_argument("content", type=str, help="Description of the Book", required=True)
librarian_put_args.add_argument("id", type=int, help="ID", required=True)

resource_fields = {
	'title': fields.String,
	'content': fields.String,
	'id': fields.Integer,
}


def find_book_by_id(id:int):
    for i in my_books:
        if i["id"]==id:
            return i

def find_id_by_book(id:int):
    for i,n in enumerate(my_books):
        if n["id"]==id:
            return i
            
class Book(Resource):
    def get(self):
        return my_books
    
    @marshal_with(resource_fields)
    def get(self, id: int):
        book = find_book_by_id(id)
        if not book:
            abort(404, message="Could not find book with that id")
        return book
    
    @marshal_with(resource_fields)
    def post(self, id: int):
        args =librarian_put_args.parse_args()
        book = dict()
        book['title']=args['title'], 
        book['content']=args['content'],
        if args['id']==None:
            book['id']=randrange(3,1000000)
        else:
            book['id']=args['id']
        my_books.append(book)
        return book
    
    @marshal_with(resource_fields)
    def put(self, id: int):
        args =librarian_put_args.parse_args()
        index = find_id_by_book(id)
        if index == None:
            abort(404, message="Could not find book with that id")
        book = dict()
        book['title']=args['title'], 
        book['content']=args['content'],
        if args['id']==None:
            book['id'] = id
        else:
            book['id']=args['id']
        my_books[index] = book
        return book, 201
    
    @marshal_with(resource_fields)
    def patch(self, id: int):
        args =librarian_put_args.parse_args()
        index = find_id_by_book(id)
        if index == None:
            abort(404, message="Could not find book with that id")
        if args['title']:
            my_books[index].title=args['title']
        if args['content']:
            my_books[index].content=args['content']
        if args['id']:
            my_books[index].content=args['id']
        return my_books[index], 201

        
    @marshal_with(resource_fields)
    def delete(self, id: int):
        index = find_id_by_book(id)
        if index == None:
            abort(404, message="Could not find book with that id")
        del my_books[index]
        return '', 204


api.add_resource(Book, "/books/<int:id>")

if __name__ == "__main__":
	app.run(debug=True)
