import { useParams } from 'react-router-dom'
import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { businessReviewThunk } from '../../redux/reviews'
// import './BusinessReview.css'

function BusinessReviews(){
    const { businessId } = useParams()
    const dispatch = useDispatch()
    const reviews = useSelector((state)=> state.reviews.Review)
    const reviewImages = useSelector((state)=> state.reviews.ReviewImage)
    const currUser = useSelector((state)=> state.session.user)

    console.log('user ==>', currUser)
    console.log('reviews ==>', reviews)
    console.log('reviewImages ==>', reviewImages)



    useEffect(()=>{
        dispatch(businessReviewThunk(businessId))
    }, [dispatch, businessId])

    if(!reviews){
        return <div className='NoReview'>Be the first to review</div>
    }

    //might need, format dates func
    function formatDate(date) {
        const newDate = new Date(date)
        //might need to change day attribtue
        const options = { month: 'long', day: 'numeric', year: 'numeric' }
        return newDate.toLocaleDateString(undefined, options)
    }
    console.log(formatDate)

    return(
        <>
            <h1>allReviews</h1>
        </>
    )
}

export default BusinessReviews
