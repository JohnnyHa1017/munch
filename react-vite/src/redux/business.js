export const GET_ALL_DATA = 'business/GET_ALL_DATA'

const getAllData = (data) => {
    return {
        type: GET_ALL_DATA,
        data
    }
}


// Change URL path
export const landingPageThunk = () => async (dispatch) => {
    const response = await fetch('http://127.0.0.1:8000/')
    console.log('response ==>', response)
    if (!response.ok) {
        throw new Error('Failed to fetch data')
    }
    const all_data = await response.json()
    console.log('all_data ==>', all_data)
    if (all_data.errors) {
        return all_data.errors;
    }
    dispatch(getAllData(all_data))
    return all_data

}



function businessReducer(state = {}, action) {
    switch (action.type) {
        case GET_ALL_DATA: {
            return {
                ...state,
                ...action.data
            }
        }
        default:
            return state
    }
}

export default businessReducer

