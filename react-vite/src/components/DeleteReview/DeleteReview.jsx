import { useNavigate, useParams } from 'react-router-dom'
import { useModal } from '../../context/Modal'
import { useDispatch } from 'react-redux'
import { deleteReviewThunk } from '../../redux/reviews'
// import './DeleteReview.css'

const DeleteReview = ()=>{
    const { reviewId, businessId } = useParams()
    const nav = useNavigate()
    // console.log('reviewId===>', reviewId)
    const dispatch = useDispatch()
    const { closeModal } = useModal()

    const onDelete = (e) => {
        e.preventDefault()
        dispatch(deleteReviewThunk(reviewId))
        closeModal()
        nav(`/business/${businessId}`)
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
