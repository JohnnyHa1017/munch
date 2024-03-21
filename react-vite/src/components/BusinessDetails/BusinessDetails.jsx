import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { businessAmenitiesThunk, specificBusinessThunk } from '../../redux/business'
import { menuByBusinessThunk } from '../../redux/menu'
import { useParams } from 'react-router-dom'
import { businessReviewThunk } from "../../redux/reviews";
import './BusinessDetails.css'

// TODO: Pass in reviews

export default function OneBusiness() {
  const dispatch = useDispatch()
  const business = useSelector(state => state.business)
  const reviews = useSelector(state => state.reviews)
  const menus = useSelector(state => state.menus)
  const { businessId } = useParams()

  console.log('business ==>', business)
  console.log('reviews ==>', reviews)
  console.log('menus ==>', menus)

  let business_preview_img = {}
  if (business.Business_Images && reviews && menus) {
    business_preview_img = business.Business_Images.filter(img => img.business_id == businessId && img.preview == true)[0]
    console.log('business_preview_img ==>', business_preview_img)
  }

  useEffect(() => {
    dispatch(specificBusinessThunk(businessId))
    dispatch(menuByBusinessThunk(businessId))
    dispatch(businessAmenitiesThunk(businessId))
    dispatch(businessReviewThunk(businessId))
  }, [businessId, dispatch])


  return (
    <>
      {business && reviews && menus && Object.keys(business_preview_img).length > 0 ? (
        <div>
          <h1>Business Detail Page</h1>
          <div className="business-detail-header-img">
              <p className="business-detail-header-text">Business Details</p>
              <p className="business-detail-header-text">hello!</p>
          </div>

        </div>
      ) : (
        <h2>Loading ...</h2>
      )}
    </>
  )
}
