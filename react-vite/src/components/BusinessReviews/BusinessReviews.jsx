import { useParams } from 'react-router-dom'
import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { businessReviewThunk } from '../../redux/reviews'
// import './BusinessReview.css'

function BusinessReviews(){
    const { businessId } = useParams()
    const dispatch = useDispatch()
    const reviews = useSelector((state)=> state.reviews)

    console.log('@@@@!',reviews)
    const reviewArray = Object.values(reviews).filter((review)=>review.businessId === parseInt(businessId)).reverse()

    console.log('@@@@!ARR', reviewArray)
    const currUser = useSelector((state)=> state.session.user)

    useEffect(()=>{
        dispatch(businessReviewThunk(businessId))
    }, [dispatch, businessId])

    if(!reviewArray.length){
        return <div className='NoReview'>Be the first to review</div>
    }

    //might need, format dates func
    function formatDate(date) {
        const newDate = new Date(date)
        //might need to change day attribtue
        const options = { month: 'long', day: 'numeric', year: 'numeric' }
        return newDate.toLocaleDateString(undefined, options)
    }

    return(
        <>
            <h1>allReviews</h1>
        </>
    )
}

export default BusinessReviews
