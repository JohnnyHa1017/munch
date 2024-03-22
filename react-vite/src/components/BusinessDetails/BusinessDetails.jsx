import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { businessAmenitiesThunk, specificBusinessThunk } from '../../redux/business'
import { menuByBusinessThunk } from '../../redux/menu'
import { useParams } from 'react-router-dom'
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

  console.log('business ==>', business)
  console.log('reviews.Review ==>', reviews.Review)
  console.log('menus ==>', menus)

  //get average start rating
  let avgStarRating = 1
  let priceRating = 1
  let business_preview_img = {}
  let business_category = ""
  let business_schedule = ""
  if (reviews.Review && business.Business && menus) {
    avgStarRating = reviews.Review.reduce((acc, curr) => {
      if ('star' in curr && typeof curr.star == 'number') {
        return acc + curr.star
      } else {
        return acc
      }
    }, 0) / reviews.Review.length
    priceRating = business.Business.price_rating
    business_preview_img = business.Business_Images.filter(img => img.business_id == businessId && img.preview == true)[0]
    let business_categoryStr = business.Business.category
    if (business_categoryStr) {
      business_category = business_categoryStr.split(',')[0].split('"')[1]
    }
    business_schedule = business.Business.schedule
  }

  useEffect(() => {
    dispatch(specificBusinessThunk(businessId))
    dispatch(menuByBusinessThunk(businessId))
    dispatch(businessAmenitiesThunk(businessId))
    dispatch(businessReviewThunk(businessId))
  }, [businessId, dispatch, business_schedule])


  return (
    <>
      {business.Business && reviews.Review && menus.Menu && Object.keys(business_preview_img).length > 0 ? (
        <>
          <div className="business-detail-header-container">
            <div className="business-detail-header-img" style={{ backgroundImage: `url(${business_preview_img.url})`, height: '360px' }}>
              <h1 className="business-detail-header-text">{business.Business.title}</h1>
              <div className="bd-star-rating-container">
                {[...Array(Math.floor(avgStarRating))].map((_, index) => (
                  <BiSolidGame key={index} className="bd-star" />
                ))}
                {avgStarRating % 1 !== 0 && <LuBean className="bd-star" />}
                {[...Array(5 - Math.ceil(avgStarRating))].map((_, index) => (
                  <BiGame key={index} className="bd-star" />
                ))}
                <h3 className="business-detail-header-text">
                  {avgStarRating} ({reviews.Review.length} reviews)
                </h3>
              </div>
              <div>
                {[...Array(priceRating)].map((_, index) => (
                  <BiSolidBadgeDollar key={index} className="bd-dollar-sign" />
                ))}
              </div>
              <p className="business-detail-header-text">
                {business_category}
              </p>
              <p className="business-detail-header-text schedule-text">
                {business_schedule}
              </p>
            </div>
          </div>

          <div className="business-detail-action-buttons-container">
            <button>Write a review</button>
            <button>Add a photo</button>
            <button>Share</button>
            <button>Save</button>
            <button>Follow</button>
          </div>

          <div className="menu-container">
            <h2>menu</h2>
          </div>

          <div className="reviews-container">
            <h2>reviews</h2>
            <BusinessReviews />
          </div>

          <div className="business-info-container schedule-text">
            <h2>business info</h2>
          </div>

        </>
      ) : (
        <h2>Loading ...</h2>
      )}
    </>
  )
}
