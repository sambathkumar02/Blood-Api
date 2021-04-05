from flask import Flask
from flask_restful import Resource,Api,abort,reqparse,fields,marshal_with  #reparse for getting request data
import users,arg_parser
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)     #Flask app initialization
api=Api(app)              #Flask RESTAPI initialization
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'   #Database configuration
db=SQLAlchemy(app)        #initializing SQLAlchemy object



class UserModel(db.Model):
    id=db.Column(db.String(5),primary_key=True)
    name=db.Column(db.String(60),nullable=False)
    email = db.Column(db.String(60), nullable=False)
    blood_group = db.Column(db.String(3), nullable=False)


    def __repr__(self):
        return f"Donor(name= {self.name},email= {self.email}, blood_group={self.blood_group}"

#db.create_all()
# this method used when server is runnig for the first time


resources_fields={      # for making database instances serializable
    'id':fields.String,
    'name':fields.String,
    'email':fields.String,
    'blood_group':fields.String
}



post_req_parser=arg_parser.PostRequestParser() # calling parser for post request
update_req_parser=arg_parser.UpdateRequestParser()

class Users(Resource): # For CRUD options

    @marshal_with(resources_fields)  # It takes the return parameter and make it serializable
    def get(self,id):
        result=UserModel.query.filter_by(id=id).all()
        return result


    #@marshal_with(resources_fields)     (Needed only if it returns a database object to be serializable
    def post(self,id):
        args=post_req_parser.parse_args()
        user=UserModel(id=id,name=args['name'],email=args['email'],blood_group=args['blood_group'])
        db.session.add(user)
        db.session.commit()
        return 201


    def put(self,id):

        args=update_req_parser.parse_args()
        data={}                             #Empty dictionary for stiring filtered input arguments
        for key in args.keys():
            if args[key] != None:           # filtering the incomming arguments by clearing keys with NONe value.
              data[key]=args[key]
        result=UserModel.query.filter_by(id=id).first()
        if not result:
            return {"Error": "Invalid Identifier"}
        result=UserModel.query.filter_by(id=id).update(data)        #GEt the single record and update it with keys in data dictionary
        db.session.commit()             #here no add required because the record alredy stored

        return 201



    def delete(self,id):
        try:
            record=UserModel.query.filter_by(id=id).first()
            db.session.delete(record)               #deleting the record
            db.session.commit()
            return 200
        except(Exception):
            return {"Error":"Invalid identifier"}


class UserList(Resource): # for Listing all users
    @marshal_with(resources_fields)
    def get(self):
        result=UserModel.query.filter_by().all()
        return result



api.add_resource(UserList,'/donors/','/donors')
api.add_resource(Users,'/donors/<string:id>')


if __name__ == '__main__':
    app.run(debug=True)
