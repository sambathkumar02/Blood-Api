from flask_restful import reqparse


def PostRequestParser():
    post_req_parser = reqparse.RequestParser()
    post_req_parser.add_argument('name', type=str, help="invalid name",required=True)
    post_req_parser.add_argument('email', type=str, help="invalid mail",required=True)
    post_req_parser.add_argument('blood_group', type=str, help="invalid group",required=True)
    return post_req_parser

def UpdateRequestParser():
    update_req_parser = reqparse.RequestParser()
    update_req_parser.add_argument('name', type=str, help="invalid name")
    update_req_parser.add_argument('email', type=str, help="invalid mail")
    update_req_parser.add_argument('blood_group', type=str, help="invalid group")
    return update_req_parser

