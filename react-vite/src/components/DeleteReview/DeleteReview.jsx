import { useParams } from 'react-router-dom'
import { useEffect } from 'react'
import { useModal } from '../../context/Modal'
import { useDispatch, useSelector } from 'react-redux'
import { deleteReviewThunk } from '../../redux/reviews'
// import './DeleteReview.css'

const DeleteReview = ()=>{
    const { reviewId } = useParams()
    // console.log('reviewId===>', reviewId)
    const dispatch = useDispatch()
    const { closeModal } = useModal()

    const onDelete = (e) => {
        e.preventDefault()
        dispatch(deleteReviewThunk(reviewId))
        closeModal()
    }

    return (
        <>
            <button className = "DeleteReview-btn" onClick={onDelete}>
                Yes (Delete Review)
            </button>
            <button className = 'Dont-DeleteReview-btn' onClick={closeModal}>
                No (Keep Review)
            </button>
        </>
    )
}

export default DeleteReview
