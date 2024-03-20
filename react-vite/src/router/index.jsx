import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import LandingPage from '../components/LandingPage'
import Layout from './Layout';
import { RouterProvider } from "react-router-dom";
import OneBusiness from '../components/Businesses/Businesses';
import CreateBusiness from '../components/CreateBusiness/CreateBusiness';
import UpdateBusiness from '../components/UpdateBusiness/UpdateBusiness';

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <LandingPage />,
      },
      {
        path: "login",
        element: <LoginFormPage />,
      },
      {
        path: "signup",
        element: <SignupFormPage />,
      },
      {
        path: "business/:businessId",
        element: <OneBusiness />
      },
      {
        path: "business/new",
        element: <CreateBusiness />
      },
      {
        path: "business/:id/edit",
        element: <UpdateBusiness />
      }
    ],
  },
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App;
