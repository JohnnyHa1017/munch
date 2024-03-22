import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import { useSelector } from 'react-redux';
import "./Navigation.css";
import landinglogo from '../../images/landinglogo.png'

function Navigation() {
  const user = useSelector(state => state.session.user)

  return (
    <ul className='nav-bar-ul'>
      <li>
        <NavLink to="/" className='Landinglogo'>
          <img src={landinglogo} alt='landinglogo'/>
        </NavLink>

      </li>
      {user && (
        <>
          <li>
            <NavLink to='/business/new'>Create a New Business</NavLink>
          </li>
          <li>
            <NavLink to={`/user/${user.id}/business`}>Manage Your Business</NavLink>
          </li>
        </>
        )
      }
      <li>
        <ProfileButton />
      </li>
    </ul>
  );
}

export default Navigation;
