import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { businessAmenitiesThunk, specificBusinessThunk } from '../../redux/business'
import { menuByBusinessThunk } from '../../redux/menu'
import { NavLink, useParams } from 'react-router-dom'
import { businessReviewThunk } from "../../redux/reviews";
import './BusinessDetails.css'
import { LuBean } from "react-icons/lu";
import { BiGame, BiSolidGame, BiSolidBadgeDollar } from "react-icons/bi";
import BusinessReviews from "../BusinessReviews/BusinessReviews";


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
  if (reviews.Review && business && businessId && menus) {
    avgStarRating = reviews.Review.reduce((acc, curr) => {
      if ('star' in curr && typeof curr.star == 'number') {
        return acc + curr.star
      } else {
        return acc
      }
    }, 0) / reviews.Review.length
    avgStarRating = avgStarRating.toFixed(1)
    const id = businessId
    selectedBusiness = business[id]

    if (selectedBusiness && menus.Business_Images) {
      priceRating = selectedBusiness.price_rating
      let businessCategoryStr = selectedBusiness.category
      businessCategory = businessCategoryStr.split(',')[0].split('"')[1]
      businessPreviewImg = menus.Business_Images.filter(img => img.business_id == businessId && img.preview == true)[0]
      businessSchedule = selectedBusiness.schedule
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
        <>
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
                  <></>
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

          <div className="menu-container">
            <h2>menu</h2>
            {/* show menu component => show menu price / link to the menu */}
          </div>

          <div className="reviews-container">
            <h2>reviews</h2>
            <BusinessReviews />
          </div>

          <div className="business-info-container schedule-text">
            <h2>business info</h2>
            {/* show amenities */}
          </div>
        </>
      ) : (
        <h2>Loading ...</h2>
      )}
    </>
  )
}
