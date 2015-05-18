import React from 'react';

export default class Navbar extends React.Component{

  render() {

    let left = this.props.links.left;
    let right = this.props.links.right;

    return (
      <nav className='navbar navbar-default navbar-inverse'>
        <div className='container-fluid'>
          <div className='navbar-header'>
            <a className='navbar-brand' href='/'>Holonet</a>
          </div>
          <ul className='nav navbar-nav'>
            {left.map((link, i) => {
              return (
                <li key={i}><a href={link.url}>{link.text}</a></li>
              );
            })
            }
          </ul>
          <ul className='nav navbar-nav navbar-right'>
            {right.map((link, i) => {
              return (
                <li key={i}><a href={link.url}>{link.text}</a></li>
              );
            })
            }
          </ul>
        </div>
      </nav>
    );
  }
}
