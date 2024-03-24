import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { landingPageThunk } from '../../redux/business'
import { NavLink } from 'react-router-dom';
// import { useModal } from "../../context/Modal";
// import { landingPageThunk } from '../../redux/business'
// import { SignupFormModal } from '../SignupFormModal'
// import { LoginFormModal } from '../LoginFormModal'
// import { OpenModalButton } from '../OpenModalButton'
// import { ProfileButton } from '../Navigation'
import ImageCarousel from "../Carousel/Carousel";
import { BiSolidBadgeDollar } from "react-icons/bi";
import { formatDistanceToNow } from 'date-fns';
import { MdOutlineTakeoutDining, MdOutlineDinnerDining, MdGroups, MdBrunchDining, MdOutlineIcecream } from "react-icons/md";
import { IoWineSharp } from "react-icons/io5";
import { FaMoon } from "react-icons/fa";
import { IoIosMore } from "react-icons/io";

import './LandingPage.css'

export default function LandingPage() {

    const dispatch = useDispatch()
    const data = useSelector((state) => state.business)
    const reviewsArray = data.Review

    console.log('data=>',data.Business)

    useEffect(() => {
        dispatch(landingPageThunk())
    }, [dispatch])

    if (!data || !data.Review || !data.Business || !data.Users) {
        return <div>Loading...</div>
    }

    console.log('RV ARRAY', reviewsArray)

    // 6 reviews on landing
    const sixreviews = []
    for (let i = 0; i < 6; i++) {
        sixreviews.push(reviewsArray[i])
    }


    // Helper func: Business avg star rating by id
    function businessAvgRating(businessId) {
        let avgRating = 0
        let numRev = 0
        for (let review of reviewsArray) {
            if (review.business_id == businessId) {
                numRev++
                avgRating += review.star
            }
        }
        return avgRating / numRev
    }
    function numReview(businessId) {
        let numRev = 0
        for (let review of reviewsArray) {
            if (review.business_id == businessId) {
                numRev++
            }
        }
        return numRev
    }
    //render stars
    function renderStars(starValue) {
        const stars = [];
        for (let i = 1; i <= 5; i++) {
            if (i <= starValue) {
                stars.push(<span key={i} className="star-filled">★</span>);
            } else {
                stars.push(<span key={i} className="star-empty">☆</span>);
            }
        }
        return stars
    }
    //formatdates
    // function formatDate(date) {
    //     const newDate = new Date(date)
    //     const options = { month: 'long', day: 'numeric', year: 'numeric' }
    //     return newDate.toLocaleDateString(undefined, options)
    // }

    //X minutes ago (package)
    function formatTimeAgo(date) {
        const time = new Date(date);
        return formatDistanceToNow(time, { addSuffix: true });
    }

    //render $$$
    function renderPriceRating(priceRating) {
        switch (priceRating) {
            case 1:
                return <BiSolidBadgeDollar />;
            case 2:
                return (
                    <>
                        <BiSolidBadgeDollar />
                        <BiSolidBadgeDollar />
                    </>
                );
            case 3:
                return (
                    <>
                        <BiSolidBadgeDollar />
                        <BiSolidBadgeDollar />
                        <BiSolidBadgeDollar />
                    </>
                );
            case 4:
                return (
                    <>
                        <BiSolidBadgeDollar />
                        <BiSolidBadgeDollar />
                        <BiSolidBadgeDollar />
                        <BiSolidBadgeDollar />
                    </>
                );
            default:
                return null;
        }
    }
    return (
        <>
            <div style={{ marginBottom: '500px' }}>
                <div className='carousel-container'>
                    <ImageCarousel />
                </div>
            </div>

            <div className='all-business-container'>


            </div>

            <div className='recent-activity-container'>
                <h2 className='recent-actity-text'>Recent Activity</h2>
                <div className='recent-reviews'>
                    {sixreviews.map(review => (
                        <NavLink to={`/business/${data?.Business[review?.business_id]?.id}`} className='landing-business-review-container' key={review.id}>
                            <div className='review-user'>
                                <p>{data.Users[review.user_id].first_name} wrote a review</p>
                                <p className='timeago'>{ formatTimeAgo(review.createdAt)}</p>
                            </div>
                            <hr className='landing-hr'></hr>
                            <div className='landing-business-container'>
                                <p className='landing-business-name'>{data?.Business[review?.business_id]?.title}</p>
                                <div className='landing-business-rating'>
                                    {renderStars(businessAvgRating(data?.Business[review?.business_id]?.id))}
                                    <span> {numReview(data?.Business[review?.business_id]?.id)}</span>
                                </div>
                                <p className='landing-business-price-rating'>
                                    {renderPriceRating(data?.Business[review?.business_id]?.price_rating)} <span className='price-rating-dot'>&middot;</span> <span>{data?.Business[review?.business_id]?.category.split('"')}</span>
                                </p>
                                <img src='data?.Business[review?.business_id]?.url' alt='' />
                            </div>
                            <p className='review-description'>{review.review}</p>
                            <p className='review-image'>{review.image}</p>
                        </NavLink>
                    ))}
                </div>
                <hr className='hr'></hr>
                <div className='landing-categories'>
                    <h2 className='landing-categories-text'>Categories</h2>
                    <div className='landing-category-container'>
                        <NavLink to='/' className='landing-category' onClick={() => alert('Feature coming soon')}><MdOutlineDinnerDining/><p>Dinner</p></NavLink>
                        <NavLink to='/' className='landing-category' onClick={() => alert('Feature coming soon')}><MdOutlineTakeoutDining /><p>Take Out</p></NavLink>
                        <NavLink to='/' className='landing-category' onClick={() => alert('Feature coming soon')}><MdGroups /><p>Good For Groups</p></NavLink>
                        <NavLink to='/' className='landing-category' onClick={() => alert('Feature coming soon')}><MdBrunchDining/><p>Brunch</p></NavLink>
                        <NavLink to='/' className='landing-category' onClick={() => alert('Feature coming soon')}><MdOutlineIcecream/><p>Dessert</p></NavLink>
                        <NavLink to='/' className='landing-category' onClick={() => alert('Feature coming soon')}><FaMoon /><p>Open Late</p></NavLink>
                        <NavLink to='/' className='landing-category' onClick={() => alert('Feature coming soon')}><IoWineSharp /><p>Fine Dining</p></NavLink>
                        <NavLink to='/' className='landing-category' onClick={() => alert('Feature coming soon')}><IoIosMore /><p>More</p></NavLink>
                    </div>
                </div>
            </div>
        </>

    )
}
