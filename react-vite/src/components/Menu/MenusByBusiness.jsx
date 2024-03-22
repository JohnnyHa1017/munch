import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { useParams } from 'react-router-dom'
import { menuByBusinessThunk } from '../../redux/menu'
import { specificBusinessThunk } from '../../redux/business'

// TODO: @TylerHan1226 WE NEED TO CHECK UP ON THIS

function MenusByBusinessId() {
    const dispatch = useDispatch()
    const { businessId } = useParams()
    const menus = useSelector((state) => state.menus.Menu)
    const all_business_images = useSelector((state) => state.menus.Business_Images)
    const business = useSelector((state) => state.business.Business)

    // !: THIS IS NOT FILTERING FOR IMAGES NOR IS IT FILTERING ANYTHING
    // ?: WE'RE CONSTANTLY GRABBING THE FULL ARRAY OF BUSINESS_IMAGES EVERY TIME (COUNT 78)

    let menu_images = []
    if (all_business_images) {
        console.log('DO I EXIST? WHAT AM I? @MENUS BY BUSINESS.JSX', all_business_images)
        // ?: NOTHING PRINTS - IF BLOCK NEVER HAPPENS

        menu_images = all_business_images.filter(img => img.business_id == businessId && typeof img.menu_id == 'number')

        console.log('DO I EXIST? DO I HOLD ANYTHING, WHAT AM I?', menu_images, '@MENUS BY BUSINESS.JSX')
        // ?: NOTHING PRINTS - IF BLOCK NEVER HAPPENS
    }

    useEffect(() => {
        dispatch(menuByBusinessThunk(businessId))
        // TODO: WE HAD A DISPATCH SPECIFIC BUSINESS THUNK IN HERE WHICH
        // TODO: I REALLY DONT THINK IT WAS DOING ANYTHING
        // !: THIS WAS REMOVED AND NOTHING HAD CHANGED
    }, [dispatch, businessId])

    return (
        <>
            {menu_images.length > 0 && business.Business ? ( // Added null check here
                <div>
                    <h1>{business.Business.title}'s Menu</h1>
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
