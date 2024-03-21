import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { useEffect } from "react";
import { businessReviewThunk } from "../../redux/reviews";
import CreateNewReview from "../CreateReview/CreateReview";

const UpdateReview = () => {
    const dispatch = useDispatch();
    const { reviewId, businessId } = useParams();

    // Fetch reviews from Redux store
    const reviews = useSelector((state) => state.reviews);
    console.log('reviews ==>', reviews);

    const buttonName = 'Update a Review';

    // Find the review to update
    let reviewToUpdate;
    if (reviews && reviews.Review) {
        reviewToUpdate = reviews.Review.find(eachReview => eachReview.id == reviewId);
        console.log('reviewToUpdate ==>', reviewToUpdate);
    }

    // Fetch reviews for the specific business
    useEffect(() => {
        dispatch(businessReviewThunk(businessId));
    }, [businessId, dispatch]);

    if (!reviews || !reviews.Review) {
        return <h1>Loading...</h1>;
      }

    return (
        <>
            <h1>Update Review</h1>
            {/* Pass the review prop to CreateNewReview component */}
            <CreateNewReview reviewToUpdate={reviewToUpdate} buttonName={buttonName} />
        </>
    );
};

export default UpdateReview;
