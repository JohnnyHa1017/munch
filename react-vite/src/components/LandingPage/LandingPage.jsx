import {  useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { landingPageThunk } from '../../redux/business'
// import { useModal } from "../../context/Modal";
// import { landingPageThunk } from '../../redux/business'
// import { SignupFormModal } from '../SignupFormModal'
// import { LoginFormModal } from '../LoginFormModal'
// import { OpenModalButton } from '../OpenModalButton'
// import { ProfileButton } from '../Navigation'

export default function LandingPage() {

    const dispatch = useDispatch()

    const data = useSelector((state) => state.business)
    console.log(data)

    useEffect(() => {
        dispatch(landingPageThunk())
    }, [dispatch])

    return (
        <>
            <h1>Landing Page!</h1>
        </>

    )
}
