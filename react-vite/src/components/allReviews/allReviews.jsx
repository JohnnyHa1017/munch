import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { allReviewThunk } from '../../redux/reviews'

function AllReviews() {
    const dispatch = useDispatch()
    const data = useSelector((state) => state.allReviews)

    useEffect(() => {
        dispatch(allReviewThunk())
    }, [dispatch])

    console.log('@@@DATA', data)

    return (
        <>
            <h1>allreviews</h1>
        </>
    )
}

export default AllReviews
