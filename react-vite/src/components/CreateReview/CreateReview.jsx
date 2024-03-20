import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate, useParams } from 'react-router-dom'
import { createReviewThunk } from '../../redux/reviews'

const CreateNewReview = () => {
    const dispatch = useDispatch()
    const { businessId } = useParams()
    console.log('businessId ==>', businessId)
    const user = useSelector((state) => state.session.user)
    const nav = useNavigate() 

    const [review, setReview] = useState('')
    const [star, setStars] = useState(null)
    const [image, setImage] = useState('')
    const [validations, setValidations] = useState('')
    const [submitted, setSubmitted] = useState(false)
    const [hover, setHover] = useState(null)

    useEffect(() => {
        if (!user) {
            nav('/')
        }
    })

    const handleSubmit = async (e) => {
        e.preventDefault()
        setSubmitted(true)
        
        const newReview = {
            review, star, image
        }
        try {
            await dispatch(createReviewThunk(businessId, newReview))
            nav(`/business/${businessId}`);
        } catch (error) {
            setValidations({ message: 'Cannot add review' })
            // console.error("Error creating review:", error);
        }

    }


    return (
        <>
            {/* <h1>allReviews</h1> */}

            <form onSubmit={handleSubmit} className='review-form'>
                <h1 className='title'>Create a Review</h1>
                {validations.review && <p>{validations.message}</p>}
                <textarea
                    className='review-textarea'
                    type='text'
                    name='review'
                    value={review}
                    onChange={(e) => setReview(e.target.value)}
                    placeholder='Leave your review here...'
                    rows={7}
                    cols={70}
                />
                {/* <label>
                    Image
                    <input type='file' name='image' value={image} placeholder='image'
                        onChange={(e) => setImage(e.target.value)}
                    ></input>
                </label> */}
                <label>
                    Image
                    <input type='text' name='image' value={image} placeholder='image'
                        onChange={(e) => setImage(e.target.value)}
                    ></input>
                </label>
                <div className='Stars-field'>
                    {[1, 2, 3, 4, 5].map((star, i) => {
                        const ratingValue = i + 1
                        return (
                            <label key={i}>
                                <span
                                    className='Stars'
                                    onClick={() => setStars(ratingValue)}
                                    onMouseEnter={() => setHover(ratingValue)}
                                    onMouseLeave={() => setHover(null)}
                                >
                                    {ratingValue <= (hover || star) ? '★' : '☆'}
                                </span>
                            </label>
                        )
                    })}
                </div>
                <div className='Review-Btn-container'>
                    <button type='submit' className='Review-Submit-btn' disabled={star < 1}>Submit Your Review</button>
                </div>
            </form>
        </>
    )
}

export default CreateNewReview
