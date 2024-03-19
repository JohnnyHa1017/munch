export const GET_ALL_DATA = 'business/GET_ALL_DATA'

const getAllData = (data) => {
    return {
        type: GET_ALL_DATA,
        data
    }
}

export const landingPageThunk = () => async (dispatch) => {
    const response = await fetch('/')
    console.log('response ==>', response)
    if (!response.ok) {
        throw new Error('Failed to fetch data')
    }
    if (response.ok) {
        console.log('here')
        const all_data = await response.json()    
        console.log('all_data ==>', all_data)   
        if (all_data.errors) {
            return all_data.errors;
        }
        dispatch(getAllData(all_data))
        return all_data
    }
}


const initialState = {
    businesses: [],
    amenities: [],
    reviews: [],
}
function businessReducer(state=initialState, action) {
    switch (action.type) {
        case GET_ALL_DATA: {
            return {...state,
                     businesses: [action.data.businesses],
                     amenities: [action.data.amenities],
                     reviews: [action.data.reviews]
                    }
        }
        default:
            return state
    }
}

export default businessReducer


