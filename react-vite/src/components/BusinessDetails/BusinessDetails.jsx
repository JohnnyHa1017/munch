import {  useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { businessAmenitiesThunk, businessMenuThunk, specificBusinessThunk } from '../../redux/business'
import { useParams } from 'react-router-dom'
import { businessReviewThunk } from "../../redux/reviews";

// TODO: Pass in reviews
  // *: COMPLETED THANK YOU @MoonChopperr

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

  const businessImages = data.Business_Images.filter((img) => img.business_id == businessId);
  const reviewArr = reviews.Review

  return (
    <>
      <h1 id='business-name'>{data[businessId].title}</h1>
      <p>Address: <br></br>
        {data[businessId].address}</p>
      <p>City: <br></br>
        {data[businessId].city}</p>
      <p>State: <br></br>
        {data[businessId].state}</p>
      <p> Categories: <br></br>
      {JSON.parse(data[businessId].category).join(', ')}
      </p>
      <p>Phone Number: <br></br>
        {data[businessId].phone_number}</p>
      <p>Price Rating: <br></br>
        {data[businessId].price_rating}</p>
      <p>Description: <br></br>
        {data[businessId].description}</p>
      <h2>Check out some photos of {data[businessId].title}</h2>

      {
        // TODO: WHOEVER HAS THE TIME TO DEBUG THIS
        // TODO: THATD BE MUCH APPRECIATED
        // TODO: PROBABLY EASIER TO DEFINE A COMPONENT FOR THIS LIKE @MoonChopperr
        // TODO: DID WITH HIS REVIEW WHERE IT'LL NEST THE BUSINESS IMAGES ELSEWHERE
        // TODO: THEN THIS IS JUST A RENDERING OF IMAGES RATHER
      }

        {businessImages.length > 0 ? (
        <div>
          {businessImages.map(image => (
          <img key={image.id} src={image.url} alt={`Image ${image.id}`} />
          ))}
        </div>) : (<p>No photos available</p>)}

      <h2>Schedule</h2>
      <p>{data[businessId].schedule}</p>
      <h2>Amenities</h2>
      <h2>Reviews</h2>
      {reviewArr.map(review => (
        <p key={review.id}>{review.review}</p>
      ))}
    </>
  )
}
