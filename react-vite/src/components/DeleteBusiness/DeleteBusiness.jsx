import { deleteBusinessThunk, specificBusinessThunk } from "../../redux/business"
import { useDispatch, useSelector } from "react-redux"
import { useNavigate, useParams } from 'react-router-dom';
import {  useEffect } from "react";

function DeleteBusiness() {
    const dispatch = useDispatch();
    const nav = useNavigate()
    const { businessId } = useParams()
    const state = useSelector (state => state.business)
    useEffect(()=>{
        dispatch(specificBusinessThunk(businessId))
    },[businessId, dispatch])

    if(!state){
        return <div>Loading...</div>
    }

    console.log(businessId, '<--- should be the actual id number')
    console.log(state, '<--- business obj of the id we are trying to delete')
    console.log(state[businessId], '<---- the object only')
    console.log(state[businessId].id, '<---- just a number')

    const deleteBusiness = async (e) => {
        e.preventDefault();
        await dispatch(deleteBusinessThunk(state[businessId]))
        // nav('/')
    }

    return(
        <>
            <button onClick={deleteBusiness}>Delete</button>
        </>
    )
}

export default DeleteBusiness
