from flask_restful import Resource
from flask import request
from Model import db, recommend_, recommend_schema


rr=[]
recommendations_schema = recommend_schema(many=True)
recommendation_schema = recommend_schema()

class recommend(Resource):
    def get(self):
        return {'Hey':'User'}
    def post(self):
        rr=[]
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        #data, errors = recommendation_schema.load(json_data)
        #if errors:
        #    return errors, 422
        i=json_data['interest']
        recommendations = recommend_.query.all()
        for r in recommendations:
            if r.interest==i:
                rr.append(r.goal)
        return {'status': 'success', 'recommendations': rr}, 201

    '''

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = category_schema.load(json_data)
        if errors:
            return errors, 422
        category = Category.query.filter_by(name=data['name']).first()
        if category:
            return {'message': 'Category already exists'}, 400
        category = Category(
            name=json_data['name']
            )

        db.session.add(category)
        db.session.commit()

        result = category_schema.dump(category).data

        return { "status": 'success', 'data': result }, 201
'''
