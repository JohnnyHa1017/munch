from flask import Blueprint, jsonify, request
from app.models import Business, db
from app.forms.business_form import CreateBusiness
from flask_login import login_required, current_user
import json

bp = Blueprint('business_routes', __name__, url_prefix='/business')

#helper function to get all businesses
def get_all_business():
    all_businesses = Business.query.all()
    business_list = [business.to_dict() for business in all_businesses]
    return business_list


#all businesses
@bp.route('/businesses')
def all_business():
    data = get_all_business()
    return data


#get business by id
@bp.route('/<int:id>')
def one_business(id):
    business = Business.query.get(id).to_dict()
    return business


#create business
@bp.route('/new', methods=['GET', 'POST'])
@login_required
def create_business():
    form = CreateBusiness()
    form['csrf_token'].data = request.cookies['csrf_token']
    print('current_user ==>', current_user)
    if form.validate_on_submit():
        params = { "owner_id": current_user.id}
        data = Business(**params)
        form.populate_obj(data)
        db.session.add(data)
        db.session.commit()
        return data.to_dict()
    return form.errors


