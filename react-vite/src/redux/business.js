// Action Creators
export const GET_ALL_DATA = 'business/GET_ALL_DATA'
export const GET_ONE_BUSINESS = 'business/GET_ONE_BUSINESS'
export const CREATE_NEW_BUSINESS = 'business/CREATE_NEW_BUSINESS'
export const UPDATE_BUSINESS = 'business/UPDATE_BUSINESS'
export const DELETE_BUSINESS = 'business/DELETE_BUSINESS'

// Action Types
const getAllData = (data) => {
    return {
        type: GET_ALL_DATA,
        data
    }
}

const getOneBusiness = (businessId) => {
    return {
        type: GET_ONE_BUSINESS,
        businessId
    }
}

const createNewBusiness = (data) => {
    return {
        type: CREATE_NEW_BUSINESS,
        data
    }
}

const updateBusiness = (data) => {
    return {
        type: UPDATE_BUSINESS,
        data
    }
}

const deleteBusiness = (businessId) => {
    return {
        type: DELETE_BUSINESS,
        businessId
    }
}

// Landing Page Thunk
export const landingPageThunk = () => async (dispatch) => {
    const response = await fetch('/api')

    if (!response.ok) {
        throw new Error('Failed to fetch data')
    }

    const all_data = await response.json()

    if (all_data.errors) {
        return all_data.errors;
    }

    dispatch(getAllData(all_data))
    return all_data
}

// Get Specific Business Thunk
export const specificBusinessThunk = (businessId) => async (dispatch) => {
    const response = await fetch(`/api/business/${businessId}`)

    if (!response.ok) {
        throw new Error('Failed to fetch specific business.')
    }

    const one_data = await response.json()
    if (one_data.errors) {
        return one_data.errors
    }

    dispatch(getOneBusiness(one_data))
    return one_data
}

// Get Business Menu Thunk
export const businessMenuThunk = (businessId) => async (dispatch) => {
    const response = await fetch(`/api/business/${businessId}/menu`)

    if (!response.ok) {
        throw new Error('Failed to fetch menu.')
    }

    const menu_data = await response.json()
    if (menu_data.errors) {
        return menu_data.errors
    }

    dispatch(getAllData(menu_data))
    return menu_data
}

// Get Business Amenities Thunk (Business Id)
export const businessAmenitiesThunk = (businessId) => async (dispatch) => {
    const response = await fetch(`/api/business/${businessId}/amenity`)

    if (!response.ok) {
        throw new Error('Failed to fetch menu.')
    }

    const amenity_data = await response.json()
    if (amenity_data.errors) {
        return amenity_data.errors
    }

    dispatch(getAllData(amenity_data))
    return amenity_data
}

// Create New Business Thunk
export const createNewBusinessThunk = (newBusiness) => async (dispatch) => {
    const response = await fetch('/api/business/new', {
        method: "POST",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(newBusiness)
    })
    console.log('resp@@@@@@', response)
    if (response.ok) {
        const data = await response.json()
        dispatch(createNewBusiness(data))
        console.log('data@@@@@@@', data)
        return data
    }else{
        const error = await response.json()
        return error
    }
}

// Update Business Thunk (Business Id)


// Delete Business Thunk (Business Id)


// TODO: Maybe need a Image Handler Thunk (Johnny)
    // ! : Backend route, Query all Images

function businessReducer(state = {}, action) {
    switch (action.type) {
        case GET_ALL_DATA: {
            return { ...state, ...action.data }
        }
        case GET_ONE_BUSINESS: {
            return { ...state, [ action.businessId.id ]: action.businessId }
        }
        case CREATE_NEW_BUSINESS: {
            return { ...state, ...action.data }
            }
        default:
            return state
    }
}

export default businessReducer
