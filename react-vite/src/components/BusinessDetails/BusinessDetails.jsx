import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { businessAmenitiesThunk, specificBusinessThunk } from '../../redux/business'
import { menuByBusinessThunk } from '../../redux/menu'
import { NavLink, useParams } from 'react-router-dom'
import { businessReviewThunk } from "../../redux/reviews";
import './BusinessDetails.css'
import { LuBean } from "react-icons/lu";
import { BiGame, BiSolidGame, BiSolidBadgeDollar } from "react-icons/bi";
import { IoCheckmarkCircle, IoCheckmarkCircleOutline } from "react-icons/io5";
import BusinessReviews from "../BusinessReviews/BusinessReviews";
import MenusByBusinessId from "../Menu/MenusByBusiness";


// TODO get current time and make Open/Closed dynamic


export default function OneBusiness() {
  const dispatch = useDispatch()
  const business = useSelector(state => state.business)
  const reviews = useSelector(state => state.reviews)
  const menus = useSelector(state => state.menus)
  const { businessId } = useParams()


  //get average start rating
  let avgStarRating = 1
  let priceRating = 1
  let businessPreviewImg = {}
  let businessCategory = ""
  let businessSchedule = ""
  let selectedBusiness = {}
  let amenities = {}
  let isAccepts_cc = false
  let isDelivery = false
  let isFreeWF = false
  let isGoodGroup = false
  let isOutdoor = false
  let isPickup = false
  let isReservation = false
  let isSP = false
  let isVegetarian = false

  if (reviews.Review && business.Amenities && businessId && menus) {
    //get average rating
    avgStarRating = reviews.Review.reduce((acc, curr) => {
      if ('star' in curr && typeof curr.star == 'number') {
        return acc + curr.star
      } else {
        return acc
      }
    }, 0) / reviews.Review.length
    avgStarRating = avgStarRating.toFixed(1)
    //get selected business
    const id = businessId
    selectedBusiness = business[id]
    //select menu images
    if (selectedBusiness && menus.Business_Images) {
      priceRating = selectedBusiness.price_rating
      let businessCategoryStr = selectedBusiness.category
      businessCategory = businessCategoryStr.split(',')[0].split('"')[1]
      businessPreviewImg = menus.Business_Images.filter(img => img.business_id == businessId && img.preview == true)[0]
      businessSchedule = selectedBusiness.schedule
    }
    //get amenity object
    const allAmenities = business.Amenities
    for (let eachAm of allAmenities) {
      if (eachAm.business_id == businessId) {
        amenities = eachAm
      }
    }

    for (const key in amenities) {
      if (amenities.hasOwnProperty(key)) {
        switch (key) {
          case 'accepts_credit_card': //to get each key
            isAccepts_cc = amenities[key] //assign boolean values
            break
          case 'delivery':
            isDelivery = amenities[key]
            break
          case 'free_wi_fi':
            isFreeWF = amenities[key]
            break
          case 'good_for_groups':
            isGoodGroup = amenities[key]
            break
          case 'outdoor_seating':
            isOutdoor = amenities[key]
            break
          case 'pickup':
            isPickup = amenities[key]
            break
          case 'reservation':
            isReservation = amenities[key]
            break
          case 'street_parking':
            isSP = amenities[key]
            break
          case 'vegetarian':
            isVegetarian = amenities[key]
            break
          default:
            break
        }
      }
    }
  }

  useEffect(() => {
    dispatch(specificBusinessThunk(businessId))
    dispatch(menuByBusinessThunk(businessId))
    dispatch(businessAmenitiesThunk(businessId))
    dispatch(businessReviewThunk(businessId))
  }, [businessId, dispatch, businessSchedule])


  return (
    <>
      {business ? (
        <div className="business-detail-page-container">
          <div className="business-detail-header-container">
            <div className="business-detail-header-img" style={{ backgroundImage: `url(${businessPreviewImg.url})`, height: '360px' }}>
              <h1 className="business-detail-header-text">{selectedBusiness?.title}</h1>
              <div className="bd-star-rating-container">
                {reviews.Review && avgStarRating > 0 ? (
                  <>
                    {[...Array(Math.floor(avgStarRating))].map((_, index) => (
                      <BiSolidGame key={index} className="bd-star" />
                    ))}
                    {avgStarRating % 1 !== 0 && <BiGame className="bd-star" />}
                    {[...Array(5 - Math.ceil(avgStarRating))].map((_, index) => (
                      <LuBean key={index} className="bd-star" />
                    ))}
                    <h3 className="business-detail-header-text">
                      {avgStarRating} ({reviews.Review.length} reviews)
                    </h3>
                    <div>
                      {[...Array(priceRating)].map((_, index) => (
                        <BiSolidBadgeDollar key={index} className="bd-dollar-sign" />
                      ))}
                    </div>
                  </>) : (
                  <>No reviews yet</>
                )}
              </div>
              <p className="business-detail-header-text">
                {businessCategory}
              </p>
              <p className="business-detail-header-text schedule-text">
                {businessSchedule}
              </p>
            </div>
          </div>
          <div className="business-detail-action-buttons-container">
            {/* add current user check for existing review */}
            <button><NavLink to={`/business/${businessId}/review/new`}>Write a review</NavLink></button>
            <button onClick={() => alert('Feature coming soon')}>Add a photo</button>
            <button onClick={() => alert('Feature coming soon')}>Share</button>
            <button onClick={() => alert('Feature coming soon')}>Save</button>
            <button onClick={() => alert('Feature coming soon')}>Follow</button>
          </div>

          <div className="business-detail-context-container">
            <div className="business-contexts">
              <div className="menu-container">
                <MenusByBusinessId />
              </div>
              <div className="business-info-container">
                <h2>Schedule</h2>
                {businessSchedule}
                <h2>Amenities</h2>
                <div className="business-detail-amenity-container">
                  <div className="amenity-blocks">
                    <p>Accepts Credit Card</p>
                    {isAccepts_cc ? (<IoCheckmarkCircle className="amenity-tags" />) : (<IoCheckmarkCircleOutline className="amenity-tags" />)}
                  </div>
                  <div className="amenity-blocks">
                    <p>Delivery</p>
                    {isDelivery ? (<IoCheckmarkCircle className="amenity-tags" />) : (<IoCheckmarkCircleOutline className="amenity-tags" />)}
                  </div>
                  <div className="amenity-blocks">
                    <p>Pickup</p>
                    {isPickup ? (<IoCheckmarkCircle className="amenity-tags" />) : (<IoCheckmarkCircleOutline className="amenity-tags" />)}
                  </div>
                  <div className="amenity-blocks">
                    <p>Reservation</p>
                    {isReservation ? (<IoCheckmarkCircle className="amenity-tags" />) : (<IoCheckmarkCircleOutline className="amenity-tags" />)}
                  </div>
                  <div className="amenity-blocks">
                    <p>Street Parking</p>
                    {isSP ? (<IoCheckmarkCircle className="amenity-tags" />) : (<IoCheckmarkCircleOutline className="amenity-tags" />)}
                  </div>
                  <div className="amenity-blocks">
                    <p>Free Wi-Fi</p>
                    {isFreeWF ? (<IoCheckmarkCircle className="amenity-tags" />) : (<IoCheckmarkCircleOutline className="amenity-tags" />)}
                  </div>
                  <div className="amenity-blocks">
                    <p>Good for Groups</p>
                    {isGoodGroup ? (<IoCheckmarkCircle className="amenity-tags" />) : (<IoCheckmarkCircleOutline className="amenity-tags" />)}
                  </div>
                  <div className="amenity-blocks">
                    <p>Out Door Seating</p>
                    {isOutdoor ? (<IoCheckmarkCircle className="amenity-tags" />) : (<IoCheckmarkCircleOutline className="amenity-tags" />)}
                  </div>
                  <div className="amenity-blocks">
                    <p>Vegetarian</p>
                    {isVegetarian ? (<IoCheckmarkCircle className="amenity-tags" />) : (<IoCheckmarkCircleOutline className="amenity-tags" />)}
                  </div>
                </div>
              </div>
              <div className="reviews-container">
                <h1>Reviews for {selectedBusiness?.title}</h1>
                <BusinessReviews />
              </div>
            </div>
            <div className="business-dtl-info">
              HI
            </div>
          </div>



        </div>
      ) : (
        <h2>Loading ...</h2>
      )}
    </>
  )
}
