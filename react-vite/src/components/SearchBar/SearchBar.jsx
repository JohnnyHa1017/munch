import { FaSearch } from 'react-icons/fa'
import { useState } from "react"
import './SearchBar.css'

const SearchBar = () => {
    const [input, setInput] = useState('')


    return (
        <form className='input-wrapper'>
            <FaSearch id='search-icon' />
            <input
                type='text'
                placeholder='Type to search...'
                value={input}
                onChange={(e) => setInput(e.target.value)}
            />
            <button type='submit'>Search</button>
        </form>
    )
}

export default SearchBar
