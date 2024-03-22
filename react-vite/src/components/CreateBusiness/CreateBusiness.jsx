import CreateNewBusiness from "../BusinessForm/BusinessForm"


const CreateBusiness = () => {
  const buttonName = 'Create a New Business'

  const business ={
    title: '',
    address: '',
    city: '',
    state: '',
    country: '',
    description: '',
    phone_number: '',
    price_rating: '',
    lat: '',
    lng: '',
    category: '',
    schedule: '',
    image: null
  }

  return (
    <>
      <h1>Create Your New Business</h1>
      <CreateNewBusiness buttonName={ buttonName } business={ business }/>
    </>
    )
}

export default CreateBusiness
