import React from 'react';
import ReactDOM from 'react-dom';

function MyApp(){
  return (
  <div>
    <p>
      this commes forom function
    </p>
    <strong>Dekh bhai</strong>
  </div>
  )
} 

ReactDOM.render(
  <MyApp />
  ,document.getElementById('root')
)
