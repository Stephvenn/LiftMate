import React, {useState} from 'react';
import './NavBar.css'
import {
    BrowserRouter as Router, 
    Routes, 
    Route, 
    Link
} from 'react-router-dom';

function NavBar() {
  return (
    <>
        <nav className='navbar'>
            <div className='navbar-container'>
                <li><Link to="/" className='title-one'>LIFT</Link></li>
                <li><Link to="/" className='title-two'>MATE</Link></li>
            </div>
        </nav>
    </>
    
  )
}

export default NavBar