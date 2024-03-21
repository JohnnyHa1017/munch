import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { useParams } from 'react-router-dom'
import { menuByBusinessThunk } from '../../redux/menu'


function MenusByBusinessId() {
    const dispatch = useDispatch()
    const menus = useSelector((state) => state.menus)
    const { businessId } = useParams()

    console.log('menus ==>', menus)
    console.log('businessId ==>', businessId)

    useEffect(() => {
        dispatch(menuByBusinessThunk(businessId))
    }, [dispatch, businessId])

    return (
        <>
            <h1>Menus!</h1>
        </>
    )
}

export default MenusByBusinessId
