# munch!
[![aa-projects-munch.png](https://i.postimg.cc/pV7s4077/aa-projects-munch.png)](https://postimg.cc/DmrQbc7d)
## User Stories

## URL
https://aa-munch.onrender.com

### Sign Up
- As an unregistered and unauthorized user, I want to be able to sign up for the website via a sign-up form.
- When I'm on the `/signup` page:
  - I would like to be able to enter my email, username, and preferred password on a clearly laid out form.
  - I would like the website to log me in upon successful completion of the sign-up form, so that I can seamlessly access the site's functionality.
  - When I enter invalid data on the sign-up form:
    - I would like the website to inform me of the validations I failed to pass and repopulate the form with my valid entries (except my password), so that I can try again without needing to refill forms I entered valid data into.

### Log in
- As a registered and unauthorized user, I want to be able to log in to the website via a log-in form.
- When I'm on the `/login` page:
  - I would like to be able to enter my email and password on a clearly laid out form.
  - When I enter invalid data on the log-up form:
    - I would like the website to inform me of the validations I failed to pass and repopulate the form with my valid entries (except my password), so that I can try again without needing to refill forms I entered valid data into.

### Demo User
- As an unregistered and unauthorized user, I would like an easy-to-find and clear button on both the `/signup` and `/login` pages to allow me to visit the site as a guest without signing up or logging in.
- When I'm on either the `/signup` or `/login` pages:
  - I can click on a Demo User button to log me in and allow me access as a normal user, so that I can test the site's features and functionality without needing to stop and enter credentials.

### Log Out
- As a logged-in user, I want to log out via an easy-to-find log out button on the navigation bar.
- While on any page of the site:
  - I can log out of my account and be redirected to the landing change.
  - So that I can easily log out to keep my information secure.


## Businesses
> Create, Read, Update, Delete
### Creating a Business
- As a logged-in user, I want to be able to create a new Business by providing relevant information such as name, address, category, location, etc.
- When I'm on any page I can click a button to redirect me to `/business/new` page to create a new business:
  - I can create and submit a new Business.
  - I can add Menu Items and Images (Optional).
  - I can specify Hours of Operation.
  - I can specify Amenities (i.e. parking, Wi-Fi, wheelchair accessibility, etc.).

### Viewing a Business
- As a logged-in or logged-out user, I want to be able to view a selection of the spots.
- When I'm on the `/businesses` page:
  - I can view all the spots.
- As a logged-in or logged-out user, I want to be able to view a specific spot and its associated spot reviews and rating.
- When I'm on the `/business/:businessId` page:
  - I can view the content of the spot, as well as the associated reviews, menu items, and amenities.

### Updating a Business
- As a logged-in user, I want to be able to edit my spot by clicking an Edit button associated with the user-owned spot.
- When I'm on the `/business/:businessId`, or `/users/:id/businesses` pages:
  - I can click "Edit" to make permanent changes to the spot I have posted, so that I can fix any errors I make in my spot.

### Deleting a Business
- As a logged-in user, I want to be able to delete my Business by clicking a Delete button associated with the Business(s) that I own.
- When I'm on the `/business/:businessId`, or `/users/:id/businesses` pages:
  - I can click "Delete" to permanently delete a business I have listed.

## Review
> Create, Read, Update, Delete
### Create Review
- As a logged-in user, I want to be able to create a new review on a business by providing relevant information such as star rating, description, and photos.
- When I'm on the `/business/:businessId` page:
  - I can create and submit a new Review on that business.
  - I can add star rating, review description, and photos (optional).

### Viewing Reviews
- As a logged-in or logged-out user, I want to be able to view a selection of the reviews.
- When I'm on the `/business/:businessId` page:
  - I can view all the reviews.

### Updating a Review
- As a logged-in user, I want to be able to edit my review by clicking an Edit button associated with the user review.
- When I'm on the `/business/:businessId`, or `/users/:id/profile` pages:
  - I can click "Edit" to make permanent changes to the review I have posted, so that I can fix any errors I make in my review.

### Deleting a Review
- As a logged-in user, I want to be able to delete my review for a business by clicking a Delete button associated with the review(s) I’ve made.
- When I'm on the `/business/:businessId`, or `/users/:id/profile` pages:
  - I can click "Delete" to permanently delete a business I have listed.

## Menu
> Create, Read
### Creating a Menu
- As a logged-in user, I want to be able to create a new Menu by providing relevant information.
  - Done on creation of a new business.

### Viewing a Menu
- As a logged-in or logged-out user, I want to be able to view a selection of the menu items.
  - When I'm on the `/business/:businessId/menu` page:
    - I can view all the menu items.

## Amenities
> Create, Read
### Creating Amenities
- As a logged-in user, I want to be able to create Amenities by providing relevant information.
  - Done on creation of a new business.

### Viewing Amenities
- As a logged-in or logged-out user, I want to be able to view a selection of the amenities.
  - When I'm on the `/business/:businessId` page:
    - I can view all the amenities.
