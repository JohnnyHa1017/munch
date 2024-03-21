import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useNavigate } from 'react-router-dom'
import { createNewBusinessThunk, updateBusinessThunk } from '../../redux/business'

const CreateNewBusiness = ({ buttonName, business }) => {
  const dispatch = useDispatch()
  const nav = useNavigate()
  const user = useSelector((state) => state.session.user)
  const { businessId } = useParams()

  // let checkBusiness = Object.values(business)

  const [title, setTitle] = useState(business?.title );
  const [address, setAddress] = useState(business?.address);
  const [city, setCity] = useState(business?.city);
  const [state, setState] = useState(business?.state);
  const [country, setCountry] = useState(business?.country);
  const [lat, setLat] = useState(business?.lat);
  const [lng, setLng] = useState(business?.lng);
  const [description, setDescription] = useState(business?.description);
  const [phone_number, setPhoneNumber] = useState(business?.phone_number);
  const [price_rating, setPrice] = useState(business?.price_rating);
  const [category, setCategory] = useState(business?.category);
  const [previewImage, setPreviewImage] = useState(business?.previewImage);
  // const [schedule, setSchedule] = useState(business?.schedule);
  const [mondayopen, setMondayOpen] = useState('')
  const [mondayclose, setMondayClose]= useState('')
  const [tuesdayopen, setTuesdayOpen] = useState('')
  const [tuesdayclose, setTuesdayClose] = useState('')
  const [validations, setValidations] = useState({})
  const [submitted, setSubmitted] = useState(false)



  useEffect(() => {
    const errors = {}
    if (!user) {
      nav('/')
    }
    if (!title || (title.length > 50)) {
      errors.title = 'Title is required and can only be under 50 characters.'
    }
    if (!address || (address.length > 50)) {
      errors.address = 'Address is required and can only be under 50 characters.'
    }
    if (!city || city.length > 30) {
      errors.city = 'City is required and can only be under 30 characters.'
    }
    if (!state || (state.length > 20)) {
      errors.state = 'State is required and can only be under 20 characters.'
    }
    if (!country || (country.length > 20)) {
      errors.county = 'Country is required and can only be under 20 characters.'
    }
    if (!lat || (lat >= 90) || (lat <= -90)) {
      errors.lat = 'Latitude must be between -90 and 90.'
    }
    if (!lng || (lng >= 180) || (lng <= -180)) {
      errors.lng = 'Longitude must be between -180 and 180.'
    }
    if (!description || (description.length > 2000)) {
      errors.description = 'Description is required and must be 2000 characters or less.'
    }
    if (!phone_number || (phone_number.length > 20)) {
      errors.phone_number = "Phone Number is required and must be unique, can't be more than 20 characters."
    }
    if (!price_rating) {
      errors.price_rating = "Price Rating is required and must be an integer of 1 to 5."
    }
    if (!category) {
      errors.category = 'Atleast one category must be selected.'
    }

    setValidations(errors)
  }, [user, nav, title, address, city, state, country, lat, lng, description, phone_number, price_rating, category])

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSubmitted(true);

    let createSchedule = `Monday: ${mondayopen} - ${mondayclose},
                          Tuesday: ${tuesdayopen} - ${tuesdayclose},
                          Wednesday:
                        `
    console.log(createSchedule, 'created schedule')

    let business ={
      title,
      address,
      city,
      state,
      country,
      description,
      phone_number,
      price_rating,
      lat,
      lng,
      category,
      schedule: createSchedule,
      previewImage
    }

  if (!Object.keys(validations).length) {
    if (!businessId) {
        const createBusiness = await dispatch(createNewBusinessThunk(business))
        if(createBusiness && createBusiness.id){
          nav(`/business/${createBusiness.id}`);
        }
      }
    else {
      const updateBusiness = await dispatch(updateBusinessThunk(business, businessId))
      console.log(submitted, updateBusiness)
      nav(`/business/${businessId}`);
    }
  }
}



  return (
    <form
      className='business-form'
      onSubmit={handleSubmit}
    >
      <h2>Where is your business located?</h2>
      <label>
        Business Name
        <input
          type='text'
          name='title'
          value={title}
          placeholder='Business Name'
          onChange={(e) => setTitle(e.target.value)}
        ></input>
      </label>
      {validations.title && (<p>{validations.title}</p>)}
      <label>
        Address
        <input
          type='text'
          name='address'
          value={address}
          placeholder='Address'
          onChange={(e) => setAddress(e.target.value)}
        ></input>
      </label>
      {validations.address && (<p>{validations.address}</p>)}
      <label>
        City
        <input
          type='text'
          name='city'
          value={city}
          placeholder='City'
          onChange={(e) => setCity(e.target.value)}
        ></input>
      </label>
      {validations.city && (<p>{validations.city}</p>)}
      <label>
        State
        <input
          type='text'
          name='state'
          value={state}
          placeholder='State'
          onChange={(e) => setState(e.target.value)}
        ></input>
      </label>
      {validations.state && (<p>{validations.state}</p>)}
      <label>
        Country
        <input
          type='text'
          name='country'
          value={country}
          placeholder='Country'
          onChange={(e) => setCountry(e.target.value)}
        ></input>
      </label>
      {validations.country && (<p>{validations.country}</p>)}
      <label>
        Price
        <input
          type='text'
          name='price'
          value={price_rating}
          placeholder='Price'
          onChange={(e) => setPrice(e.target.value)}
        ></input>
      </label>
      {validations.price && (<p>{validations.price}</p>)}
      <label>
        Category
        <input
          list='categories'
          name='category'
          value={category}
          onChange={(e) => setCategory(e.target.value)}
        ></input>
        <datalist id='categories'>
          <option value='American'></option>
          <option value='Asian Fusion'></option>
          <option value='Bar'></option>
          <option value='Brunch'></option>
          <option value='Cafe'></option>
          <option value='Casual'></option>
          <option value='Cocktail Bar'></option>
          <option value='Deli'></option>
          <option value='Dessert'></option>
          <option value='Dinner'></option>
          <option value='Fast Food'></option>
          <option value='Fine Dining'></option>
          <option value='German'></option>
          <option value='Indian'></option>
          <option value='Italian'></option>
          <option value='Japanese'></option>
          <option value='Mexican'></option>
          <option value='Palestinian'></option>
          <option value='Pub'></option>
          <option value='Seafood'></option>
          <option value='Tapas'></option>
        </datalist>
      </label>
      {validations.category && (<p>{validations.category}</p>)}
      <label>
        Latitude
        <input
          type='text'
          name='lat'
          value={lat}
          placeholder='Latitude'
          onChange={(e) => setLat(e.target.value)}
        ></input>
      </label>
      {validations.lat && (<p>{validations.lat}</p>)}
      <label>
        Longitude
        <input
          type='text'
          name='lng'
          value={lng}
          placeholder='Longitude'
          onChange={(e) => setLng(e.target.value)}
        ></input>
      </label>
      {validations.lng && (<p>{validations.lng}</p>)}
      <label>
        Phone Number
        <input
          type='text'
          name='phone number'
          value={phone_number}
          placeholder='Phone Number'
          onChange={(e) => setPhoneNumber(e.target.value)}
        ></input>
      </label>
      {validations.phone_number && (<p>{validations.phone_number}</p>)}
      <label>
        Description
        <input
          type='text'
          name='description'
          value={description}
          placeholder='Description'
          onChange={(e) => setDescription(e.target.value)}
        ></input>
      </label>
      {validations.description && (<p>{validations.description}</p>)}
      <label>
        Preview Image
        <input
          type='file'
          name='preview image'
          value={previewImage}
          placeholder='Preview Image'
          onChange={(e) => setPreviewImage(e.target.value)}
        ></input>
      </label>
      {validations.previewImage && (<p>{validations.previewImage}</p>)}
      <h2>Schedule</h2>
      <label>
        Monday
        <input
          list='hours'
          name='mondayOpen'
          value={mondayopen}
          placeholder='Open'
          onChange={(e) => setMondayOpen(e.target.value)}
        ></input>
        <datalist id='hours'>
          <option value='Closed'></option>
          <option value='12:00am'></option>
          <option value='1:00am'></option>
          <option value='2:00am'></option>
          <option value='3:00am'></option>
          <option value='4:00am'></option>
          <option value='5:00am'></option>
          <option value='6:00am'></option>
          <option value='7:00am'></option>
          <option value='8:00am'></option>
          <option value='9:00am'></option>
          <option value='10:00am'></option>
          <option value='11:00am'></option>
          <option value='12:00pm'></option>
          <option value='1:00pm'></option>
          <option value='2:00pm'></option>
          <option value='3:00pm'></option>
          <option value='4:00pm'></option>
          <option value='5:00pm'></option>
          <option value='6:00pm'></option>
          <option value='7:00pm'></option>
          <option value='8:00pm'></option>
          <option value='9:00pm'></option>
          <option value='10:00pm'></option>
          <option value='11:00pm'></option>
        </datalist>
      </label>
      {validations.schedule && (<p>{validations.schedule}</p>)}
      <label>
        <input
            list='hours'
            name='mondayClose'
            value={mondayclose}
            placeholder='Close'
            onChange={(e) => setMondayClose(e.target.value)}
        ></input>
        <datalist id='hours'>
          <option value='Closed'></option>
          <option value='12:00am'></option>
          <option value='1:00am'></option>
          <option value='2:00am'></option>
          <option value='3:00am'></option>
          <option value='4:00am'></option>
          <option value='5:00am'></option>
          <option value='6:00am'></option>
          <option value='7:00am'></option>
          <option value='8:00am'></option>
          <option value='9:00am'></option>
          <option value='10:00am'></option>
          <option value='11:00am'></option>
          <option value='12:00pm'></option>
          <option value='1:00pm'></option>
          <option value='2:00pm'></option>
          <option value='3:00pm'></option>
          <option value='4:00pm'></option>
          <option value='5:00pm'></option>
          <option value='6:00pm'></option>
          <option value='7:00pm'></option>
          <option value='8:00pm'></option>
          <option value='9:00pm'></option>
          <option value='10:00pm'></option>
          <option value='11:00pm'></option>
        </datalist>
      </label>
      <label>
        Tuesday
        <input
          list='hours'
          name='tuesdayOpen'
          value={tuesdayopen}
          placeholder='Open'
          onChange={(e) => setTuesdayOpen(e.target.value)}
        ></input>
        <datalist id='hours'>
          <option value='Closed'></option>
          <option value='12:00am'></option>
          <option value='1:00am'></option>
          <option value='2:00am'></option>
          <option value='3:00am'></option>
          <option value='4:00am'></option>
          <option value='5:00am'></option>
          <option value='6:00am'></option>
          <option value='7:00am'></option>
          <option value='8:00am'></option>
          <option value='9:00am'></option>
          <option value='10:00am'></option>
          <option value='11:00am'></option>
          <option value='12:00pm'></option>
          <option value='1:00pm'></option>
          <option value='2:00pm'></option>
          <option value='3:00pm'></option>
          <option value='4:00pm'></option>
          <option value='5:00pm'></option>
          <option value='6:00pm'></option>
          <option value='7:00pm'></option>
          <option value='8:00pm'></option>
          <option value='9:00pm'></option>
          <option value='10:00pm'></option>
          <option value='11:00pm'></option>
        </datalist>
      </label>
      {validations.schedule && (<p>{validations.schedule}</p>)}
      <label>
        <input
            list='hours'
            name='tuesdayClose'
            value={tuesdayclose}
            placeholder='Close'
            onChange={(e) => setTuesdayClose(e.target.value)}
        ></input>
        <datalist id='hours'>
          <option value='Closed'></option>
          <option value='12:00am'></option>
          <option value='1:00am'></option>
          <option value='2:00am'></option>
          <option value='3:00am'></option>
          <option value='4:00am'></option>
          <option value='5:00am'></option>
          <option value='6:00am'></option>
          <option value='7:00am'></option>
          <option value='8:00am'></option>
          <option value='9:00am'></option>
          <option value='10:00am'></option>
          <option value='11:00am'></option>
          <option value='12:00pm'></option>
          <option value='1:00pm'></option>
          <option value='2:00pm'></option>
          <option value='3:00pm'></option>
          <option value='4:00pm'></option>
          <option value='5:00pm'></option>
          <option value='6:00pm'></option>
          <option value='7:00pm'></option>
          <option value='8:00pm'></option>
          <option value='9:00pm'></option>
          <option value='10:00pm'></option>
          <option value='11:00pm'></option>
        </datalist>
      </label>
      {/* <label>
        <input
            type='text'
            name=''
            value={}
            placeholder=''
            onChange={(e) => (e.target.value)}
        ></input>
      </label>
      {validations. && (<p>{validations.}</p>)} */}
      <button type='submit' disabled={Object.keys(validations).length > 0}>{ buttonName }</button>
    </form>
  )
}

export default CreateNewBusiness
