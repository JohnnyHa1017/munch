import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { useParams } from 'react-router-dom'
import { menuByBusinessThunk } from '../../redux/menu'
import { specificBusinessThunk } from '../../redux/business'


function MenusByBusinessId() {
    const dispatch = useDispatch()
    const { businessId } = useParams()
    const menus = useSelector((state) => state.menus.Menu)
    const all_business_images = useSelector((state) => state.menus.Business_Images)
    const business = useSelector((state) => state.business)

    let menu_images = []
    if (all_business_images) {
        menu_images = all_business_images.filter(img => img.business_id == businessId && typeof img.menu_id == 'number')
        console.log('menu_images ==>', menu_images)
        //    console.log('menu_images[0].url ==>', menu_images[0].url)
    }

    console.log('menus ==>', menus)
    console.log('business ==>', business)

    useEffect(() => {
        dispatch(menuByBusinessThunk(businessId))
        dispatch(specificBusinessThunk(businessId))
    }, [dispatch, businessId])

    return (
        <>
            {menu_images.length > 0 ? ( // Added null check here
                <div>
                    {menus.map((menu, index) => (
                        <div key={index}>
                            <h3>{menu.name}</h3>
                            <h4>{menu.category}</h4>
                            <p>{menu.description}</p>
                            {menu_images.length > 0 && menu_images[index] ? (
                                <img className='menu-item-img' src={menu_images[index].url} alt={`Image for ${menu.menu_name}`} />
                            ) : (
                                <p>No image available</p>
                            )}
                            {/* Render additional menu information here */}
                        </div>
                    ))}
                    {menus.length === 0 && <h2>Loading ...</h2>}
                </div>

            ) : (
                <h2>Loading ...</h2> // Render a message if no images
            )}
        </>
    )
}

export default MenusByBusinessId
