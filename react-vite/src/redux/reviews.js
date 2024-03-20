// Action Creators
export const GET_BUSINESS_REVIEWS = 'business/GET_BUSINESS_REVIEWS '
export const CREATE_REVIEW = 'business/CREATE_REVIEW'
export const UPDATE_REVIEW = 'business/UPDATE_REVIEW'
export const DELETE_REVIEW = 'business/DELETE_REVIEW'
export const ALL_REVIEW = 'review/ALL'
// Action Types
const getAllReviews = (allReviews)=>{
    return{
        type: ALL_REVIEW,
        allReviews
    }
}

const getAllData = (businessId)=>{
    return{
        type: GET_BUSINESS_REVIEWS,
        businessId
    }
}

const createReview = (newReview)=>{
    return{
        type: CREATE_REVIEW,
        newReview
    }
}

const updateReview = (data)=>{
    return{
        type: UPDATE_REVIEW,
        data
    }

}

const deleteReview = (reviewId)=>{
    return{
        type: DELETE_REVIEW,
        reviewId
    }

}


// Review Thunks
export const allReviewThunk = () => async (dispatch) => {
    const response = await fetch('/api/reviews/all')

    console.log('response ==>', response)
    
    if (!response.ok) {
        throw new Error('Failed to fetch reviews.')
    }

    const all_data = await response.json()

    if (all_data.errors) {
        return all_data.errors;
    }

    dispatch(getAllReviews(all_data))
    return all_data
}


export const businessReviewThunk = (businessId) => async (dispatch) => {
    const response = await fetch(`/api/business/${businessId}/reviews`)

    if (!response.ok) {
        throw new Error('Failed to fetch reviews.')
    }

    const all_data = await response.json()

    if (all_data.errors) {
        return all_data.errors;
    }

    dispatch(getAllData(all_data))
    return all_data
}

export const createReviewThunk = (businessId, newReview) => async (dispatch) => {
    const response = await fetch(`/api/business/${businessId}/reviews`,{
        method: "POST",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(newReview)
    })

    if (response.ok) {
        const data = await response.json()
        dispatch(createReview(data))
        return data

    }else{
        const error = await response.json()
        return error
    }
}


export const updateReviewThunk = (businessId) => async (dispatch) => {
    const response = await fetch(`/api/business/${businessId}/reviews`,{

    })


    dispatch(updateReview)
}

export const deleteReviewThunk = (businessId) => async (dispatch) => {
    const response = await fetch(`/api/business/${businessId}/reviews`)

    dispatch(deleteReview)
}


//reducers
function reviewReducer(state={}, action){
    switch(action.type){
        case ALL_REVIEW:{
            return { ...state, ...action.allReviews}
        }
        case GET_BUSINESS_REVIEWS:{
            return { ...state, ...action.businessId}
        }
        case CREATE_REVIEW:{
            return { ...state, ...action.data}
        }
        case UPDATE_REVIEW:{
            return { ...state, ...action.data}
        }
        case DELETE_REVIEW:{
            const newState = { ...state }
            delete newState[action.reviewId]
            return newState
        }
        default:
            return state
    }
}

export default reviewReducer