import React from 'react';

import Navbar from './navbar/navbar';

export default class App extends React.Component {

  navbarLinks() {
    return {
      left: [],
      right: [
        {text: 'API', url: '/api'},
        {text: 'Logout', url: '/logout'}
      ]
    };
  }

  render() {
    return (
      <div className='container'>
        <Navbar links={this.navbarLinks()} />
      </div>
    );
  }

}
