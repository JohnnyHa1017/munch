import { deleteBusinessThunk, specificBusinessThunk } from "../../redux/business"
import { useDispatch, useSelector } from "react-redux"
import { useNavigate, useParams } from 'react-router-dom';
import {  useEffect } from "react";

function DeleteBusiness() {
    const state = useSelector(state => state.business)
    const { businessId } = useParams()
    const dispatch = useDispatch();
    const nav = useNavigate()

    useEffect(()=>{
        dispatch(specificBusinessThunk(businessId))
    }, [businessId, dispatch])

    const deleteBusiness = async (e) => {
        e.preventDefault();
        dispatch(deleteBusinessThunk(state[businessId]))
        nav('/')
    }

    return(
        <>
            <button onClick={deleteBusiness}>Delete</button>
        </>
    )
}

export default DeleteBusiness
