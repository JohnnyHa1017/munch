import {  useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { businessAmenitiesThunk, businessMenuThunk, specificBusinessThunk } from '../../redux/business'
import { useParams } from 'react-router-dom'
import { businessReviewThunk } from "../../redux/reviews";

// TODO: Pass in reviews

export default function OneBusiness() {
  const dispatch = useDispatch()
  const data = useSelector((state) => state.business)
  const reviews = useSelector(state => state.reviews)
  const { businessId } = useParams()

  useEffect(() => {
    dispatch(specificBusinessThunk(businessId))
    dispatch(businessMenuThunk(businessId))
    dispatch(businessAmenitiesThunk(businessId))
    dispatch(businessReviewThunk(businessId))
  }, [businessId, dispatch])

  if (!data[businessId] || !reviews.Review) {
    return <div>Loading...</div>
  }

  const reviewArr = reviews.Review

  return (
    <>
      <h1>Business Id Page</h1>
      <p>{data[businessId].title}</p>
      <h2>Schedule</h2>
      <p>{data[businessId].schedule}</p>
      <h2>Reviews</h2>
      {reviewArr.map(review => (
        <p key={review.id}>{review.review}</p>
      ))}
    </>
  )
}
