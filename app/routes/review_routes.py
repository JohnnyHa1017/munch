from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Review, db
from app.forms.review_form import CreateReview
from .aws_helpers import upload_file_to_s3, remove_file_from_s3

bp = Blueprint('review_routes', __name__, url_prefix='api/reviews')

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


# UPDATE REVIEW BY REVIEW ID /:reviewId/update
    # TODO: MADE A REVISION HERE, NEED TO CHECK AND TEST

@bp.route('/<int:id>/update', methods=['PUT'])
@login_required
def update_review(id):
    review = Review.query.get(id)

    if not review:
        return jsonify({'error': 'Review not found'}), 404

    if review.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403

    form = CreateReview()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        new_image_url = None
        if 'image' in request.files:
            new_image_url = upload_image_url(request.files['image'])

            if new_image_url and review.image_url:
                remove_image(review.image_url)

        form.populate_obj(review)

        if new_image_url:
            review.image_url = new_image_url

        db.session.commit()

        return jsonify({'message': 'Review updated successfully'})
    return jsonify({'error': form.errors}), 400


# DELETE REVIEW BY REVIEW ID /:reviewId/delete
    # TODO: MADE A REVISION HERE, NEED TO CHECK AND TEST

@bp.route('/<int:id>/delete', methods=['DELETE'])
@login_required
def delete_review(id):
    review = Review.query.get(id)

    if not review:
        return jsonify({'error': 'Review not found'}), 404

    if review.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403

    if review.image_url:
        remove_image(review.image_url)

    db.session.delete(review)
    db.session.commit()

    return jsonify({'message': 'Successfully Deleted'}), 200
