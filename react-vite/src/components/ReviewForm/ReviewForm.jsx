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
    const [image, setImage] = useState(reviewToUpdate?.image ?? null);
    const [imageLoading, setImageLoading] = useState(false);
    const [validations, setValidations] = useState('')
    const [submitted, setSubmitted] = useState(false)
    const [hover, setHover] = useState(null)

    console.log(submitted)

    // console.log('buttonName in CreateReview =>', buttonName)
    // console.log('reviewToUpdate in CreateReview =>', reviewToUpdate)

    useEffect(() => {
        if (!user) {
            nav('/')
        }
    },)

    const handleSubmit = async (e) => {
        e.preventDefault()
        const formData = new FormData();
        formData.append("image", image);
        setImageLoading(true);
        setSubmitted(true)

        await Promise.resolve(formData);

        const reviewObj = {
            review, star, image
        }

        if (!reviewId) {
            console.log('CREATE REVIEW')
            const newReview = {
                review, star, image
            }
            try {
                await dispatch(createReviewThunk(businessId, newReview))
                nav(`/business/${businessId}`);
            } catch (error) {
                setValidations({ ...validations, message: 'Cannot add review' })
                // console.error("Error creating review:", error);
            }
        } else {
            const updateReview = await dispatch(updateReviewThunk(reviewObj, reviewId))
            console.log(updateReview)
            nav(`/business/${businessId}`)
        }
    }


    return (
        <>
            <div>
                <form
                    onSubmit={handleSubmit}
                    encType="multipart/form-data"
                    className="review-form-container"
                >
                    {/* <h1 className='title'>Create a Review</h1> */}
                    {submitted && validations && validations.message && <p>{validations.message}</p>}
                    <div className='Stars-field'>
                        {[1, 2, 3, 4, 5].map((star, i) => {
                            const ratingValue = i + 1;
                            return (
                                <label key={i}>
                                    <span
                                        className='Stars'
                                        onClick={() => setStars(ratingValue)}
                                        onMouseEnter={() => setHover(ratingValue)}
                                        onMouseLeave={() => setHover(ratingValue)}
                                    >
                                        {ratingValue <= (hover || star) ? '★' : '☆'}
                                    </span>
                                </label>
                            );
                        })}
                    </div>
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
                    {(review.length <= 15) && (
                        <p style={{ color: 'red' }}>Your review must be greater than 15 characters</p>
                    )}
                    {(star < 1) && (
                        <p style={{ color: 'red' }}>You must select a star rating</p>
                    )}
                    <label>
                        <div>

                        </div>

                        <input
                            type='file'
                            accept="image/*"
                            onChange={(e) => setImage(e.target.files[0])}
                            placeholder='Add a Review Image'
                        ></input>
                    </label>
                    {submitted && validations.image && (<p style={{ color: 'red' }}>{validations.image}</p>)}

                    <div className='Review-Btn-container'>
                        <button type='submit' className='Review-Submit-btn' disabled={star < 1 || review.length <= 15}>{buttonName}</button>
                        {(imageLoading) && <p>Loading...</p>}
                    </div>
                </form>
            </div>
        </>
    )
}

export default CreateNewReview
