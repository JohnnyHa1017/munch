import { useDispatch, useSelector } from 'react-redux';
import { useEffect } from 'react';
import { landingPageThunk } from '../../redux/business'
import { NavLink } from 'react-router-dom';
import './ManageBusiness.css'

function ManageBusiness() {
    const dispatch = useDispatch()
    const currUser = useSelector(state => state.session.user)
    const business = useSelector(state => state.business.Business)
    const amenities = useSelector(state => state.business.Amenities)

    useEffect(() => {
        dispatch(landingPageThunk())
    },[dispatch])

    if(!currUser || !business){
        return <div>Loading...</div>
    }

    const currBusiness = []
    for(let bus of business){
        if(bus.owner_id == currUser.id){
            currBusiness.push(bus)
        }
    }
    console.log('currBusiness ==>', currBusiness)

    let amenityArr = []
    if (currBusiness && business) {
        for (let amenity of amenities) {
            for (let eachBusiness of currBusiness) {
                if (amenity.business_id == eachBusiness.id) {
                    amenityArr.push(amenity)
                }
            }
        }
        console.log('amenityArr ==>', amenityArr)
    }

    // TODO add amenity check
    let isAmenity = false
    function checkAmenity (businessId) {
        for (let a of amenityArr) {
            console.log('a ==>', a)
            if (a.business_id == businessId) {
                isAmenity = !isAmenity
            }
        }
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
                        {
                            !isAmenity && checkAmenity(bus?.id) &&  (
                            <>
                                <button><NavLink>Amenity</NavLink></button>
                            </>)
                        }
                    </NavLink>
                ))}
            </div>
        </>
    )
}

export default ManageBusiness;
