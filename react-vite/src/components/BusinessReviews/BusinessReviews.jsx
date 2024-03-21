import { useParams } from 'react-router-dom'
import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { businessReviewThunk } from '../../redux/reviews'
// import './BusinessReview.css'

function BusinessReviews() {
    const { businessId } = useParams()
    const dispatch = useDispatch()
    const reviews = useSelector((state) => state.reviews.Review)
    const reviewImages = useSelector((state) => state.reviews.ReviewImage)
    const currUser = useSelector((state) => state.session.user)

    console.log('user ==>', currUser)
    console.log('reviews ==>', reviews)
    console.log('reviewImages ==>', reviewImages)

    // console.log('reviewCreate=>', reviews.createdAt)

    useEffect(() => {
        dispatch(businessReviewThunk(businessId))
    }, [dispatch, businessId])


    //to be used when query for user
    function renderName(user) {
        if (!user) return null;
        const { firstName, lastName } = user;
        const lastNameInitial = lastName ? lastName.charAt(0) : '';
        return `${firstName} ${lastNameInitial}.`;
    }


    function formatDate(date) {
        const newDate = new Date(date)
        const options = { month: 'long', day: 'numeric', year: 'numeric' }
        return newDate.toLocaleDateString(undefined, options)
    }

    function renderStars(starValue) {
        const stars = [];
        for (let i = 1; i <= starValue; i++) {
            stars.push(<span key={i} className="star-filled">★</span>);
        }
        return stars
    }

    return (
        <>
            {reviews ? (
                reviews.slice().reverse().map((review, index) => (
                    <div key={index}>
                        <h4 className='Review-Name'>Firstname L-initial </h4>
                        <p>{renderStars(review.star)}</p>
                        <p>{formatDate(review.createdAt)}</p>
                        <p>{review.review}</p>
                        <p>URL:{review.image}</p>
                    </div>
                ))
            ) : (
                <div className='NoReview'>Be the first to review</div>
            )}
        </>
    )
}

export default BusinessReviews
