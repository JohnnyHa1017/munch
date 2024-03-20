import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import LandingPage from '../components/LandingPage'
import Layout from './Layout';
import { RouterProvider } from "react-router-dom";
import OneBusiness from '../components/Businesses/Businesses';
import CreateNewBusiness from '../components/CreateBusiness/CreateBusiness';
import BusinessReviews from '../components/BusinessReviews/BusinessReviews'
import AllReviews from '../components/allReviews/allReviews'
import CreateReview from '../components/CreateReview/CreateReview'

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
        element: <CreateNewBusiness />
      },
      //testing paths
      {
        path: 'reviews/all',
        element: <AllReviews/>
      },
      {
        path: 'business/:businessId/reviews',
        element: <BusinessReviews/>
      },
      {
        path: 'business/:businessId/review/new',
        element: <CreateReview />
      },
    ],
  },
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App;
