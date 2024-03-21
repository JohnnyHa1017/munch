import {  useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { landingPageThunk } from '../../redux/business'
import { NavLink } from 'react-router-dom';
// import { useModal } from "../../context/Modal";
// import { landingPageThunk } from '../../redux/business'
// import { SignupFormModal } from '../SignupFormModal'
// import { LoginFormModal } from '../LoginFormModal'
// import { OpenModalButton } from '../OpenModalButton'
// import { ProfileButton } from '../Navigation'
import './LandingPage.css'

export default function LandingPage() {

    const dispatch = useDispatch()
    const data = useSelector((state) => state.business)

    const businessArray = data.Business
    const reviewsArray = data.Review
    // const amenitiesArray = data.Amen


    console.log('DATA ---->', data)

    useEffect(() => {
        dispatch(landingPageThunk())
    }, [dispatch])

    if(!data || !data.Review || !data.Business || !data.Users){
        return <div>Loading...</div>
    }

    const sixreviews = []
    for(let i=0; i < 6; i++){
        sixreviews.push(reviewsArray[i])
    }

    // Helper func: Business avg star rating by id
    function businessAvgRating(businessId){
        let avgRating = 0
        let numRev = 0
        for (let review of reviewsArray){
            if(review.business_id == businessId){
                numRev++
                avgRating += review.star
            }
        }
        return avgRating/numRev
    }
    function numReview(businessId){
        let numRev = 0
        for(let review of reviewsArray){
            if(review.business_id == businessId){
                numRev++
            }
        }
        return numRev
    }

    return (
        <>
            <h1>Landing Page!</h1>
            <div className='recent-activity-container'>
                <div>
                    <p>image carousel here</p>
                </div>
                <h2 className='recent-actity-text'>Recent Activity</h2>
                <div className='recent-reviews'>
                    {sixreviews.map(review => (
                        <div className='landing-business-review-container'>
                            <div className='review-user'>
                                <p>{data.Users[review.user_id].first_name} wrote a review</p>
                            </div>
                            <hr></hr>
                            <div className='landing-business-container'>
                                <p className='landing-business-name'>{data?.Business[review.business_id].title}</p>
                                <p className='landing-business-rating'>Business Rating: {businessAvgRating(data?.Business[review.business_id].id)}</p>
                                <p>Number of Reviews: {numReview(data?.Business[review.business_id].id)}</p>
                                <p className='landing-business-price-rating'>Business Price Rating: {data?.Business[review.business_id].price_rating}</p>
                                <img src=''></img>
                            </div>
                            <p>{review.review}</p>
                        </div>
                    ))}
                </div>
                <div className='landing-categories'>
                    <h2 className='landing-categories-text'>Categories</h2>
                    <div className='landing-category-container'>
                        <NavLink to='/' className='landing-category'>Dinner</NavLink>
                        <NavLink to='/' className='landing-category'>Take Out</NavLink>
                        <NavLink to='/' className='landing-category'>Good For Groups</NavLink>
                        <NavLink to='/' className='landing-category'>Brunch</NavLink>
                        <NavLink to='/' className='landing-category'>Dessert</NavLink>
                        <NavLink to='/' className='landing-category'>Open Late</NavLink>
                        <NavLink to='/' className='landing-category'>Fine Dining</NavLink>
                        <NavLink to='/' className='landing-category'>Casual Dining</NavLink>
                    </div>
                </div>
            </div>
        </>

    )
}
