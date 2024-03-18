from flask import Blueprint, jsonify, request, redirect
from app.models import Business, Menu, Amenity, Review, ReviewImage, db
from app.forms.business_form import CreateBusiness
from app.forms.menu_form import NewMenu
from app.forms.amenities_form import CreateAmenities
from app.forms.business_form import CreateBusiness
from app.forms.review_form import CreateReview
from flask_login import login_required, current_user
import json

bp = Blueprint('business_routes', __name__, url_prefix='/business')

#helper function to get all businesses
def get_all_business():
    all_businesses = Business.query.all()
    business_list = [business.to_dict() for business in all_businesses]
    return business_list


# GET all businesses
@bp.route('/businesses')
def all_business():
    data = get_all_business()
    return data


# GET business /:businessId
@bp.route('/<int:id>')
def one_business(id):
    business = Business.query.get(id)
    if not business:
        return jsonify({'error': 'Business not found'}), 404
    else:
        business_dict = business.to_dict()
        return business_dict

# GET users business /

# POST business
@bp.route('/new', methods=['GET', 'POST'])
@login_required
def create_business():
    form = CreateBusiness()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        params = { "owner_id": current_user.id}
        data = Business(**params)
        form.populate_obj(data)
        db.session.add(data)
        db.session.commit()
        return data.to_dict()
    return jsonify({'error': form.errors}), 400


# PUT business
@bp.route('/<int:id>/edit', methods=['PUT'])
@login_required
def update_business(id):
    business = Business.query.get(id)
    if not business:
        return jsonify({'error': 'Business not found'}), 404
    if business.owner_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403
    form = CreateBusiness()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        form.populate_obj(business)
        db.session.commit()
        return jsonify({'message': 'Business updated successfully'})
    return jsonify({'error': form.errors}), 400


# DELETE business /:businessId/delete
@bp.route('/<int:id>/delete', methods=['DELETE'])
@login_required
def delete_business(id):
    business = Business.query.get(id)
    if not business:
        return jsonify({'error': 'Business not found'}), 404
    if business.owner_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403
    db.session.delete(business)
    db.session.commit()
    return jsonify({'message': 'Successfully Deleted'}), 200


# GET review /:businessId/review
@bp.route('/<int:id>/review')
def business_review(id):
    all_reviews = Review.query.filter_by(business_id=id).all()
    review_img = ReviewImage.query.filter_by(review_id=id).all()
    review_list = [review.to_dict() for review in all_reviews]
    review_img_list = [image.to_dict() for image in review_img]
    data = {"Review": review_list, "ReviewImage": review_img_list}
    return data

# GET users review /:businessId/

# POST review /:businessId/review/new
@bp.route('<int:id>/review/new', methods=['GET', 'POST'])
@login_required
def create_review(id):
    form = CreateReview()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        params = { "business_id": id, "user_id": current_user.id}
        data = Review(**params)
        form.populate_obj(data)
        db.session.add(data)
        db.session.commit()
        return data.to_dict()
    return jsonify({'error': form.errors}), 400

# GET amenities /:businessId/amenity
@bp.route('/<int:id>/amenity', methods=['GET'])
def business_amenities(id):
    amenities = Amenity.query.filter(Amenity.business_id == id)
    amenities_lst = [amenity.to_dict() for amenity in amenities]
    if not amenities:
        return jsonify({'error': 'Amenities not found'}), 404
    else:
        return amenities_lst[0]

# POST amenity /:businessId/amenity/new
@bp.route('/<int:id>/amenity/new', methods=['GET','POST'])
def create_amenities(id):
    form = CreateAmenities()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        params = {'business_id':id}
        data = Amenity(**params)
        form.populate_obj(data)
        db.session.add(data)
        db.session.commit()
        return data.to_dict()
    return jsonify({'error': form.errors}), 400

# GET menu /:businessId/menu
@bp.route('/<int:id>/menu', methods=['GET'])
def business_menu(id):
    menu = Menu.query.filter(Menu.business_id == id).all()
    menu_lst = [item.to_dict() for item in menu]
    if not menu:
        return jsonify({'error': 'Menu not found'}), 404
    else:
        return menu_lst

# POST menu /:businessId/menu/new
@bp.route('/<int:id>/menu/new', methods=['GET', 'POST'])
@login_required
def create_menu(id):
    form = NewMenu()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        params = {'business_id':id}
        data = Menu(**params)
        form.populate_obj(data)
        db.session.add(data)
        db.session.commit()
        return data.to_dict()
    return jsonify({'error': form.errors}), 400
