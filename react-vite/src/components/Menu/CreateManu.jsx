import { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { useNavigate, useParams } from 'react-router-dom'
import { createMenuThunk } from '../../redux/menu'
import './Menu.css'


function CreateMenu() {
    const dispatch = useDispatch()
    const { businessId } = useParams()
    const user = useSelector((state) => state.session.user)
    const nav = useNavigate()

    console.log('businessId ==>', businessId)

    const [name, setName] = useState('')
    const [category, setCategory] = useState('')
    const [price, setPrice] = useState('')
    const [description, setDescription] = useState('')
    const [validations, setValidations] = useState('')
    const [submitted, setSubmitted] = useState(false)


    useEffect(() => {
        const errors = {}
        if (!user) {
            nav('/')
        }
        if (!name || name.length > 50) {
            errors.name = 'Name is required and can only be under 50 characters'
        }
        if (!category || !['Drink', 'Appetizer', 'Entree', 'Dessert', 'Specials'].includes(category)) {
            errors.category = 'Menu category must be one of: Drink, Appetizer, Entree, Dessert, or Specials.'
        }
        if (!price) {
            errors.price = 'Price is required'
        }
        if (description.length < 2000) {
            errors.description = 'Description must be under 2000 characters'
        }
        setValidations(errors)
    }, [user, nav, name, category, price])


    const handleSubmit = async (e) => {
        e.preventDefault()
        setSubmitted(true)
        const newMenu = {
            name, category, price, description
        }
        if (!Object.keys(validations).length) {
            await dispatch(createMenuThunk(businessId, newMenu))
        }
    }

    return (
        <>
            <h1>Create Menu!</h1>

            <form onSubmit={handleSubmit} className='menu-form'>
                <label>
                    Menu Item Name
                    <input
                        type='text'
                        name='name'
                        value={name}
                        placeholder='Menu Name'
                        onChange={(e) => setName(e.target.value)}
                    ></input>
                </label>
                {validations.name && (<p className='validation-messages'>{validations.name}</p>)}
                <label>
                    Menu Item Category
                    <select onChange={(e) => setCategory(e.target.value)}>
                        <option value='Appetizer' >Appetizer</option>
                        <option value='Drink' >Drink</option>
                        <option value='Entree' >Entree</option>
                        <option value='Dessert' >Dessert</option>
                        <option value='Specials' >Specials</option>
                    </select>
                </label>
                {validations.category && (<p className='validation-messages'>{validations.category}</p>)}
                <label>
                    Price
                    <input
                        type='text'
                        name='price'
                        value={price}
                        placeholder='Price'
                        onChange={(e) => setPrice(parseFloat(e.target.value))}
                    ></input>
                </label>
                {validations.price && (<p className='validation-messages'>{validations.price}</p>)}

            </form>

        </>
    )
}

export default CreateMenu
