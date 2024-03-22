import { useDispatch, useSelector } from 'react-redux';
import { useEffect } from 'react';
import { landingPageThunk } from '../../redux/business'
import { NavLink } from 'react-router-dom';
import './ManageBusiness.css'
import { menuByBusinessThunk } from '../../redux/menu';

function ManageBusiness() {
    const dispatch = useDispatch()
    const currUser = useSelector(state => state.session.user)
    const business = useSelector(state => state.business.Business)
    const amenities = useSelector(state => state.business.Amenities)
    const menus = useSelector(state => console.log(state.menus.Menu))

    const currBusiness = []
    useEffect(() => {
        dispatch(landingPageThunk())
        // for(let bus of currBusiness){ //pulls menus from all business in currentbusiness arr
        //     dispatch(menuByBusinessThunk(bus.id))
        // }
    },[dispatch])

    if(!currUser || !business){
        return <div>Loading...</div>
    }

    for(let bus of business){ //adding business into the currBus arr
        if(bus?.owner_id == currUser?.id){
            currBusiness.push(bus)
        }
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

    function checkMenu(businessId){
        // for(let m of menus){
        //     if(m.business_id == businessId){
        //         return true
        //     }
        // }
        return false
    }

    return(
        <>
            <h1>Hello {currUser.first_name}</h1>
            <NavLink to={`/`}>See all your reviews!</NavLink>
            <div className='manage-businesses-container'>
                {!currBusiness && (
                    <>
                        <p>You have no businesses</p>
                        <button><NavLink>Create a business!</NavLink></button>
                    </>
                )}
                {currBusiness.map(bus => (
                    <NavLink key={bus?.id} to={`/business/${bus?.id}`}>
                        <p className='manage-bus-title'>{bus?.title}</p>
                        <p className='manage-bus-address'>{bus?.address}</p>
                        <p className='manage-bus-city'>{bus?.city}, {bus?.state}</p>
                        <button><NavLink to={`/business/${bus?.id}/edit`}>Update Business</NavLink></button>
                        <button><NavLink to={`/business/${bus?.id}/delete`}>Delete Business</NavLink></button>
                        {!checkAmenity(bus.id) && (
                            <button><NavLink to={`/business/${bus.id}/amenities`}>Add Amenities</NavLink></button>
                        )}
                        {!checkMenu(bus.id) && (
                            <button><NavLink to={`/business/${bus.id}/menus/new`}>Add Menu</NavLink></button>
                        )}
                    </NavLink>
                ))}
            </div>
        </>
    )
}

export default ManageBusiness;
