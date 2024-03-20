import { useSelector, useDispatch } from "react-redux"
import  CreateNewReview  from "../CreateReview/CreateReview"
import { useParams } from "react-router-dom";
import { useEffect } from "react";
import { updateReviewThunk, businessReviewThunk } from "../../redux/reviews";

const UpdateReview = () => {

  const reviews = useSelector((state) => state.reviews)
  console.log('reviews ==>', reviews)
  const buttonName = 'Update a Review'
  const dispatch = useDispatch();
  const { reviewId, businessId } = useParams()

  if (!reviews || !reviews.Review || !reviews.ReviewImage) {
    return <h1>Loading...</h1>;
  }

  const review = state.Review.find(eachReview => eachReview.id == reviewId)

  console.log('review ==>', review)

  useEffect(() => {
    dispatch(businessReviewThunk(businessId))
  }, [businessId, dispatch])


  return (
    <>
      <h1>Update Review</h1>
      <CreateNewReview />
    </>
    )
}

export default UpdateReview
