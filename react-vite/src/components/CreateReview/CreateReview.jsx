import CreateNewReview from "../ReviewForm/ReviewForm";

const CreateReview = () => {
    const buttonName = 'Create Review'

    const review = {
        review: '',
        star:'',
        image:''
    }

    return (
        <>
            <h1>Create a Review</h1>
            <CreateNewReview reviewToUpdate={review} buttonName={buttonName}/>
        </>
    )
}

export default CreateReview
