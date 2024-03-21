// Action Creators
export const GET_MENU_BY_BUSINESS = 'menu/GET_MENU_BY_BUSINESS'
export const CREATE_MENU = 'menu/CREATE_MENU'


// Action Types
const getMenuByBusiness = (menus) => {
    return {
        type: GET_MENU_BY_BUSINESS,
        menus
    }
}
const createMenu = (newMenu) => {
    return {
        type: CREATE_MENU,
        newMenu
    }
}


// Landing Page Thunk
export const menuByBusinessThunk = (businessId) => async (dispatch) => {
    const response = await fetch(`/api/business/${businessId}/menu`)
    if (!response.ok) {
        throw new Error('Failed to fetch menu')
    }
    const menus = await response.json()
    if (menus.errors) {
        return menus.errors
    }
    dispatch(getMenuByBusiness(menus))
    return menus
}
export const createMenuThunk = (businessId, newMenu) => async (dispatch) => {
    const response = await fetch(`/api/business/${businessId}/menu/new`, {
        method: "POST",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(newMenu)
    })
    if (!response.ok) {
        throw new Error('Failed to create menu')
    }
    const newMenuRes = await response.json()
    if (newMenuRes.errors) {
        return newMenuRes.errors
    }
    dispatch(createMenu(newMenuRes))
    return newMenuRes
}

//reducers
function menuReducer(state={}, action) {
    switch(action.type){
        case GET_MENU_BY_BUSINESS: {
            return {...state, ...action.menus}
        }
        case CREATE_MENU: {
            return {...state, ...action.newMenu}
        }
        default:
            return state
    }
}

export default menuReducer