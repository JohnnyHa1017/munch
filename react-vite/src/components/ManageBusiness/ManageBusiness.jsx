import { useDispatch, useSelector } from 'react-redux';
import { useEffect } from 'react';
import { getBusinessImagesThunk, landingPageThunk } from '../../redux/business'
import { NavLink } from 'react-router-dom';
import './ManageBusiness.css'
import { getAllMenusThunk } from '../../redux/menu';

function ManageBusiness() {
    const dispatch = useDispatch()
    const currUser = useSelector(state => state.session.user)
    const business = useSelector(state => state.business.Business)
    const busImgs = useSelector(state => state.business.Business_Images)
    const amenities = useSelector(state => state.business.Amenities)
    const menus = useSelector(state => state.menus)

    // console.log('CURRENT USER', currUser)
    // console.log('BUSINESS', business)
    // console.log('AMENITIES', amenities)
    // console.log('MENUS ------->', menus)
    // console.log('BUSIMAGES', busImgs)

    useEffect(() => {
        dispatch(landingPageThunk())
        dispatch(getAllMenusThunk())
        dispatch(getBusinessImagesThunk())
    },[dispatch])

    if(!currUser || !business || !amenities || !menus || !busImgs){
        return <div>Loading...</div>
    }

    const currBusiness = []
    for(let bus of business){ //adding business into the currBus arr
        if(bus?.owner_id == currUser?.id){
            currBusiness.push(bus)
        }
    }

    function getImgs(businessId) {
        let imgs= busImgs.filter(img => img.business_id == businessId);
        const length = imgs.length
        if(length){
            return imgs[Math.floor(Math.random() * length)].url
        }
        return null
    }


    let amenityArr = []
    if (currBusiness && business) {
        for (let amenity of amenities) {
            for (let eachBusiness of currBusiness) {
                if (amenity.business_id == eachBusiness.id) {
                    amenityArr.push(amenity)
                }
            }
        }
    }

    function checkAmenity (businessId) {
        for (let a of amenityArr) {
            if (a.business_id == businessId) {
                return true
            }
        }
        return false
    }
    const menuArr = Object.keys(menus).map( key => ({
        id: key,
        ...menus[key]
    }))

    function checkMenu(businessId){
        for(let m of menuArr){
            if(m.business_id == businessId){
                return true
            }
        }
        return false
    }

    return(
        <>
            <h1>Hello {currUser.first_name}</h1>
            <h2>Your Businesses</h2>
            <div className='manage-businesses-container'>
                {!currBusiness && (
                    <>
                        <p>You have no businesses</p>
                        <button><NavLink>Create a business!</NavLink></button>
                    </>
                )}
                {currBusiness.map(bus => (
                    <div className='manage-onebusiness-container'>
                        <NavLink className='manage-nav-container'key={bus?.id} to={`/business/${bus?.id}`}>
                            <div className='nav-bus-container'>
                                <div className='manage-address-container'>
                                    <p className='manage-bus-title'>{bus?.title}</p>
                                    <p className='manage-bus-address'>{bus?.address}</p>
                                    <p className='manage-bus-city'>{bus?.city}, {bus?.state}</p>
                                    {checkMenu(bus.id) && (
                                        <NavLink className='manage-see-menu' to={`/business/${bus.id}/menus`}>See Menu</NavLink>
                                    )}
                                </div>
                            {getImgs(bus.id) && (
                                <img className='manage-bus-img 'src={getImgs(bus.id)} alt={`Image for ${bus.title}`} />
                                )}
                            </div>
                        </NavLink>
                        <button className='manage-btns'><NavLink to={`/business/${bus?.id}/edit`} className='manage-btn-text'>Update Business</NavLink></button>
                        <button className='manage-btns manage-delete'><NavLink to={`/business/${bus?.id}/delete`} className='manage-btn-text'>Delete Business</NavLink></button>
                        {!checkAmenity(bus.id) && (
                            <button className='manage-btns'><NavLink to={`/business/${bus.id}/amenities`} className='manage-btn-text'>Add Amenities</NavLink></button>
                        )}
                        {!checkMenu(bus.id) && (
                            <button className='manage-btns'><NavLink to={`/business/${bus.id}/menus/new`} className='manage-btn-text'>Add Menu</NavLink></button>
                        )}
                    </div>
                ))}
            </div>
        </>
    )
}

export default ManageBusiness;
