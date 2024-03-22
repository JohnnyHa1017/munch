import { FaSearch } from 'react-icons/fa'
import { useState } from "react"
import './SearchBar.css'

const SearchBar = () => {
    const [input, setInput] = useState('')


    return (
        <form className='input-wrapper'>
            <FaSearch id='search-icon' />
            <input className='search-input'
                type='text'
                placeholder='Type to search...'
                value={input}
                onChange={(e) => setInput(e.target.value)}
            />
            <button className='fasfaSearch' onClick={() => alert('Feature coming soon')} type='submit'><FaSearch /></button>
        </form>
    )
}

export default SearchBar
