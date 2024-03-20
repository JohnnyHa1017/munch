from flask import Blueprint, jsonify, request, redirect
from app.models import Business, Menu, Amenity, Review, ReviewImage, db
from app.forms.business_form import CreateBusiness
from app.forms.menu_form import NewMenu, MenuImageForm
from app.forms.amenities_form import CreateAmenities
from app.forms.business_form import CreateBusiness, ScheduleForm, BusinessImageForm
from app.forms.review_form import CreateReview
from flask_login import login_required, current_user
from .aws_helpers import upload_file_to_s3, remove_file_from_s3
import json

bp = Blueprint('business_routes', __name__, url_prefix='/api/business')

#helper function to get all businesses
def get_all_business():
    all_businesses = Business.query.all()
    business_list = [business.to_dict() for business in all_businesses]
    return business_list


# Helper function to upload image and get its URL
def upload_image_url(image):
    if not image:
        return None
    upload_result = upload_file_to_s3(image)
    if "url" in upload_result:
        return upload_result["url"]
    return None


# Helper function to remove image from AWS S3
def remove_image(image_url):
    if not image_url:
        return
    remove_file_from_s3(image_url)


# GET all businesses
    # TODO: MADE A REVISION HERE, NEED TO CHECK AND TEST

@bp.route('/businesses')
def all_business():
    all_businesses = Business.query.all()
    business_list = [business.to_dict() for business in all_businesses]
    return jsonify(business_list)


# GET business /:businessId
@bp.route('/<int:id>')
def one_business(id):
    business = Business.query.get(id)

    if not business:
        return jsonify({'error': 'Business not found'}), 404
    else:
        business_dict = business.to_dict()
        return business_dict


# POST business
    # TODO: MADE A REVISION HERE, NEED TO CHECK AND TEST

@bp.route('/new', methods=['GET', 'POST'])
@login_required
def create_business():
    form = CreateBusiness()
    schedule_form = ScheduleForm()
    image_form = BusinessImageForm()

    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        schedule = f'''Monday:{schedule_form.data['monday_open']} - {schedule_form.data['monday_close']}, Tuesday: {schedule_form.data['tuesday_open']} - {schedule_form.data['tuesday_close']}, Wednesday: {schedule_form.data['wednesday_open']} - {schedule_form.data['wednesday_close']}, Thursday: {schedule_form.data['thursday_open']} - {schedule_form.data['thursday_close']}, Friday: {schedule_form.data['friday_open']} - {schedule_form.data['friday_close']}, Saturday: {schedule_form.data['saturday_open']} - {schedule_form.data['saturday_close']}, Sunday: {schedule_form.data['sunday_open']} - {schedule_form.data['sunday_close']}'''

        if image_form.image.data:
            image_url = upload_image_url(image_form.image.data)
            if not image_url:
                return jsonify({'error': 'Failed to upload image'}), 500

        business = Business(owner_id=current_user.id, schedule=schedule, image=image_url if image_form.image.data else 'None')

        form.populate_obj(business)
        db.session.add(business)
        db.session.commit()

        return jsonify(business.to_dict()), 201
    return jsonify({'error': form.errors}), 400


# PUT business
    # TODO: MADE A REVISION HERE, NEED TO CHECK AND TEST

@bp.route('/<int:id>/edit', methods=['PUT'])
@login_required
def update_business(id):
    business = Business.query.get(id)

    if not business:
        return jsonify({'error': 'Business not found'}), 404

    if business.owner_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403

    form = CreateBusiness()
    image_form = BusinessImageForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        if image_form.validate_on_submit():
            if image_form.image.data:
                if business.image:
                    remove_image(business.image)
                business.image = upload_image_url(image_form.image.data)

        form.populate_obj(business)
        db.session.commit()

        return jsonify({'message': 'Business updated successfully'})
    return jsonify({'error': form.errors}), 400


# DELETE business /:businessId/delete
    # TODO: MADE A REVISION HERE, NEED TO CHECK AND TEST

@bp.route('/<int:id>/delete', methods=['DELETE'])
@login_required
def delete_business(id):
    business = Business.query.get(id)

    if not business:
        return jsonify({'error': 'Business not found'}), 404

    if business.owner_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403

    remove_image(business.image)

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


# POST review /:businessId/review/new
    # TODO: MADE A REVISION HERE, NEED TO CHECK AND TEST

@bp.route('<int:id>/review/new', methods=['GET', 'POST'])
@login_required
def create_review(id):
    form = CreateReview()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        if form.image.data:
            image_url = upload_image_url(form.image.data)
        else:
            image_url = None

        params = {'business_id': id, 'user_id': current_user.id, 'image': image_url}
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
    # TODO: MADE A REVISION HERE, NEED TO CHECK AND TEST

@bp.route('/<int:id>/menu/new', methods=['GET', 'POST'])
@login_required
def create_menu(id):
    form = NewMenu()
    image_form = MenuImageForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        if image_form.image.data:
            image_url = upload_image_url(image_form.image.data)
        else:
            image_url = None

        params = {'business_id': id, 'image': image_url}
        data = Menu(**params)
        form.populate_obj(data)
        db.session.add(data)
        db.session.commit()

        return data.to_dict()
    return jsonify({'error': form.errors}), 400
