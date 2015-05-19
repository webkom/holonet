import React from 'react';

import Navbar from './navbar/navbar';
import Activity from './activity/activity';

export default class App extends React.Component {

  navbarLinks() {
    return {
      left: [
        {text: 'Profile', url: '/profile'}
      ],
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
        <Activity />
      </div>
    );
  }

}
