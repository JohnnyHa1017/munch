import {  useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { businessAmenitiesThunk, businessMenuThunk, specificBusinessThunk } from '../../redux/business'
import { useParams } from 'react-router-dom'

// TODO: Pass in reviews

export default function OneBusiness() {
  const dispatch = useDispatch()
  const data = useSelector((state) => state.business)
  const { businessId } = useParams()

  useEffect(() => {
    dispatch(specificBusinessThunk(businessId))
    dispatch(businessMenuThunk(businessId))
    dispatch(businessAmenitiesThunk(businessId))
  }, [businessId, dispatch])

  if (!data[businessId]) {
    return <div>Loading...</div>
  }

  return (
    <>
      <h1>Business Id Page</h1>
      <p>{data[businessId].title}</p>
      <h2>Schedule</h2>
      <p>{data[businessId].schedule}</p>
    </>
  )
}
