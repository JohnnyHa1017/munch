import React from 'react'
import { Carousel } from 'react-responsive-carousel';
import "react-responsive-carousel/lib/styles/carousel.min.css";

import bleach from '../../images/bleach.png'
import MHplatter from '../../images/MHplatter.jpg'
import MHplatter2 from '../../images/MHplatter2.png'
import Op from '../../images/OP.png'
import stardew from '../../images/stardew.jpeg'
import './Carousel.css'

function ImageCarousel(){
    return(
        <>
         <Carousel className='main-slide'>
                <div>
                    <img src={bleach}height='400px'width='300px'/>
                </div>
                <div>
                    <img src={MHplatter}height='400px'width='300px' />
                </div>
                <div>
                    <img src={MHplatter2}height='400px'width='300px' />
                </div>
                <div>
                    <img src={Op}height='400px'width='300px' />
                </div>
                <div>
                    <img src={stardew}height='400px'width='300px' />
                </div>
            </Carousel>
        </>
    )
}

export default ImageCarousel
