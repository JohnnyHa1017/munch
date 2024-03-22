import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { useParams } from 'react-router-dom'
import { menuByBusinessThunk } from '../../redux/menu'
import { specificBusinessThunk } from '../../redux/business'

// TODO: @TylerHan1226 WE NEED TO CHECK UP ON THIS
// TODO: ADD MENU IMAGES

function MenusByBusinessId() {
    const dispatch = useDispatch()
    const { businessId } = useParams()
    const menus = useSelector((state) => state.menus.Menu)
    const menuImages = useSelector((state) => state.menus.Business_Images)
    const business = useSelector((state) => state.business[businessId])

    let menu_images = []
    if (menus) {
        for (let img of menuImages) {
            if (img.business_id == businessId) {
                menu_images.push(img)
            }
        }
    }

    useEffect(() => {
        dispatch(menuByBusinessThunk(businessId))
        dispatch(specificBusinessThunk(businessId)) //TO GET BUSINESS TITLE TO SHOW ON PAGE
    }, [dispatch, businessId])

    return (
        <>
            {menu_images.length > 0 && business && menus ? ( // Added null check here
                <div className='menu-page-container'>
                    <h1>{business?.title}'s Menu</h1>
                    <div className='menu-page-all-items-container'>
                        {menus.map((menu, index) => (
                            <div className='menu-item-container' key={index}>
                                <h3>{menu?.name}</h3>
                                <h4>{menu?.category}</h4>
                                <p>{menu?.description}</p>
                                {menu_images.length > 0 && menu_images[index] ? (
                                    <img className='menu-item-img' src={menu_images[index].url} alt={`Image for ${menu.menu_name}`} />
                                ) : (
                                    <p>No image available</p>
                                )}
                                {/* Render additional menu information here */}
                            </div>
                        ))}
                    </div>
                </div>
            ) : (
                <h2>Loading ...</h2> // Render a message if no images
            )}
        </>
    )
}

export default MenusByBusinessId
