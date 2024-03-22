import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { NavLink, useParams } from 'react-router-dom'
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
            if (img.business_id == businessId && img.menu_id) {
                menu_images.push(img)
            }
        }
        console.log('menu_images ==>', menu_images)
    }

    useEffect(() => {
        dispatch(menuByBusinessThunk(businessId))
        dispatch(specificBusinessThunk(businessId)) //TO GET BUSINESS TITLE TO SHOW ON PAGE
    }, [dispatch, businessId])

    return (
        <>
            {menu_images.length > 0 && business && menus ? ( // Added null check here
                <div className='menu-page-container'>
                    <NavLink to={`/business/${businessId}`}><h1 className='menu-detail-text-black'>{business?.title}'s Menu</h1></NavLink>
                    <div className='menu-page-all-items-container'>
                        {menus.map((menu, index) => {
                            const matchedImage = menu_images.find(image => image.menu_id === menu.id);
                            return (
                                <div className='menu-item-container' key={index}>
                                    <h2>{menu?.name}</h2>
                                    <h4>{menu?.category}</h4>
                                    <p>{menu?.description}</p>
                                    <p className='menu-detail-text'>{menu?.price} $</p>
                                    <img className='menu-item-img' src={matchedImage?.url} alt={`Image for ${menu.menu_name}`} />
                                </div>
                            )
                        })}
                    </div>
                </div>
            ) : (
                <h2>Loading ...</h2> // Render a message if no images
            )}
        </>
    )
}

export default MenusByBusinessId
