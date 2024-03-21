import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate, useParams } from 'react-router-dom'
import { createReviewThunk } from '../../redux/reviews'
import { updateReviewThunk } from '../../redux/reviews'


const CreateNewReview = ({ buttonName, reviewToUpdate }) => {
    const dispatch = useDispatch()
    const { businessId, reviewId } = useParams()
    const user = useSelector((state) => state.session.user)
    const nav = useNavigate()

    const [review, setReview] = useState(reviewToUpdate?.review)
    const [star, setStars] = useState(reviewToUpdate?.star ?? null)
    const [image, setImage] = useState(reviewToUpdate?.image)
    const [validations, setValidations] = useState('')
    const [submitted, setSubmitted] = useState(false)
    const [hover, setHover] = useState(null)

    console.log('buttonName in CreateReview =>', buttonName)
    console.log('reviewToUpdate in CreateReview =>', reviewToUpdate)

    useEffect(() => {
        if (!user) {
            nav('/')
        }
    })

    const handleSubmit = async (e) => {
        e.preventDefault()
        setSubmitted(true)

        console.log()
        if (!reviewId) {
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
        } else {
            await dispatch(updateReviewThunk(reviewToUpdate, reviewId))
            nav(`/business/${businessId}`)
        }
    }


    return (
        <>
            {/* <h1>allReviews</h1> */}

            <form onSubmit={handleSubmit} className='review-form'>
                {/* <h1 className='title'>Create a Review</h1> */}
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
                    <button type='submit' className='Review-Submit-btn' disabled={star < 1}>{buttonName}</button>
                </div>
            </form>
        </>
    )
}

export default CreateNewReview
