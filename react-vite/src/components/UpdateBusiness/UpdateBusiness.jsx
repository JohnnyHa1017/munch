import { useSelector, useDispatch } from "react-redux"
import CreateNewBusiness from "../BusinessForm/BusinessForm"
import { useParams } from "react-router-dom";
import { useEffect } from "react";
import { specificBusinessThunk } from "../../redux/business";

const UpdateBusiness = () => {
  const state = useSelector((state) => state.business)
  const buttonName = 'Update a Business'
  const dispatch = useDispatch();
  const { businessId } = useParams();

  if (!state) {
    return <h1>Loading...</h1>
  }

  const business = state[businessId]

  useEffect(() => {
    dispatch(specificBusinessThunk(businessId))
  }, [businessId, dispatch])

  return (
    <>
      <h1>Update Business</h1>
      <CreateNewBusiness buttonName={buttonName} business={ business } />
    </>
    )
}

export default UpdateBusiness
