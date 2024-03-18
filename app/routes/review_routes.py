from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Review, db
from app.forms.review_form import CreateReview


bp = Blueprint('review_routes', __name__)


# UPDATE REVIEW BY REVIEW ID /:reviewId/update
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
        form.populate_obj(review)
        db.session.commit()
        return jsonify({'message': 'Review updated successfully'})
    return jsonify({'error': form.errors}), 400


# DELETE REVIEW BY REVIEW ID /:reviewId/delete
@bp.route('/<int:id>/delete', methods=['DELETE'])
@login_required
def delete_business(id):
    review = Review.query.get(id)
    if not review:
        return jsonify({'error': 'Review not found'}), 404
    if review.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403
    db.session.delete(review)
    db.session.commit()
    return jsonify({'message': 'Successfully Deleted'}), 200
