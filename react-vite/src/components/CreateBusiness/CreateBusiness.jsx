import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useNavigate } from 'react-router-dom'
import { createNewBusinessThunk } from '../../redux/business'

const CreateNewBusiness = () => {
  const dispatch = useDispatch()
  const nav = useNavigate()
  const user = useSelector((state) => state.session.user)

  const [title, setTitle] = useState('');
  const [address, setAddress] = useState('');
  const [city, setCity] = useState('');
  const [state, setState] = useState('');
  const [country, setCountry] = useState('');
  const [lat, setLat] = useState('');
  const [lng, setLng] = useState('');
  const [description, setDescription] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');
  const [price, setPrice] = useState();
  const [category, setCategory] = useState('');
  const [schedule, setSchedule] = useState('');
  const [previewImage, setPreviewImage] = useState('');
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
    if (!phoneNumber || (phoneNumber.length > 20)) {
      errors.phoneNumber = "Phone Number is required and must be unique, can't be more than 20 characters."
    }
    if (!price) {
      errors.price = "Price Rating is required and must be an integer of 1 to 5."
    }
    if (!category) {
      errors.category = 'Atleast one category must be selected.'
    }

    setValidations(errors)
  }, [user, nav, title, address, city, state, country, lat, lng, description, phoneNumber, price, category, schedule, previewImage])

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSubmitted(true);
    if (!Object.keys(validations).length) {
      const business = dispatch(createNewBusinessThunk({
        title,
        address,
        city,
        state,
        country,
        description,
        phoneNumber,
        price,
        category,
        schedule,
        previewImage
      })
      )
      nav(`/business/${business.id}`);
    }
    // setTitle('');
    // setAddress('');
    // setCity('');
    // setState('');
    // setCountry('');
    // setLat('');
    // setLng('');
    // setDescription('');
    // setPhoneNumber('');
    // setPrice('');
    // setCategory('');
    // setSchedule('');
    // setPreviewImage('');
  }

  return (
    <form
      className='business-form'
      onSubmit={handleSubmit}
    >
      <h1>Create Business</h1>
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
          value={price}
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
          value={ category }
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
          value={phoneNumber}
          placeholder='Phone Number'
          onChange={(e) => setPhoneNumber(e.target.value)}
        ></input>
      </label>
      {validations.phoneNumber && (<p>{validations.phoneNumber}</p>)}
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
        Schedule
        <input
          type='text'
          name='schedule'
          value={schedule}
          placeholder='Schedule'
          onChange={(e) => setSchedule(e.target.value)}
        ></input>
      </label>
      {validations.schedule && (<p>{validations.schedule}</p>)}
      <label>
        Preview Image
        <input
          type='text'
          name='preview image'
          value={previewImage}
          placeholder='Preview Image'
          onChange={(e) => setPreviewImage(e.target.value)}
        ></input>
      </label>
      {validations.previewImage && (<p>{validations.previewImage}</p>)}
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
      <button type='submit' disabled={Object.keys(validations).length >= 1}>Create New Business!</button>
    </form>
  )
}

export default CreateNewBusiness
