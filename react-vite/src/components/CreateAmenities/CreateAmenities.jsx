import { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { useNavigate, useParams } from 'react-router-dom'
import { createNewAmenitiesThunk, specificBusinessThunk, businessAmenitiesThunk} from '../../redux/business'

function CreateAmenity () {
    const dispatch = useDispatch()
    const nav = useNavigate()
    const { businessId } = useParams()
    const business = useSelector(state => state.business)

    useEffect(()=> {
        dispatch(specificBusinessThunk(businessId))
        dispatch(businessAmenitiesThunk(businessId))
    },[dispatch, businessId])

    const [reservation, setReservation] = useState(false)
    const [delivery, setDelivery] = useState(false)
    const [pickup, setPickup] = useState(false)
    const [vegetarian, setVegetarian] = useState(false)
    const [accepts_credit_card, setAcceptsCreditCard] = useState(false)
    const [free_wi_fi, setFreeWifi] = useState(false)
    const [street_parking, setStreetParking] = useState(false)
    const [good_for_groups, setGoodForGroups] = useState(false)
    const [outdoor_seating, setOutdoorSeating] = useState(false)
    const [submitted, setSubmitted] = useState(false)

    const handleSubmit = async (e) => {
        e.preventDefault()
        setSubmitted(true)
        const newAmenity = {
            reservation,
            delivery,
            pickup,
            vegetarian,
            accepts_credit_card,
            free_wi_fi,
            street_parking,
            good_for_groups,
            outdoor_seating
        }
        await dispatch(createNewAmenitiesThunk(businessId, newAmenity))
        nav(`/business/${businessId}`)
    }

    return(
        <>
            <h1>Add your amenities</h1>
            <form onSubmit={handleSubmit}>
                <label>
                    Reservation
                    <input
                        type='checkbox'
                        name='reservation'
                        checked={reservation}
                        onChange={(e) => setReservation(e.target.checked)}
                    ></input>
                </label>
                <label>
                    Delivery
                    <input
                        type='checkbox'
                        name='delivery'
                        checked={delivery}
                        onChange={(e) => setDelivery(e.target.checked)}
                    ></input>
                </label>
                <label>
                    Pick up
                    <input
                        type='checkbox'
                        name='pick up'
                        checked={pickup}
                        onChange={(e) => setPickup(e.target.checked)}
                    ></input>
                </label>
                <label>
                    Vegetarian
                    <input
                        type='checkbox'
                        name='vegetarian'
                        checked={vegetarian}
                        onChange={(e) => setVegetarian(e.target.checked)}
                    ></input>
                </label>
                <label>
                    Accepts credit card
                    <input
                        type='checkbox'
                        name='accepts credit card'
                        checked={accepts_credit_card}
                        onChange={(e) => setAcceptsCreditCard(e.target.checked)}
                    ></input>
                </label>
                <label>
                    Free Wifi
                    <input
                        type='checkbox'
                        name='free wifi'
                        checked={free_wi_fi}
                        onChange={(e) => setFreeWifi(e.target.checked)}
                    ></input>
                </label>
                <label>
                    Street Parking
                    <input
                        type='checkbox'
                        name='street parking'
                        checked={street_parking}
                        onChange={(e) => setStreetParking(e.target.checked)}
                    ></input>
                </label>
                <label>
                    Good for groups
                    <input
                        type='checkbox'
                        name='good for groups'
                        checked={good_for_groups}
                        onChange={(e) => setGoodForGroups(e.target.checked)}
                    ></input>
                </label>
                <label>
                    Outdoor seating
                    <input
                        type='checkbox'
                        name='outdoor seating'
                        checked={outdoor_seating}
                        onChange={(e) => setOutdoorSeating(e.target.checked)}
                    ></input>
                </label>
                <button type='submit'>Add Amenities</button>
            </form>
        </>
    )
}

export default CreateAmenity;
