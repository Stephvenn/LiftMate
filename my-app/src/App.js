import React from 'react';
import './App.css';
import Navbar from './components/NavBar';
import {
  BrowserRouter as Router, 
  Routes, 
  Route, 
  Link
} from 'react-router-dom';

function App() {
  return (
    <>
    <Router>
      <Navbar />
      <Routes>
        <Route path='/' exact/>
      </Routes>
    </Router>
    </>
  );
}

export default App;
